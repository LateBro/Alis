from tkinter import *
from tkinter import filedialog
filedialog
from pygame import mixer

       
class Grip:
    def __init__(self, parent, disable=None, releasecmd=None) :
        super().__init__()    
    
        self.parent = parent
        self.root = parent.winfo_toplevel()

        self.disable = disable
        if type(disable) == 'str':
            self.disable = disable.lower()

        self.releaseCMD = releasecmd

        self.parent.bind('<Button-1>', self.relative_position)
        self.parent.bind('<ButtonRelease-1>', self.drag_unbind)

    def relative_position (self, event) :
        cx, cy = self.parent.winfo_pointerxy()
        geo = self.root.geometry().split('+')
        self.oriX, self.oriY = int(geo[1]), int(geo[2])
        self.relX = cx - self.oriX
        self.relY = cy - self.oriY

        self.parent.bind('<Motion>', self.drag_wid)

    def drag_wid (self, event) :
        cx, cy = self.parent.winfo_pointerxy()
        d = self.disable
        x = cx - self.relX
        y = cy - self.relY
        if d == 'x' :
            x = self.oriX
        elif d == 'y' :
            y = self.oriY
        self.root.geometry('+%i+%i' % (x, y))

    def drag_unbind (self, event) :
        self.parent.unbind('<Motion>')
        if self.releaseCMD != None :
            self.releaseCMD()        


class MainFrame(Frame):
    def __init__(self, parent):
        super(MainFrame, self).__init__(parent)
        

        text = 'Pause'

        Load = Button(self,             relief='flat', text = 'Load',             bg = 'black', fg = 'white',             width = 10, font = ('Comic', 10),             command = self.load)
        Play = Button(self,             relief='flat', text = 'Play',             bg = 'black', fg = 'white',             width = 10,font = ('Comic', 10),             command = self.play)
        Pause = Button(self,             relief='flat', text = text,             bg = 'black', fg = 'white',             width = 10, font = ('Comic', 10),             command = self.pause)
        Stop = Button(self,             relief='flat', text = 'Stop',             bg = 'black', fg = 'white',             width = 10, font = ('Comic', 10),             command = self.stop)
   
        Load.place(x=0, y=20);
        Play.place(x=110, y=20);
        Pause.place(x=220, y=20);
        Stop.place(x=110, y=60);
        
        self.music_file = False
        self.playing_state = False
        
    def load(self):
        self.music_file = filedialog.askopenfilename()
        
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
            
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
            self.text = 'Play'
        else:
            mixer.music.unpause()
            self.playing_state = False
            
    def stop(self):
        mixer.music.stop()


def exit():
    root.destroy()        
        
root = Tk()
root.geometry('330x120')
root.resizable(0, 0)
root.overrideredirect(1)
root.wm_attributes('-topmost', True)
root.wm_attributes('-alpha',0.8)
root['bg'] = 'black'

mainFrame = MainFrame(root)
mainFrame.pack_propagate(0)
mainFrame.pack(fill=BOTH, expand=1)
mainFrame['bg'] = 'black'

bottomFrame = Frame(mainFrame, bg='#050505')
bottomFrame.place(x=0, y=100, anchor='nw', width=330, height=20)

grip = Grip(bottomFrame)

title = Label(
    bottomFrame,     text='Alis',     bg='black',     fg='white'
)
title.place(x=0, y=0)

exit_btn = Button(
    bottomFrame,     text='×',     relief='flat',
    bg='black',     fg='white',     width=1,
    font=('Times', 20),
    command=lambda: exit()
)
exit_btn.place(x=310, y=0, anchor='nw', width=20, height=20)

root.mainloop()