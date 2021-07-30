import os
import PIL.Image
import PIL.ImageDraw
import face_recognition
import glob
import cv2
import sys

def main(path):
    cv_img = []
    print(path)
    for img in glob.glob(path):
        n= cv2.imread(img)
        cv_img.append(n)
        image = face_recognition.load_image_file(img)
        face_locations = face_recognition.face_locations(image)
        number_of_faces = len(face_locations)
        print("I found {} face(s) in this photograph.".format(number_of_faces))
        if number_of_faces==1:
           #cv2.imwrite(output)
           pass

if __name__ == "__main__":
   main(sys.argv[1])
