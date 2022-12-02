import requests
import os
import cv2
import numpy as np


def get(year=2021, month=11, day=6, hour=10, minute=0):

    url = "https://www.sat24.com/h-image.ashx?region=eu&time=%04d%02d%02d%02d%02d&ir=False" % (year,month,day,hour, minute)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    image_path = 'images/sat24_%04d-%02d-%02d-%02d-%02d.gif' % (year,month,day,hour, minute)

    if  os.path.exists(image_path) == True:
        print('File exists')
    else:
        print('download file from ' + url)
        response = requests.get(url, headers=headers)
        open(image_path, "wb").write(response.content)

        os.system('convert ' + image_path + ' ' + image_path.replace('.gif', '.png'))

    return image_path.replace('.gif', '.png')


def check(image_path):
    print(image_path)
    img = cv2.imread(image_path)

    x = 423
    y = 341
    w = 10
    h = 11

    a = ( w  * h)

    crop_img = img[y:y+h, x:x+w]

    WHITE_MIN = np.array([100, 100, 00], np.uint8)
    WHITE_MAX = np.array([200, 200, 190], np.uint8)

    dst = cv2.inRange(crop_img, WHITE_MIN, WHITE_MAX)
    white = cv2.countNonZero(dst)
    print(white, a)
    print('Percentage of white is: ' + str(white/a*100) + '%')

    show(crop_img)

def show(img):
    cv2.namedWindow("opencv")
    cv2.imshow("opencv",img)
    cv2.waitKey(0)


