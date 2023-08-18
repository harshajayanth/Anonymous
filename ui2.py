import tkinter as tk
from PIL import ImageTk, Image


root=tk.Tk()
root.title('Anonymous')
root.geometry("300x200+10+20")

class AnimatedGIF(tk.Label):
    def __init__(self, master=None, filename=None):
        super().__init__(master)
        self.filename = filename
        self.load()

    def load(self):
        self.gif = Image.open(self.filename)
        self.frames = []
        try:
            while True:
                self.frames.append(ImageTk.PhotoImage(self.gif.copy()))
                self.gif.seek(len(self.frames))
        except EOFError:
            pass

        self.index = 0
        self.delay = self.gif.info.get("duration", 50)
        self.show_frame()

    def show_frame(self):
        self.configure(image=self.frames[self.index])
        self.index += 1
        if self.index == len(self.frames):
            self.index = 0
        self.after(self.delay,self.show_frame)

gif = AnimatedGIF(root, "load.gif")
gif.pack()

root.resizable(False, False)


