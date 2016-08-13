# -*- coding: utf-8 -*-

# import click
from collections import deque
import numpy as np
import pandas as pd
import cv2
from digit_recognizer import read_number
import tensorflow as tf
import os


def filter_image(img):
    th = cv2.adaptiveThreshold(
        img,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        21,
        2)
    median = cv2.medianBlur(th, 7)

    ret, thresh = cv2.threshold(
        median, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # noise removal
    kernel = np.ones((2, 2), np.uint8)
    # opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

    # sure background area
    sure_bg = cv2.dilate(thresh, kernel, iterations=1)

    return sure_bg


def bounding_square(cnt):
    x,y,w,h = cv2.boundingRect(cnt)
    center_y = y + h / 2
    center_x = x + w / 2
    delta = int(0.7 * max(h, w))
    if center_x - delta < 0:
        x1 = 0
        x2 = 2 * delta
    else: 
        x1 = center_x - delta
        x2 = center_x + delta
    if center_y - delta < 0:
        y1 = 0
        y2 = 2 * delta
    else: 
        y1 = center_y - delta
        y2 = center_y + delta

    return y1, y2, x1, x2


# @click.command()
def main(args=None):
    """Console script for recognizer"""
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        cap = cv2.VideoCapture(0)

    frame_list = deque()
    number = None

    while True:
        # Read Frame
        _, frame = cap.read()

        # Plot a rectangle and define the ROI
        roi = frame[180:300, 180:460]

        # Get grayscaled image
        grayscaled = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        # Apply some filters
        filtered = filter_image(grayscaled)

        # Add frame to queue end remove the last one
        if len(frame_list) < 2:
            frame_list.append(filtered)
        else:
            frame_list.append(filtered)
            frame_list.popleft()

        # Reduce noise by averaging frames
        last = None
        for img in frame_list:
            if last != None:
                last = cv2.bitwise_and(filtered, filtered, mask=last)
            out = cv2.bitwise_and(img, img, mask=last)
            last = out

        # Find contours and contour areas
        image, contours, hierarchy = cv2.findContours(
            out, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnt_areas = [cv2.contourArea(x) for x in contours]

        # Get the a sorted list of images for each digit
        masks = []
        x_list = []
        for cnt in contours:       
            if cv2.contourArea(cnt) > max(cnt_areas)/3: 
                x,y,w,h = cv2.boundingRect(cnt)
                cv2.rectangle(roi,(x,y),(x+w,y+h),(0,255,0),2)
                y1, y2, x1, x2 = bounding_square(cnt)
                try:
                    mask = np.zeros(grayscaled.shape, np.uint8)
                    mask = cv2.drawContours(mask, [cnt], 0, (255,255,255), cv2.FILLED)
                    masks.append(cv2.resize(mask[y1:y2, x1:x2], (28, 28)))
                    x_list.append(x1)
                except:
                    raise
        masks = [x for (y,x) in sorted(zip(x_list,masks), key=lambda pair: pair[0])]

        # Display frames
        frame = cv2.rectangle(frame,(0,0),(frame.shape[1],40),(0,0,0),-1)
        cv2.putText(frame,'Number: '+str(number),(10,30), 1, 1.5,(255,255,255),1,cv2.LINE_AA)
        cv2.rectangle(frame, (200, 200), (440, 280), (0, 200, 0), 2)
        cv2.imshow('frame', frame)

        # Print number by pressing 'p'
        k = cv2.waitKey(5)
        if k == ord('r'):
            # Reshape images
            inputs_list = []
            for i, mask in enumerate(masks):
                inputs_list.append(mask.reshape(784))
            # Run model and print the result
            number = read_number(np.array(inputs_list))
        # Quit recording by pressing 'q'
        elif k == ord('q'):
            cap.release()
            break

    # Destroy all windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
