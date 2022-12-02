import requests
import os.path
import cv2
import numpy as np


def get(year=2021, month=11, day=6, hour=10, minute=0):

    url = "https://img1.kachelmannwetter.com/images/data/cache/wwanalyze/wwanalyze_%04d_%02d_%02d_262_%02d%02d.png" % (year,month,day,hour, minute)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    image_path = 'images/' + os.path.basename(url)

    if  os.path.exists(image_path) == True:
        print('File exists')
    else:
        print('download file from ' + url)
        response = requests.get(url, headers=headers)
        open(image_path, "wb").write(response.content)

    return image_path


def check(image_path):
    img = cv2.imread(image_path)

    x = 200
    y = 170
    w = 100
    h = 100

    a = ( w * h )

    crop_img = img[y:y+h, x:x+w]

    YELLOW_MIN = np.array([40, 235, 235], np.uint8)
    YELLOW_MAX = np.array([60, 255, 255], np.uint8)

    BLUE_MIN = np.array([190, 70, 0], np.uint8)
    BLUE_MAX = np.array([220, 120, 40], np.uint8)

    dst = cv2.inRange(crop_img, YELLOW_MIN, YELLOW_MAX)
    yellow = cv2.countNonZero(dst)

    dst = cv2.inRange(crop_img, BLUE_MIN, BLUE_MAX)
    blue = cv2.countNonZero(dst)

    if( blue/ a > 0.5 ):
        print('Percentage of blue is: ' + str(blue/a*100) + '%. Delete.')
        os.remove(image_path)
        return

    print('Percentage of yellow is: ' + str(yellow/a*100) + '%')

    #show(crop_img)


def show(img):
    cv2.namedWindow("opencv")
    cv2.imshow("opencv",img)
    cv2.waitKey(0)
    exit

