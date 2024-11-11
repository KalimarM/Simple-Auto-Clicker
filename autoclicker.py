import keyboard
import mouse
import time


clicks_per_second = 200

def main():
    
    print('hold ~ to autoclick.')
    while True:
        if keyboard.is_pressed('`'):
            mouse.click()
            print('click')
            time.sleep(1/clicks_per_second)
        else:
            time.sleep(1/60)


if __name__ == "__main__":
    main()
