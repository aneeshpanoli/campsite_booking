import pyautogui as pag
import time, sys, os
import mss
import mss.tools
from pygame import mixer

class Make_reservation:
    '''Automatically checks the rec gov reservation availablity
        Set up your screen resolution
    '''
    def __init__(self):
        self.scr_width = 1440
        self.scr_height = 900
        mixer.init()

    def take_screenshot(self, scName, monitor_number):
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
    # series_shot()

    run = Make_reservation()
    scName = '/media/aneesh/io_python_usb/recreation.gov/reserve/scrot.png'
    run.get_btn_pos(scName, 2)
    # run.play_alarm()
