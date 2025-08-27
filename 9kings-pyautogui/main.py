from pynput import keyboard, mouse
from collections import namedtuple
import pyautogui
import os
import threading
import time

# types
Point = namedtuple("Point", ["x", "y"])

# global variables
isRunning = False
last_save_time = 0

# global constants
start_delay = 5
restart_game_delay = 600
quitting_game_delay = 15
loading_game_delay = 5
between_commands_delay = 0.2
after_start_delay = 1

# buttons points on 1920x1080
pause_btn = Point(1692, 48)
quit_btn = Point(960, 628)
save_and_quit_btn = Point(963, 677)
start_btn = Point(226, 588)
continue_btn = Point(226, 588)
select_card_on_hand_btn = Point(853, 1019)
discard_card_btn = Point(353, 565)
pick_loot_btn = Point(956, 365)
declare_war_btn = Point(954, 655)
select_left_king_btn = Point(722, 401)
accept_war_btn = Point(958, 740)
select_left_royal_decree_btn = Point(533, 440)
leave_shop_btn = Point(1413, 833)

def on_release_callback(key):
    global isRunning
    if key == keyboard.Key.esc:
        os._exit(0)
    elif key == keyboard.Key.space:
        isRunning = not isRunning 
    try:
        if key.char == 'p':
            x, y = mouse_controller.position
            print(f"Posição do mouse: x={x}, y={y}")
    except AttributeError:
        pass



def is_running_loop():
    global last_save_time
    while True:
        if isRunning:
            now = time.time()
            if now - last_save_time >= restart_game_delay:
                pyautogui.click(x=pause_btn.x, y=pause_btn.y)
                time.sleep(between_commands_delay)
                pyautogui.click(x=quit_btn.x, y=quit_btn.y)
                time.sleep(between_commands_delay)
                pyautogui.click(x=save_and_quit_btn.x, y=save_and_quit_btn.y)
                time.sleep(quitting_game_delay)

                pyautogui.click(x=start_btn.x, y=start_btn.y)
                time.sleep(after_start_delay)
                pyautogui.click(x=continue_btn.x, y=continue_btn.y)
                time.sleep(loading_game_delay)
                last_save_time = now

            pyautogui.click(x=pick_loot_btn.x, y=pick_loot_btn.y)
            time.sleep(between_commands_delay)
            pyautogui.click(x=declare_war_btn.x, y=declare_war_btn.y)
            time.sleep(between_commands_delay)
            pyautogui.click(x=select_left_king_btn.x, y=select_left_king_btn.y)
            time.sleep(between_commands_delay)
            pyautogui.click(x=accept_war_btn.x, y=accept_war_btn.y)
            time.sleep(between_commands_delay)
            pyautogui.click(x=select_left_royal_decree_btn.x, y=select_left_royal_decree_btn.y)
            time.sleep(between_commands_delay)
            pyautogui.click(x=leave_shop_btn.x, y=leave_shop_btn.y)
            time.sleep(between_commands_delay)

            pyautogui.moveTo(select_card_on_hand_btn.x, select_card_on_hand_btn.y)
            time.sleep(between_commands_delay)
            pyautogui.dragTo(discard_card_btn.x, discard_card_btn.y, duration=between_commands_delay, button='left')
        time.sleep(between_commands_delay)

def main():
    global mouse_controller
    mouse_controller = mouse.Controller()

    # Inicia o listener do teclado
    keyboard_listener = keyboard.Listener(on_release=on_release_callback)
    keyboard_listener.start()  # roda em thread separada

    # Inicia a thread do loop das ações
    thread_loop = threading.Thread(target=is_running_loop, daemon=True)
    thread_loop.start()

    # Thread principal fica em um loop infinito, sem bloquear
    while True:
        time.sleep(0.1)  # mantém o programa vivo

if __name__ == "__main__":
    main()
