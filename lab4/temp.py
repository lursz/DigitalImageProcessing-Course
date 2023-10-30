from tkinter import W
import cv2
import os
import requests
from matplotlib import pyplot as plt
import numpy as np

def IsWall(i, j, W, image):
    '''
    i - index of row
    j - index of column
    W - size of window
    '''
    result = []
    if i < W/2:
        result.append('u')
    if j < W/2:
        result.append('l')    
    if i > image.shape[0] - W/2:
        result.append('d')
    if j > image.shape[1] - W/2:
        result.append('r')
    return result

    

def Interpolation(image, W: int):
    # Calc an array of average values
    avg_brightness_arr = np.zeros((image.shape[0]//W, image.shape[1]//W))
    for i in range(0, image.shape[0], W):
        for j in range(0, image.shape[1], W):
            avg_brightness_arr[i//W, j//W] = np.average(image[i:i+W, j:j+W])


    dummy = np.zeros(image.shape)
    for j in range(image.shape[0]):
        for i in range(image.shape[1]):
            # Obliczenie indeksów iT i jT
            iT = i // W
            jT = j // W

            
            walls = IsWall(i, j, W, image)
            # corner
            if len(walls) == 2:
                brightness = avg_brightness_arr[iT, jT]
                test = image[i][j]

            # wall
            elif len(walls) == 1:
                if walls[0] in ['r', 'l']:
                    firstj = int(j - W/2) // W
                    secondj = firstj + 1
                    brightness = (avg_brightness_arr[iT, firstj] + avg_brightness_arr[iT, secondj]) / 2

                    dYup = j - W / 2 - jT * W
                    dYdown = (jT + 1) * W - j - W / 2

                    t11 = image[iT, firstj]
                    t12 = image[iT, secondj]

                    interpolation_y1 = (t11 * dYup / W) + (t12 * dYdown / W)
                    test = int(interpolation_y1)
                    
                else:
                    firsti = int(i - W/2) // W
                    secondi = firsti + 1
                    brightness = (avg_brightness_arr[firsti, jT] + avg_brightness_arr[secondi, jT]) / 2

                    dXleft = i - W / 2 - iT * W
                    dXright = (iT + 1) * W - i - W / 2

                    t11 = image[firsti, jT]
                    t12 = image[secondi, jT]

                    interpolation_x1 = (t11 * dXleft / W) + (t12 * dXleft / W)
                    test = int(interpolation_x1)

            # rest
            else:
                firsti = int(i - W/2) // W
                secondi = firsti + 1

                firstj = int(j - W/2) // W
                secondj = firstj + 1
                print(firsti, secondi, firstj, secondj)
                brightness = int((avg_brightness_arr[firsti, firstj] + avg_brightness_arr[firsti, secondj] + \
                                     avg_brightness_arr[secondi, firstj] + avg_brightness_arr[secondi, secondj]) / 4)

                dXleft = i - W / 2 - iT * W
                dXright = (iT + 1) * W - i - W / 2

                dYup = j - W / 2 - jT * W
                dYdown = (jT + 1) * W - j - W / 2

                t11 = image[firsti, firstj]
                t12 = image[firsti, secondj]
                t21 = image[secondi, firstj]
                t22 = image[secondi, secondj]

                
                interpolation_x1 = (t11 * dXleft / W) + (t12 * dXright / W)
                interpolation_x2 = (t21 * dXleft / W) + (t22 * dXright / W)

                # Interpolacja w osi Y
                interpolated_value = (interpolation_x1 * dYup / W) + (interpolation_x2 * dYdown / W)
                test = int(interpolated_value)
            dummy[i, j] = 255 if test > brightness else 0

    plt.imshow(dummy, "gray")
    plt.axis("off")
    plt.show()




def AdaptBinarization(img, w: int) -> None:
    # Calc an array of average values
    threshold_arr = np.zeros((img.shape[0] // w, img.shape[1] // w))
    for i in range(0, img.shape[0], w):
        for j in range(0, img.shape[1], w):
            threshold_arr[i // w, j // w] = np.average(img[i : i + w, j : j + w])
    # Binarize
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i, j] = 255 if img[i, j] > threshold_arr[i // w, j // w] else 0

    # Plot
    plt.imshow(img, "gray")
    plt.axis("off")
    plt.show()


rice = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)
AdaptBinarization(rice, 16)
























def Piotrek():
    for x in range(img.shape[0]):
        for y in range (img.shape[1]):
            (xT, yT) = (x // W, y // W)
            (x_half_T, y_half_T) =(x //halfW, y// halfW))
            isXEdge = x_half_T == 0 or x_half_T == imgX_half_W - 1
            isYEdge = y_half_T == 0 or y_half_T == imgY_half_W - 1

            x_before_cell = (x - W // 2) // W
            x_after_cell = (x - W // 2) // W + 1

            y_before_cell = (y - W // 2) // W
            y_after_cell = (y - W // 2) // W + 1
            dx = x - W // 2 - xT * W
            dy = y - W // 2 - yT * W

            dx_part = (dx / W + 1) /2
            dy_part = (dy / W + 1) /2

            T = 0

            if isXEdge nad isYEdge:
T = everges_img[xT, yT]

