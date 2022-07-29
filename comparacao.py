import face_recognition

def compare(imagem_1, imagem_2) -> bool:

    try:
        load_imagem_1 = face_recognition.load_image_file(imagem_1)
        encoding_imagem_1 = face_recognition.face_encodings(load_imagem_1)[0]
    except:
        raise Exception("Não foi possível localizar a imagem da primeira foto. Favor verificar se a foto esta rotacionada corretamente e sem mascara")

    try:
        load_imagem_2 = face_recognition.load_image_file(imagem_2)
        encoding_imagem_2 = face_recognition.face_encodings(load_imagem_2)[0]
    except:
        raise Exception("Não foi possível localizar a imagem da segunda foto. Favor verificar se a foto esta rotacionada corretamente e sem mascara")


    try:
        # quanto menor o valor de tolerance, mais criterioso se torna
        results = face_recognition.compare_faces([encoding_imagem_1], encoding_imagem_2, tolerance=0.59)

        return results[0]
    except:
        raise Exception("Não foi comparar as imagens")


if __name__ == "__main__":

    try:
        result = compare("../imagens/sung_kang_1.jpg", "../imagens/erro_2.jpeg")

        if result == True:
            print("A foto um é da mesma pessoa da foto dois")
        else:
            print("A foto um NÃO é da mesma pessoa da foto dois")

    except Exception as ex:
        print(ex)

