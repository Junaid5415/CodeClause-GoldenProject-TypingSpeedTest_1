import time
from tkinter import *
import random
from threading import *
import webbrowser
from PIL import Image, ImageTk


class WPM:

    def __init__(self):
        self.root = Tk()

        self.counter = 0
        self.running = False

        self.root.title('Typing Speed Test')
        self.root.geometry('1000x500')
        self.root.minsize(width=1000, height=500)
        self.root.maxsize(width=1000, height=500)
        self.root.wm_iconbitmap('key.ico')
        self.frame = Frame(self.root, width=1000, height=500)
        self.frame.place(x=0, y=0)
        self.root.bind('<Escape>', self.quit)

        self.image0 = Image.open('link.png')
        self.image1 = self.image0.resize((35, 35))
        self.test = ImageTk.PhotoImage(self.image1)

        self.img1 = Label(image=self.test)
        self.img1.place(x=820, y=40)

        self.lprof = Label(self.frame, text='⭣ LinkedIn Profile ⭣', fg='black', font=('Terminal', 11, 'bold'))
        self.lprof.place(x=800, y=20)

        self.Linked = Label(self.frame, text="LinkedIn", fg="#0a66c2", cursor="hand2", font=('Terminal', 15, 'bold'))
        self.Linked.place(x=860, y=50)
        self.Linked.bind("<Button-1>", lambda _: self.Callback(0))

        self.image2 = Image.open('Git.png')
        self.image01 = self.image2.resize((35, 35))
        self.test2 = ImageTk.PhotoImage(self.image01)

        self.img2 = Label(image=self.test2)
        self.img2.place(x=10, y=40)

        self.lprof = Label(self.frame, text='⭣ GitHub Profile ⭣', fg='black', font=('Terminal', 11, 'bold'))
        self.lprof.place(x=20, y=20)

        self.git = Label(self.root, text='GitHub', bg='Black', fg='white', cursor='hand2',
                         font=('Terminal', 15, 'bold'))
        self.git.place(x=60, y=50)
        self.git.bind('<Button-1>', lambda _: self.Callback(1))

        self.texts = open('sample.txt', 'r').read().split('\n')

        self.welcome = Label(text="Welcome To My Typing Speed Test", font=('Terminal', 15, 'bold'))
        self.welcome.place(x=500, y=50, anchor='center')

        self.smpl = Label(self.frame, text=random.choice(self.texts), font=('Terminal', 15))
        self.smpl.place(x=500, y=120, anchor='center')

        self.entry = Entry(self.frame, width=70, font=('Terminal', 15, 'bold'))
        self.entry.place(x=500, y=200, anchor='center')
        self.entry.bind('<KeyRelease>', self.start)

        self.spd = Label(self.frame, text='Speed\n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPM',
                         font=('Terminal', 15))
        self.spd.place(x=500, y=300, anchor='center')

        self.reset = Button(self.frame, height=2, width=10, font=('Terminal', 15, 'bold'), text='Reset',
                            command=self.reset)
        self.reset.place(x=500, y=450, anchor='center')

        self.root.mainloop()

    @staticmethod
    def Callback(n):
        if n == 0:
            webbrowser.open('www.linkedin.com/in/junaid-ahmed-a10302273')
        elif n == 1:
            webbrowser.open('https://github.com/Junaid5415')

    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18]:
                self.running = True
                t = Thread(target=self.time_Thread)
                t.start()
        if not self.smpl.cget('text').startswith(self.entry.get()):
            self.entry.config(fg='red')
        else:
            self.entry.config(fg='black')
        if self.entry.get() == self.smpl.cget('text'):
            self.running = False
            self.entry.config(fg='green')

    def time_Thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.entry.get()) / self.counter
            cpm = cps * 60
            wps = len(self.entry.get().split(' ')) / self.counter
            wpm = wps * 60
            self.spd.config(text=f'Speed\n{cps:.2f} CPS\n{cpm:.2f} CPM\n{wps:.2f} WPS\n{wpm:.2f} WPM')

    def reset(self):
        self.running = False
        self.counter = 0
        self.spd.config(text='Speed\n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPM')
        self.smpl.config(text=random.choice(self.texts))
        self.entry.delete(0, END)

    def quit(self, event):
        self.root.quit()


WPM()
