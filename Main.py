from ultralytics import YOLO
import pyautogui
import webbrowser
import time
import keyboard
import cv2

# initialized YOLO model
class GameBot:
    def __init__(self):
        self.model = YOLO('best.pt')
        self.death = 0

    def open_game(self) -> None:
        url = 'https://poki.com/en/g/subway-surfers'
        webbrowser.open(url)

    def fullscreen(self) -> None:
        # Fullscreen button is located at 1260x710 px with 1920x1080   
        x, y = 1260, 710
        pyautogui.moveTo(x, y)
        time.sleep(2)
        pyautogui.click()
        time.sleep(2)

    def start(self) -> None:
        x, y = 1070, 900
        pyautogui.moveTo(x, y)
        time.sleep(2)
        pyautogui.click()

    def take_screenshot(self) -> None:
        screenshot = pyautogui.screenshot()
        screenshot.save(r'running\current.png')

    def image_recognition(self) -> None:
        results = self.model.predict(r'running\current.png')
        boxes = results[0].boxes.xyxy.tolist()
        classes = results[0].boxes.cls.tolist()
        names = results[0].names
        confidences = results[0].boxes.conf.tolist()

        #play button
        template = cv2.imread(r'jpgs\play button.png', cv2.IMREAD_GRAYSCALE)
        screenshot = cv2.imread(r'running\current.png', cv2.IMREAD_GRAYSCALE)
        
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # conf = 0.75
        if max_val >= 0.75:
            self.start()
            self.death += 1

    def run(self):
        self.open_game()
        self.fullscreen()
        self.start()

        while True:
            self.take_screenshot()
            self.image_recognition()

            if keyboard.is_pressed('q'):
                print('Exiting script')
                print(self.death)
                break

if __name__ == '__main__':
    bot = GameBot()
    bot.run()