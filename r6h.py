import cv2
import numpy as np
import pyautogui

def capture_screen():
    img = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR) 
    return img

def process_image(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)

    result = cv2.bitwise_and(image, image, mask=mask)

    return result

def main():
    while True:
        screen_img = capture_screen() 
        processed_img = process_image(screen_img) 

        cv2.imshow('Processed Screen', processed_img) 

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    cv2.destroyAllWindows()  

if __name__ == "__main__":
    main()
