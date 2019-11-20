import pyautogui as pag
import time, sys, os
import mss
import mss.tools
from pygame import mixer

class Make_reservation:
    '''Automatically checks the rec gov reservation availablity
    '''
    def __init__(self):
        self.scr_width = 1440
        self.scr_height = 900
        mixer.init()

    def take_screenshot(self, scName, monitor_number=1):
        '''
        Takes screenshots at specified intervals
        scName: name with path to save the screenshot
        monitor_numer: if you have multiple monitors, 
        specify the number
        '''
        with mss.mss() as sct:
            mon = sct.monitors[monitor_number]
            monitor = {
                "top": mon["top"] + 0,  # 100px from the top
                "left": mon["left"] + 0,  # 100px from the left
                "width": self.scr_width,
                "height": self.scr_height,
                "mon": monitor_number,
            }
            output = scName
            sct_img = sct.grab(monitor)
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

    def get_btn_pos(self, scName, monitor_number):
        '''
        Script to automatically click the reservation button
        '''
        while True:
            time.sleep(2)
            self.take_screenshot(scName, monitor_number)
            try:
                btn = pag.locate('reserve_btn.png',scName)
                btn_pos = pag.center(btn)
                pag.click(btn_pos)
                self.play_alarm()
                print("Reservation Available")
                break
            except:
                print("Reservation unavailable")
                continue

    def play_alarm(self):
        mixer.music.load('alarm.mp3')
        mixer.music.play(loops = -1)
        while mixer.music.get_busy() == True:
            continue

if __name__ == "__main__":
    monitor_number = 1
    scName = 'path/to/screenhot/folder'
    run = Make_reservation()
    #CAUTION: repeasted readwrite can reduce the life of ...
    #your hard drive
    # I used a sapare flash drive
    run.get_btn_pos(scName, 1)
