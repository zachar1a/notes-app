from tkinter import *
from tkinter import font, filedialog
from tkhtmlview import HTMLText, RenderHTML, HTMLLabel
from markdown2 import Markdown


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.myfont = font.Font(family="Helvetica", size=14)
        self.init_window()

    def init_window(self):
        self.master.title=("TDOWN")
        self.pack(fill=BOTH, expand=True)

        # This is the portion that lets me type
        self.inputeditor = Text(self, width="1", font=self.myfont)
        self.inputeditor.pack(fill=BOTH, expand=True, side=LEFT)
        self.inputeditor.bind("<<Modified>>", self.onInputChange)

        # The box on the right that has all of the markdown that I've typed
        self.outputbox = HTMLLabel(self, width="1", background="#f1f1f1", html="<h1>Welcome</h1>")
        self.outputbox.pack(fill=BOTH, expand=1, side=RIGHT)
        self.outputbox.fit_height()

    def onInputChange(self, event):
        self.inputeditor.edit_modified(0)
        md2html = Markdown()
        self.outputbox.set_html(md2html.convert(self.inputeditor.get("1.0", END)))

    #TODO:
    #An auto complete tool would be nice to have, if I can't
    #have that then at least have an auto-wrapping tool to close tags
    #
    #TODO:
    # have a tool that can help sort the files in the side and that I can
    # click and edit a file whenever I want. I don't want to have to load this
    # up each time i want to change a file


root = Tk()
root.geometry("700x600")
app = Window(root)
app.mainloop()
