import cv2
import numpy as np
import os

def get_average_color(image, contour):

    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.drawContours(mask, [contour], -1, 255, thickness=cv2.FILLED)
    masked_image = cv2.bitwise_and(image, image, mask=mask)
    mean_color = cv2.mean(masked_image, mask=mask)[:3]
    return tuple(map(int, mean_color))


def classify_color(RGB_color):
    r, g, b = RGB_color

    if r > 200 and g < 100 and b < 100:
        return "Red"

    elif r > 200 and g > 150 and b < 100:
        return "Orange"

    elif r > 200 and g > 200 and b < 100:
        return "Yellow"

    elif r < 150 and g > 200 and b < 150:
        return "Green"

    elif r < 100 and g > 200 and b > 200:
        return "Cyan"

    elif r < 100 and g < 150 and b > 200:
        return "Blue"

    elif r > 150 and g < 100 and b > 150:
        return "Purple"

    elif r > 100 and g < 100 and b < 100:
        return "Dark Red"

    elif r < 100 and g < 100 and b < 100:
        return "Black"

    elif r > 200 and g > 200 and b > 200:
        return "White"

    elif r > 150 and g > 150 and b > 150:
        return "Light Gray"

    elif r > 100 and g > 100 and b > 100:
        return "Gray"

    elif r > 100 and g > 50 and b < 50:
        return "Brown"

    elif r > 150 and g < 50 and b > 50:
        return "Magenta"

    elif r < 50 and g > 50 and b > 150:
        return "Indigo"
    else:
        return "Unknown"
