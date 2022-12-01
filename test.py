import cv2
import numpy as np
import requests
import os.path

year = 2021
month = 11
day = 6
hour = 10
minute = 0
url = "https://img3.kachelmannwetter.com/images/data/cache/wwanalyze/download_wwanalyze-de-320-1_%04d_%02d_%02d_262_%02d%02d.png" % (year,month,day,hour, minute)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
image_path = 'images/' + os.path.basename(url)

if  os.path.exists(image_path) == True:
    print('File exists')
else:
    response = requests.get(url, headers=headers)
    open(image_path, "wb").write(response.content)


img = cv2.imread(image_path)
x = 50
y = 0
w = 500
h = 300

a = ( w - x ) * (h - y)

crop_img = img[y:y+h, x:x+w]

YELLOW_MIN = np.array([40, 235, 235], np.uint8)
YELLOW_MAX = np.array([60, 255, 255], np.uint8)

dst = cv2.inRange(crop_img, YELLOW_MIN, YELLOW_MAX)
no_brown = cv2.countNonZero(dst)
#print('The number of brown pixels is: ' + str(no_brown))
#print('Total number ' + str(a))

print('Percentage of yellow is: ' + str(no_brown/a*100) + '%')

#cv2.namedWindow("opencv")
#cv2.imshow("opencv",crop_img)
#cv2.waitKey(0)

