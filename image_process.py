import cv2

def change_color(image, color):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = img_gray.shape[:2]
    color_list = {"b": [1, 0, 0], "g": [0, 1, 0], "r": [0, 0, 1]}[color]
    for x in range(height):
        for y in range(width):
            intensity = img_gray[x, y]
            image[x, y] = [c * intensity for c in color_list]
            
    return image