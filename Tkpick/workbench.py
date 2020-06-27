import gi

gi.require_version("Gdk", "3.0")

from os import path
import tkinter as tk
from threading import Thread
from gi.repository import Gdk
from pynput import mouse, keyboard


__version__ = "1.2"
__author__ = "Adil Gürbüz"
__contact__ = "adlgrbz@tutamail.com"
__source__ = "https://github.com/adlgrbz/Tkpick"

this_dir, this_filename = path.split(__file__)


class Tool(tk.Tk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)
        self.icon = tk.PhotoImage(
            file=f"{this_dir}/assets/tkpick.gif"
        ).subsample(4, 4)

        self.ww, self.wh = 60, 20
        self.wx, self.wy = 10, 20

        self.sw = self.winfo_screenwidth()
        self.sh = self.winfo_screenheight()

        self.label = tk.Label()
        self.label.config(relief=tk.SUNKEN, border=2)
        self.label.pack(fill=tk.BOTH, expand=1)

    def on_move(self, x, y):
        if x + self.wx + self.ww > self.sw:
            self.geometry(f"{self.ww}x{self.wh}+{x-self.ww}+{y+self.wy}")
        elif y + self.wy + self.wh > self.sh:
            self.geometry(f"{self.ww}x{self.wh}+{x+self.wx}+{y-self.wy}")
        else:
            self.geometry(f"{self.ww}x{self.wh}+{x+self.wx}+{y+self.wy}")

        self.color = self.pixel_at(x, y)
        self.label.config(text=self.color, bg=self.color)

    def listener_mouse(self):
        with mouse.Listener(on_move=self.on_move) as l:
            l.join()

        listener = mouse.Listener(on_move=self.on_move)
        listener.start()

    def listener_keyboard(self):
        with keyboard.GlobalHotKeys(
            {
                "<shift>+c": self.copy,
                "<shift>+a": self.about,
                "<shift>+q": self.quit,
            }
        ) as h:
            h.join()

    def pixel_at(self, x, y):
        # Source:
        # https://stackoverflow.com/a/27406714/12418109

        w = Gdk.get_default_root_window()
        pb = Gdk.pixbuf_get_from_window(w, x, y, 1, 1)
        r, g, b = pb.get_pixels()

        if (r > 127) and (g > 127) and (b > 127):
            self.label.config(fg="#000000")
        else:
            self.label.config(fg="#FFFFFF")

        # RGB to HEX
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    def copy(self):
        self.clipboard_clear()
        self.clipboard_append(self.color)

    def about(self):
        a = tk.Toplevel()

        a.title("About")
        a.resizable(0, 0)
        a.wm_iconphoto(a._w, self.icon)

        tk.Label(
            a, text=f" Tkpick {__version__}", compound=tk.LEFT, image=self.icon
        ).pack(padx=5, pady=5)

        content = (
            f"Author: {__author__}\n"
            f"Contact: {__contact__}\n\n"
            f"Source: {__source__}"
        )
        tk.Label(a, text=content, padx=5, pady=5, relief=tk.RIDGE).pack()

        tk.Button(a, text="Close", command=lambda: a.destroy()).pack(
            padx=5, pady=5, side=tk.RIGHT
        )

    def quit(self):
        self.destroy()
