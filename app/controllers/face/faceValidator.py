import time

import face_recognition
import cv2
import imutils
import redis
import ast
import os
import numpy as np

from datetime import datetime

import concurrent.futures


def format_time(inicio, fin):
    return "{:.4f} segundos".format(fin-inicio)


def get_encodings(image):
    print(image[0], end="\t")
    print(f"{datetime.now()} \t {os.getppid()}")
    rgb = cv2.cvtColor(image[1], cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model="hog")
    encodings = face_recognition.face_encodings(rgb, known_face_locations=boxes, num_jitters=2, model="small")
    print(f"{datetime.now()} \t {os.getppid()} -> fin")
    return [arr.tolist() for arr in encodings]


def getNumpy2(ine):
    inicio = time.time()
    try:
        image = imutils.resize(ine, width=800)

        grades = [0, 90, 180, 270]
        images_rotadas = []

        for grade in grades:
            if grade == 0:
                images_rotadas.append([0,image])
            elif grade == 90:
                images_rotadas.append([90, cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)])
            elif grade == 180:
                images_rotadas.append([90, cv2.rotate(image, cv2.ROTATE_180)])
            elif grade == 270:
                images_rotadas.append([270, cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)])

        fotoEncodings = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(get_encodings, image) for image in images_rotadas]
            for future in concurrent.futures.as_completed(futures):
                encodings = future.result()
                for arr in encodings:
                    fotoEncodings.append(arr)

        fin = time.time()
        return {
            'numRostros': len(fotoEncodings),
            'arrays': fotoEncodings,
            'time': format_time(inicio, fin)
        }

    except Exception as e:
        print(f"error {e}")
        fin = time.time()
        return {
            'numRostros': 0,
            'arrays': [],
            'time': format_time(inicio, fin)
        }

def getNumpy(ine):
    inicio = time.time()
    try:
        image = imutils.resize(ine, width=500)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        grades = {0, 90, 180, 270}

        fotoEncodings = []

        for grade in grades:

            if grade == 0:
                image_rotada = rgb

            if grade == 90:
                image_rotada = cv2.rotate(rgb, cv2.ROTATE_90_CLOCKWISE)

            if grade == 180:
                image_rotada = cv2.rotate(rgb, cv2.ROTATE_180)

            if grade == 270:
                image_rotada = cv2.rotate(rgb, cv2.ROTATE_90_COUNTERCLOCKWISE)

            print(f"{datetime.now()} \t se rota image {grade} grados ")

            # img_color = cv2.cvtColor(image_rotada, cv2.COLOR_BGR2RGB)
            """
            boxes = face_recognition.face_locations(image_rotada, model="cnn")
            fotoEncodings_1 = face_recognition.face_encodings(image_rotada,
                                                              known_face_locations=boxes, num_jitters=1,
                                                              model="small")
            """
            boxes = face_recognition.face_locations(image_rotada, model="hog")
            #print(f"{grade} \t {boxes}")
            fotoEncodings_1 = face_recognition.face_encodings(image_rotada,
                                                              known_face_locations=boxes, num_jitters=2,
                                                              model="small")
            print(f"{datetime.now()} \t num rostros {len(fotoEncodings_1)} ")
            for arr in fotoEncodings_1:
                fotoEncodings.append(arr.tolist())


        fin = time.time()
        return {
            'numRostros': len(fotoEncodings),
            'arrays': fotoEncodings,
            'time': format_time(inicio, fin)
        }


    except Exception as e:
        print(f"error {e}")

        fin = time.time()
        return {
            'numRostros': 0,
            'arrays': [],
            'time': format_time(inicio, fin)
        }