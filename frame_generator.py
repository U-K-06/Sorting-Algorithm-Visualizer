import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from time import sleep
class FrameGenerator:

    def __init__(self,data,frames):
        self.data = data
        self.frames = frames #snap of each state of array
        self.fig,self.ax = plt.subplots()
        self.bars = self.ax.bar(range(len(self.data)),[i*2 for i in self.data])
        self.ax.set_ylim(0,max(self.data or [0])*1.3)
        self.ax.set_xticks(range(len(data)),[*map(str,self.data)])
        self.fig.patch.set_facecolor('#1E1E1E')  

        self.ax.set_facecolor('#121212')  
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['top'].set_color('white') 
        self.ax.spines['left'].set_color('white')
        self.ax.spines['right'].set_color('white')

        self.ax.tick_params(colors='white') 
        self.ax.yaxis.label.set_color('white')
        self.ax.xaxis.label.set_color('white')
        self.ax.title.set_color('white')
        self.current_frame = 0
        self.is_playing = False
        self.fig.canvas.mpl_connect('key_press_event', self.animation_handler)
        self.animation = FuncAnimation(self.fig,self.play,frames=self.frame_generator(),interval=16,repeat=False)
        self.playback_speed = 1
        

    def frame_generator(self):
        while True:
            yield self.current_frame
            if self.is_playing:
                self.current_frame  = (self.current_frame+self.playback_speed)
                if(self.current_frame>len(self.frames)):
                     self.is_playing = False
                

    def animation_handler(self,event):
            key = event.key if hasattr(event,"key") else event
            if key == "right":
                self.current_frame  = min(self.current_frame + self.playback_speed, len(self.frames) - 1)
                print("Animation Paused\nShowing Next State")
            if key == "left":
                self.current_frame  = max(self.current_frame - self.playback_speed, 0)
                print("Animation Paused\nShowing Previous State")
            if key == "p":
                self.is_playing = False
                print("Animation Paused")
            if key == "enter":
                self.is_playing = True
                print("ENTER PRESSED RUNNING ANIMation")

            if key == "escape":
                self.animation.save
                plt.close(self.fig)
                self.fig.canvas.draw_idle()


    def play(self,frame):
        if 0 <= frame < len(self.frames):
                for bar, height in zip(self.bars, self.frames[frame]):
                    bar.set_height(height)
                self.ax.set_xticklabels([str(val) for val in self.frames[frame]])

    def set_playback_speed(self,value):
         print(f'{self.playback_speed=}')
         self.playback_speed = value

    # def update_data(self,new_data,new_frames):
    #     self.data = new_data
    #     self.frames = new_frames
    #     self.current_frame = 0
    #     self.is_playing = False


    #     if len(self.bars) != len(self.data):
    #         self.ax.clear()
    #         self.bars = self.ax.bar(range(len(self.data)), [i*2 for i in self.data])
    #         self.ax.set_ylim(0, max(self.data or [0]) * 1.3)
    #         self.ax.set_xticks(range(len(self.data)))
    #     else:

    #         for bar, height in zip(self.bars, [i*2 for i in self.data]):
    #             bar.set_height(height)

    #     self.ax.set_xticklabels([str(val) for val in self.data])

    #     self.fig.canvas.draw_idle()

if __name__ == "__main__":
    from Algorithms_visuialize import Algorithms
    data = [225, 42, 345, 103, 490, 273, 100, 469, 188, 7, 150, 420, 98, 260, 119, 363, 198, 287, 8, 364]
    a = Algorithms(data)
    snaps = a.get_snaps(a.merge_sort)

    b = FrameGenerator(data,snaps)
