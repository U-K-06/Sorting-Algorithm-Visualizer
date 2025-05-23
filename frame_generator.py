import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class FrameGenerator:
    def __init__(self,data,frames):
        self.data = data
        self.frames = frames #snap of each state of array
        self.fig,self.ax = plt.subplots()
        self.bars = self.ax.bar(range(len(self.data)),[i*2 for i in self.data])
        self.ax.set_ylim(0,max(self.data)*1.3)
        self.ax.set_xticks(range(len(data)),[*map(str,self.data)])
        self.current_frame = 0
        self.is_playing = False
        self.fig.canvas.mpl_connect('key_press_event', self.update)
        self.animation = FuncAnimation(self.fig,self.play,frames=self.frame_generator(),interval=120,repeat=False)

    def frame_generator(self):
        while True:
            yield self.current_frame
            if self.is_playing:
                self.current_frame  = (self.current_frame+1)
                if(self.current_frame>len(self.frames)):
                     self.is_playing = False
                

    def update(self,event):
            if event.key == "right":
                self.current_frame  = min(self.current_frame + 1, len(self.frames) - 1)
                print("Animation Paused\nShowing Next State")
            if event.key == "left":
                self.current_frame  = max(self.current_frame - 1, 0)
                print("Animation Paused\nShowing Previous State")
            if event.key == "p":
                self.is_playing = False
                print("Animation Paused")
            if event.key == "enter":
                self.is_playing = True
                print("ENTER PRESSED RUNNING ANIMation")

            if event.key == "escape":
                self.animation.save
                plt.close(self.fig)
                self.fig.canvas.draw_idle()


    def play(self,frame):
        if 0 <= frame < len(self.frames):
                for bar, height in zip(self.bars, self.frames[frame]):
                    bar.set_height(height)
                self.ax.set_xticklabels([str(val) for val in self.frames[frame]])
    
from Algorithms_visuialize import Algorithms
data = [225, 42, 345, 103, 490, 273, 100, 469, 188, 7, 150, 420, 98, 260, 119, 363, 198, 287, 8, 364]
a = Algorithms(data)
snaps = a.get_snaps(a.merge_sort)

b = FrameGenerator(data,snaps)

plt.show()
