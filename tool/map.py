from .calculated import *
import cv2 as cv
import pyautogui
import time


class map:
    def __init__(self):
        self.calculated = calculated()
        self.win32api = win32api
        self.win32con = win32con

    def map_init(self):

        # 进行地图初始化，把地图缩小,需要缩小5次

        target = cv.imread('./temp/contraction.jpg')
        while True:
            result = self.calculated.scan_screenshot(target)
            if result['max_val'] > 0.98:
                points = self.calculated.calculated(result, target.shape)
                print(points)
                pyautogui.click(points, clicks=5, interval=0.1)
                break

    def auto_map_1_1(self):

        # 选择地图
        pyautogui.keyDown("m")
        pyautogui.keyUp("m")
        time.sleep(1)
        self.map_init()

        map_click = [
            (951, 1263),
            (1964, 414),
            (667, 936),
            (1877, 702),
            (1163, 634),
            (1979, 1248)
        ]
        for points in map_click:
            self.calculated.Click(points)
            time.sleep(1.5)

        self.calculated.click_target(
            'temp\\transfer.jpg', 0.98)
        
        # 选择完地图，开始寻路
        print("选择完地图，开始寻路")
        time.sleep(5)
        self.calculated.auto_map("map_1-1")

    def auto_map_1_2(self):
        # 选择地图
        pyautogui.keyDown("m")
        pyautogui.keyUp("m")
        time.sleep(1)
        self.map_init()

        self.calculated.click_target(
            'temp\\orientation_1.jpg', 0.98)

        time.sleep(1)
        self.calculated.click_target(
            'temp\\orientation_2.jpg', 0.98)

        self.calculated.click_target(
            'temp\\map_1-2.jpg', 0.98)

        self.calculated.click_target(
            'temp\\map_1-2_point_1.jpg', 0.98)

        self.calculated.click_target(
            'temp\\transfer.jpg', 0.98)

        # 开始寻路

        time.sleep(5)
        self.calculated.auto_map("map_1-2_1")

        # 继续寻路
        pyautogui.keyDown("m")
        pyautogui.keyUp("m")
        time.sleep(1)

        self.calculated.click_target(
            'temp\\map_1-2_point_2.jpg', 0.98)

        self.calculated.click_target(
            'temp\\transfer.jpg', 0.98)

        time.sleep(5)
        self.calculated.auto_map("map_1-2_2")

        # 继续寻路
        pyautogui.keyDown("m")
        pyautogui.keyUp("m")
        time.sleep(1)

        self.calculated.click_target(
            'temp\\map_1-2_point_3.jpg', 0.98)

        self.calculated.click_target(
            'temp\\map_1-2_point_4.jpg', 0.98)

        self.calculated.click_target(
            'temp\\transfer.jpg', 0.98)

        time.sleep(5)
        self.calculated.auto_map("map_1-2_3")

        # 继续寻路
        pyautogui.keyDown("m")
        pyautogui.keyUp("m")
        time.sleep(1)

        self.calculated.click_target(
            'temp\\map_1-2_point_3.jpg', 0.98)

        self.calculated.click_target(
            'temp\\map_1-2_point_4.jpg', 0.98)

        self.calculated.click_target(
            'temp\\transfer.jpg', 0.98)

        time.sleep(5)
        self.calculated.auto_map("map_1-2_4")

        print("完成收容舱段清怪")

    def auto_map_1_3(self):
        # 选择地图
        pyautogui.keyDown("m")
        pyautogui.keyUp("m")
        time.sleep(1)
        self.map_init()

        self.calculated.click_target(
            'temp\\orientation_1.jpg', 0.98)
        time.sleep(1)
        self.calculated.click_target(
            'temp\\orientation_2.jpg', 0.98)

        self.calculated.click_target(
            'temp\\map_1-3.jpg', 0.98)

        self.calculated.click_target(
            'temp\\map_1-3_point_1.jpg', 0.98)

        self.calculated.click_target(
            'temp\\map_1-3_point_2.jpg', 0.98)

        self.calculated.click_target(
            'temp\\transfer.jpg', 0.98)

        # 开始寻路
        time.sleep(5)
        self.calculated.auto_map("map_1-3_1")

        # 继续寻路
        print("继续寻路")
        pyautogui.keyDown("m")
        pyautogui.keyUp("m")

        self.calculated.click_target(
            'temp\\map_1-3_point_3.jpg', 0.98)

        self.calculated.click_target(
            'temp\\transfer.jpg', 0.98)

        time.sleep(5)
        self.calculated.auto_map("map_1-3_2")

        # 继续寻路
        time.sleep(1)  # 等待传送
        self.calculated.auto_map("map_1-3_3")

        # 继续寻路
        pyautogui.keyDown("m")
        pyautogui.keyUp("m")

        self.calculated.click_target(
            'temp\\map_1-3_point_4.jpg', 0.98)

        self.calculated.click_target(
            'temp\\transfer.jpg', 0.98)

        time.sleep(5)
        self.calculated.auto_map("map_1-3_4")

    def auto_map_2_1(self):
        # 选择地图
        pyautogui.keyDown("m")
        pyautogui.keyUp("m")
        time.sleep(1)
        self.map_init()

        self.calculated.click_target(
            'temp\\orientation_1.jpg', 0.98)

        time.sleep(1)
        self.calculated.click_target(
            'temp\\orientation_3.jpg', 0.85)

        self.calculated.click_target(
            'temp\\map_2-1.jpg', 0.98)

        self.calculated.click_target(
            'temp\\map_2-1_point_1.jpg', 0.98)

        self.calculated.click_target(
            'temp\\transfer.jpg', 0.98)

        # 开始寻路
        time.sleep(5)
        print("开始寻路")
        self.calculated.auto_map("map_2-1_1")

        # 继续寻路
        print("继续寻路")
        pyautogui.keyDown("m")
        pyautogui.keyUp("m")

        self.calculated.click_target(
            'temp\\map_2-1_point_2.jpg', 0.98)

        self.calculated.click_target(
            'temp\\transfer.jpg', 0.98)

        # 开始寻路
        time.sleep(5)
        print("开始寻路")
        self.calculated.auto_map("map_2-1_2")

    def auto_map_2_2(self):
        # 选择地图
        pyautogui.keyDown("m")
        pyautogui.keyUp("m")
        time.sleep(1)
        self.map_init()

        self.calculated.click_target(
            'temp\\orientation_1.jpg', 0.98)

        time.sleep(1)
        self.calculated.click_target(
            'temp\\orientation_3.jpg', 0.85)

        self.calculated.click_target(
            'temp\\map_2-2.jpg', 0.98)

        self.calculated.click_target(
            'temp\\map_2-2_point_1.jpg', 0.98)

        self.calculated.click_target(
            'temp\\transfer.jpg', 0.98)

        # 开始寻路
        time.sleep(5)
        print("开始寻路")
        self.calculated.auto_map("map_2-2_1")

        pyautogui.keyDown("m")
        pyautogui.keyUp("m")
        time.sleep(1)
        self.calculated.click_target(
            'temp\\map_2-2_point_1.jpg', 0.98)

        self.calculated.click_target(
            'temp\\transfer.jpg', 0.98)

        # 开始寻路
        time.sleep(3)
        print("开始寻路")
        self.calculated.auto_map("map_2-2_2")

        pyautogui.keyDown("m")
        pyautogui.keyUp("m")
        time.sleep(1)
        self.calculated.click_target(
            'temp\\map_2-2_point_2.jpg', 0.98)

        self.calculated.click_target(
            'temp\\transfer.jpg', 0.98)

        # 开始寻路
        time.sleep(3)
        self.calculated.auto_map("map_2-2_3")

    def auto_map_2_3(self):
        # 选择地图
        pyautogui.keyDown("m")
        pyautogui.keyUp("m")
        time.sleep(1)
        self.map_init()

        self.calculated.click_target(
            'temp\\orientation_1.jpg', 0.98)

        time.sleep(1)
        self.calculated.click_target(
            'temp\\orientation_3.jpg', 0.85)

        self.calculated.click_target(
            'temp\\map_2-3.jpg', 0.98)

        self.calculated.click_target(
            'temp\\map_2-3_point_1.jpg', 0.98)

        self.calculated.click_target(
            'temp\\transfer.jpg', 0.98)

        # 开始寻路
        time.sleep(5)
        print("开始寻路")
        self.calculated.auto_map("map_2-3_1")

        pyautogui.keyDown("m")
        pyautogui.keyUp("m")
        time.sleep(1)
        self.calculated.click_target(
            'temp\\map_2-3_point_2.jpg', 0.98)

        self.calculated.click_target(
            'temp\\map_2-3_point_3.jpg', 0.98)

        self.calculated.click_target(
            'temp\\transfer.jpg', 0.98)

        # 开始寻路
        time.sleep(5)
        print("开始寻路")
        self.calculated.auto_map("map_2-3_2")

        pyautogui.keyDown("m")
        pyautogui.keyUp("m")
        time.sleep(1)
        self.calculated.click_target(
            'temp\\map_2-3_point_2.jpg', 0.98)

        self.calculated.click_target(
            'temp\\map_2-3_point_3.jpg', 0.98)

        self.calculated.click_target(
            'temp\\transfer.jpg', 0.98)

        # 开始寻路
        time.sleep(3)
        print("开始寻路")
        self.calculated.auto_map("map_2-3_3")

        pyautogui.keyDown("m")
        pyautogui.keyUp("m")
        time.sleep(1)

        self.calculated.click_target(
            'temp\\map_2-3_point_4.jpg', 0.98)

        self.calculated.click_target(
            'temp\\transfer.jpg', 0.98)

        # 开始寻路
        time.sleep(3)
        print("开始寻路")
        self.calculated.auto_map("map_2-3_4")

        pyautogui.keyDown("m")
        pyautogui.keyUp("m")
        time.sleep(1)

        self.calculated.click_target(
            'temp\\map_2-3_point_5.jpg', 0.98)

        self.calculated.click_target(
            'temp\\transfer.jpg', 0.98)

        # 开始寻路
        time.sleep(3)
        print("开始寻路")
        self.calculated.auto_map("map_2-3_5")
