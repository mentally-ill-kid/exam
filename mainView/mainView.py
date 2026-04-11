from tkinter import *
# from dbhelper.database import Database

class Main_window:
    def init_window():
        root = Tk()
        root.title("exam_test")
        root.geometry("400x600")
        root.resizable(False, False)
        root.configure(bg="#202330")
        root.rowconfigure(0, weight=1)
        root.mainloop()

if __name__ == "__main__": Main_window.init_window()