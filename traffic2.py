from gpiozero import LED
from time import sleep
import cv2
import numpy as np
import random

all_images = ["all_images/cars1.jpg","all_images/cars2.jpg","all_images/cars3.jpg","all_images/cars4.jpg","all_images/cars5.jpg","all_images/cars6.jpg","all_images/cars7.jpg","all_images/cars8.jpg","all_images/cars9.jpg","all_images/cars10.jpg","all_images/cars11.jpg","all_images/cars12.jpg"]

# Cam Function
def camera():
    cam = cv2.VideoCapture(0)
    img_counter = 0

    while True:
        ret, image = cam.read()
        if (ret == False):
            print("failed to grab frame")
            break

        cv2.imshow('Imagetest',image)
        k = cv2.waitKey(1)
        if (k%256 == 32):
            img_name = "frame.png".format(img_counter)
            cv2.imwrite(img_name,image)
            print("screenshot")
            break

    cam.release()
    cv2.destroyAllWindows()

# Lane Functions
def Lane1():
    camera()
    image = cv2.imread("frame.png")
    grey = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    car_cascade = cv2.CascadeClassifier('cars.xml')
    cars = car_cascade.detectMultiScale(grey, 1.1, 1)
    global cnt1
    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cnt1 += 1
    print("Vehicle Count: ", cnt1)
    cv2.imshow("Lane1", image)
    cv2.waitKey(8000)
    cv2.destroyAllWindows()

def Lane2():
    image = cv2.imread(all_images[a])
    grey = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    car_cascade = cv2.CascadeClassifier('cars.xml')
    cars = car_cascade.detectMultiScale(grey, 1.1, 1)
    global cnt2
    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cnt2 += 1
    print("Vehicle Count: ", cnt2)
    cv2.imshow("Lane2", image)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

def Lane3():
    image = cv2.imread(all_images[b])
    grey = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    car_cascade = cv2.CascadeClassifier('cars.xml')
    cars = car_cascade.detectMultiScale(grey, 1.1, 1)
    global cnt3
    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cnt3 += 1
    print("Vehicle Count: ", cnt3)
    cv2.imshow("Lane3", image)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

def Lane4():
    image = cv2.imread(all_images[c])
    grey = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    car_cascade = cv2.CascadeClassifier('cars.xml')
    cars = car_cascade.detectMultiScale(grey, 1.1, 1)
    global cnt4
    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cnt4 += 1
    print("Vehicle Count: ", cnt4)
    cv2.imshow("Lane4", image)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

red1 = LED(4)
red2 = LED(26)
red3 = LED(16)
red4 = LED(25)
amber1 = LED(3)
amber2 = LED(19)
amber3 = LED(20)
amber4 = LED(8)
green1 = LED(2)
green2 = LED(13)
green3 = LED(21)
green4 = LED(7)

while True:

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0

    a = random.randint(0,11)
    b = random.randint(0,11)
    c = random.randint(0,11)


    Lane1()
    Lane4()

    amber2.off()
    amber3.off()
    red1.off()
    red4.off()
    sleep(0.5)

    green1.on()
    green4.on()
    red2.on()
    red3.on()
    if (cnt4 >= cnt1):
        sleep(cnt4)
    else:
        sleep(cnt1)

    green1.off()
    green2.off()
    amber1.on()
    amber4.on()
    sleep(3)

    Lane2()
    Lane3()

    amber1.off()
    amber4.off()
    red2.off()
    red3.off()
    sleep(0.5)

    #Lane2()
    #Lane3()

    green2.on()
    green3.on()
    red1.on()
    red4.on()
    if (cnt3 >= cnt2):
        sleep(cnt3)
    else:
        sleep(cnt2)

    green2.off()
    green3.off()
    amber2.on()
    amber3.on()
    sleep(3)