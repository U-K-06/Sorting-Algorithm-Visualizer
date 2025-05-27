import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from frame_generator import FrameGenerator
from Algorithms_visuialize import Algorithms
from time import sleep
from Algorithms_visuialize import Algorithms
import random
data = [225, 42, 345, 103, 490, 273, 100, 469, 188, 7, 150, 420, 98, 260, 119, 363, 198, 287, 8, 364]
# data.extend([random.randint(min(data), max(data)) for _ in range(40)])
a = Algorithms(data)
snaps = a.get_snaps(a.merge_sort)


class App(tk.Tk,FrameGenerator):
    def __init__(self):
        tk.Tk.__init__(self)
        FrameGenerator.__init__(self,data,snaps)
        self.title("Sorting Algorithm Visualiser")
        self.state('zoomed')
        canvas = FigureCanvasTkAgg(self.fig, master=self)
        canvas.draw()
        canvas_widgets = canvas.get_tk_widget().pack(fill='both')
        canvas.get_tk_widget().config(height=1300)
        scale = tk.Scale(self, from_=1, to=5, resolution=1, orient='horizontal', label='Speed',
                 command=self.on_scale,
                 length=300,      
                 width=30,       
                 sliderlength=40, 
                 font=("Helvetica", 14),bg='#2E2E2E', fg='white', troughcolor='#555555')  
        scale.set(1.0) 
        scale.pack()
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Undo", command=lambda:self.animation_handler("left"),font=("Helvetica", 14), width=12, height=2,bg="#4CAF50").pack(side='left', padx=5)
        tk.Button(btn_frame, text="Next", command=lambda:self.animation_handler("right"),font=("Helvetica", 14), width=12, height=2,bg="#4CAF50").pack(side='left', padx=5)
        tk.Button(btn_frame, text="Pause", command=lambda:self.animation_handler("p"),font=("Helvetica", 14), width=12, height=2,bg="#4CAF50").pack(side='left', padx=5)
        tk.Button(btn_frame, text="Resume", command=lambda:self.animation_handler("enter"),font=("Helvetica", 14), width=12, height=2,bg="#4CAF50").pack(side='left', padx=5)
        self.config(bg="#2E2E2E")
    def on_scale(self,val):
        speed = int(val)
        print(f"Playback speed set to {speed}")
        self.set_playback_speed(speed) # Assuming your FrameGenerator instance



a = App()
a.mainloop()
