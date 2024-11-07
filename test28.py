import tkinter as tk
from settings import *
from typing import Tuple
import sys
import os


class Clicker(tk.Tk):
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title(TITLE)
        self.root.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
        base_path = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.abspath('.')
        self.bg_image = tk.PhotoImage(file=os.path.join(base_path, 'source', 'bg.png'))

    def display_bg(self) -> None:
        bg_label = tk.Label(self.root, image=self.bg_image)
        bg_label.pack()

    def clear_screen(self) -> None:
        for widget in self.root.winfo_children():
            widget.destroy()

    def play(self) -> None:
        self.clear_screen()
        label = tk.Label(self.root, text='Сорян <3\nИгра всё ещё в разработке',
                         font=('Arial', 20, 'bold'), bg='black', fg='white')
        label.pack()
    
    def display_title(self) -> None:
        title_label = tk.Label(self.root, text=TITLE, font=('Arial', 40, 'bold'),
                            bg='black', fg='white')
        title_label.place(x=SCREEN_WIDTH // 2 - title_label.winfo_width(), y=200)
        self.root.update_idletasks()
        title_width = title_label.winfo_width()
        title_label.place(x=SCREEN_WIDTH // 2 - title_width // 2, y=200)

    def display_menu(self) -> None:
        self.display_title()
        BUTTON_WIDHT: int = 300
        BUTTON_HEIGHT: int = 100
        BUTTON_FONT: Tuple[str, int, str] = ('Arial', 20, 'bold')
        OFFSET: int = 150
        play_button = tk.Button(self.root, text='Играть', bg='black',
                                fg='white', font=BUTTON_FONT,
                                command=self.play)
        play_button.place(x=(SCREEN_WIDTH - BUTTON_WIDHT) // 2,
                          y=(SCREEN_HEIGHT - BUTTON_HEIGHT) // 2,
                          width=BUTTON_WIDHT, height=BUTTON_HEIGHT)
        quit_button = tk.Button(self.root, text='Выйти', bg='black',
                                fg='white', font=BUTTON_FONT,
                                command=self.root.quit)
        quit_button.place(x=(SCREEN_WIDTH - BUTTON_WIDHT) // 2,
                          y=(SCREEN_HEIGHT - BUTTON_HEIGHT) // 2 + OFFSET,
                          width=BUTTON_WIDHT, height=BUTTON_HEIGHT)

    def start(self) -> None:
        self.display_bg()
        self.display_menu()
        self.root.mainloop()
        

def main() -> None:
    clicker = Clicker()
    clicker.start()


if __name__ == '__main__':
    main()
