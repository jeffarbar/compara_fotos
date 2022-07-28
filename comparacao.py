import face_recognition

def compare(imagem_1, imagem_2) -> bool:

    picture_of_me = face_recognition.load_image_file(imagem_1)
    foto_um_encoding = face_recognition.face_encodings(picture_of_me)[0]

    #print('Encoding da primeira imagem ' + str(foto_um_encoding))

    #variavel foto_um_encoding agora contém uma 'codificação' universal de minhas características faciais que podem
    #ser comparado a qualquer outra foto de um rosto

    unknown_picture = face_recognition.load_image_file(imagem_2)
    foto_dois_encoding = face_recognition.face_encodings(unknown_picture)[0]

    #print('Encoding da segunda imagem ' + str(foto_dois_encoding))

    #Agora podemos ver que as duas codificações de face são da mesma pessoa com metodo compare_faces

    # quanto menor o valor de tolerance, mais criterioso se torna
    results = face_recognition.compare_faces([foto_um_encoding], foto_dois_encoding, tolerance=0.57)

    return results[0]



if __name__ == "__main__":

    result = compare("./imagens/sung_kang_2.jpg", "./imagens/sung_kang_1.jpg")

    if result == True:
        print("A foto um é da mesma pessoa da foto dois")
    else:
        print("A foto um NÃO é da mesma pessoa da foto dois")

