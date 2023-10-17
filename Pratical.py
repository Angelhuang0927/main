import glob
import cv2
import os
import matplotlib.pyplot as plt

des_path = r'D:\BrowserDownload\dogcatface\Dog_Cat\Dest'
image_path = r'D:\BrowserDownload\dogcatface\Dog_Cat\Cat'
i = 1
for img in glob.glob(image_path + '\*.png'):
    try:
        image = cv2.imread(img)
        img_resize = cv2.resize(image, (100, 100))
        os.chdir(des_path)
        filename = des_path + '/cat' + str(i) + '.png'
        cv2.imwrite(filename, image)
        i += 1
    except:
        print('Operation not executed')

des_path = r'D:\BrowserDownload\dogcatface\Dog_Cat\Gray'
image_path = r'D:\BrowserDownload\dogcatface\Dog_Cat\Dest'
n = 1
for img in glob.glob(image_path + '\*.png'):
    try:
        image = cv2.imread(img)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(9, (10, 10))
        new_clahe = clahe.apply(gray)
        os.chdir(des_path)
        filename = des_path + '/gray' + str(n) + '.png'
        cv2.imwrite(filename, new_clahe)
        n += 1
    except:
        print('Operation not executed')
