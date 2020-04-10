import cv2
import numpy as np
import os

eigenface = cv2.face.EigenFaceRecognizer_create(num_components=50, threshold=0)# quando menor, mais parecidas as faces tem que ser
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()


def getImagemComId():
    caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]
    # print(caminhos)
    faces = []
    ids = []
    for caminhoImagem in caminhos:
        imagemface = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(caminhoImagem)[-1].split('.')[1])
        print(id)
        ids.append(id)
        faces.append(imagemface)
        # cv2.imshow("Face", imagemface)
        # cv2.waitKey(10)
    return np.array(ids), faces

ids, faces = getImagemComId()
# print(faces)


print("Treinando...")

eigenface.train(faces, ids)
eigenface.write('classificadorEigen.yml')