from tkinter import *

import settings
import utils

root = Tk()

# Override the settings of the Window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

# Set up frames - top frames
top_frame = Frame(
    root,
    bg=settings.BG_COLOR,
    width=utils.width_percent(100),
    height=utils.height_percent(25)
)
top_frame.place(
    x=0,
    y=0
)

# Left frame
left_frame = Frame(
    root,
    bg=settings.BG_COLOR,
    width=utils.width_percent(25),
    height=utils.height_percent(75)
)
left_frame.place(
    x=0,
    y=utils.height_percent(25)
)

# Center frame
center_frame = Frame(
    root,
    bg=settings.BG_COLOR,
    width=utils.width_percent(75),
    height=utils.height_percent(75)
)
center_frame.place(
    x=utils.width_percent(25),
    y=utils.height_percent(25)
)

btn1 = Button(
    center_frame,
    bg='grey',
    text='First Button'
)
btn1.place(x=5, y=5)

# Run the window
root.mainloop()

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
