"""
- author: pramod khatiwada
- email : pramodkhatiwada03@gmail.com
"""
import os

import cv2
import numpy as np
import sys

from face_recognition.utils.imgutils import return_image
from face_recognition.utils.metrics import similarity

if __name__ == '__main__':
    src_path = os.path.join('data', 'dataset', 'test', '0000_02176.pgm')
    dest_path = os.path.join('data', 'dataset', 'test', '0000_02179.pgm')

    src = cv2.resize(cv2.cvtColor(np.array(return_image(src_path)), cv2.COLOR_RGB2GRAY), (64, 64))
    dest = cv2.resize(cv2.cvtColor(np.array(return_image(dest_path)), cv2.COLOR_RGB2GRAY), (64, 64))

    result = similarity(src, dest)

    result = image_ssim(resized_image_1, resized_image_2)
    print("{} - {} | Similarity score using Structural Similarity Index : {} .".format(path1, path2, result))
