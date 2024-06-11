from modules import camera_utils, racial_detection
import threading
import os
from time import sleep
from queue import Queue


def main():
    camera = camera_utils.Camera()
    q = Queue()

    camera_thread = threading.Thread(target=show_camera_window, args=(camera, q))
    camera_thread.start()

    while not os.path.exists("current_image.png"):
        sleep(0.1)

    race_detection_thread = threading.Thread(target=get_race, args=('current_image.png', q))
    race_detection_thread.start()

    camera_thread.join()
    os.remove('current_image.png')


def show_camera_window(camera, queue):
    looping = True
    race = 'Race: '
    while looping:
        if not queue.empty():
            race = queue.get(timeout=1)
            if type(race) is bool:
                looping = race
        else:
            looping = camera.show_camera(race)


def get_race(image, queue):
    race = f'Race: {racial_detection.RacialDetection.detect_race(image)}'
    queue.put(race)
    sleep(5)
    queue.put(False)


if __name__ == '__main__':
    main()
