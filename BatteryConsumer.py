import msvcrt
import time

level = 2  # battery consume level(1-3)
max_level = 3
time_sleep_list = [0.2, 0.02]
dash_list = ['\\', '|', '/', '-']
i = 0
key = ''
print("Keyboard left/right to set battery consuming level(1-3), 'q' to quit.\nMouse left/right to pause/continue.")
print('Level:' + str(level) + '  ', end='')
while key != b'q':
    print('\b', end='')
    print(dash_list[i], flush=True, end='')
    i += 1
    if i > 3:
        i = 0

    # Get keyboard input
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'M':
            level += 1
        if key == b'K':
            level -= 1
        level = max(1, min(level, max_level))
        print('\rLevel:' + str(level) + '  ', end='')

        if key == b'q':
            print('\nquit')
            time.sleep(1)

    # Battery consume method
    a = 0
    for j in range(1000):
        for k in range(1000):
            a += 1

    # Use sleep to adjust cpu usage
    if max_level - level:
        time.sleep(time_sleep_list[level-1])
