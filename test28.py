import tkinter as tk

class Clicker(tk.Tk):
    def click(self) -> None:
        self.button.destroy()
        label = tk.Label(self.root, text="Сорян <3\nИгра всё ещё в разработке", font=("Arial", 24))
        label.pack()

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Clicker")
        self.root.geometry("1024x720")

        self.button = tk.Button(self.root, text="Если вы хотите поиграть в кликер, то нажмите сюда", command=self.click)
        self.button.place(x=0, y=0, width=1024, height=720)


    def start(self) -> None:
        self.root.mainloop()
        

def main() -> None:
    clicker = Clicker()
    clicker.start()


if __name__ == '__main__':
    main()
