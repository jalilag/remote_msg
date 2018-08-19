from pynput.mouse import Button,Controller
# from win32api import GetSystemMetrics

# print("Width =", GetSystemMetrics(0))
# print("Height =", GetSystemMetrics(1))
mouse = Controller()
keyboard = Controller()
print('The current pointer position is {0}'.format(mouse.position))
mouse.position = (237,113)
