import uuid
import os
from datetime import datetime
from PIL import Image
import threading
import constante as c

def salva(foto_1, foto_2, result) -> str:

    if c.salvar_imagem:

        try:
            atual = datetime.now() 
            meu_uuid = str(uuid.uuid4())  

            diretorio_uuid = "./" + meu_uuid + "_" + atual.strftime("%d%m%Y_%H%M%S")
            os.mkdir(diretorio_uuid)

            threads = list()

            t = threading.Thread(target=salva_imagem,
                                    args=(diretorio_uuid + "/foto_1.jpeg", foto_1)
                                )
            t.start()
            threads.append(t)

            t = threading.Thread(target=salva_imagem,
                                    args=(diretorio_uuid + "/foto_2.jpeg",foto_2)
                                )
            t.start()
            threads.append(t)

            t = threading.Thread(target=escrever,
                                    args=(diretorio_uuid + "/result.txt", "O Match foi " + str(result)+"."
                                )
                            )
            t.start()
            threads.append(t)

            for thread in threads:
                thread.join()

            return diretorio_uuid

        except Exception as ex:
            print(ex)



def salva_imagem(caminho, foto):

    if c.salvar_imagem:
        image = Image.open(foto)
        image.save(caminho)



def salva_avaliacao(uuid, avaliacao):

    if c.salvar_imagem:
        escrever("./" + uuid + "/result.txt", " A avaliacao foi " + str(avaliacao)+".")


def escrever(caminho, conteudo):
    if c.salvar_imagem:
        with open(caminho, "a") as arquivo:
            arquivo.write(conteudo)