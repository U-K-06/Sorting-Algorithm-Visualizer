from random import shuffle,randint
from time import sleep
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
class Algorithms:
    def __init__(self, array: list[int], iterations: int, shuffling: bool = True):
        self.array = array
        self.copy = array.copy()
        self.iterations = iterations
        self.shuffling = shuffling
        self.fig, self.ax = plt.subplots()
        self.bars = self.ax.bar(range(len(self.array)),[i*2 for i in self.array],width=0.7,color="DarkGreen")
        self.ax.set_ylim(0, max(self.array) * 1.3)
        self.ax.set_xticks(range(len(self.array)),list(map(str,self.array)))

    def shuffle_array(self):
        if self.shuffling:
            shuffle(self.array)

    def reset_array(self):
        self.array = self.copy.copy()

    def bubble_sort(self):
        swapped = False
        for i in range(len(self.array)):
            swapped = False
            for j in range(0, len(self.array) - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    swapped = True
                    yield self.array.copy()
            if not swapped:
                break
        yield self.array.copy()  # Yield final state
        self.reset_array()
    @staticmethod
    def update(frame,ax,bars,data):
        for bar,height in zip(bars,data[frame]):
            bar.set_height(height)
        ax.set_xticklabels([str(val) for val in data[frame]])

    def selection_sort(self):
        for i in range(0,len(self.array)):
            min_indx = i
            for j in range(min_indx+1,self.array):
                if self.array[j] < self.array[min_indx]:
                    min_indx =  j
            self.array[i],self.array[min_indx] = self.array[min_indx],self.array[i]

    def insertion_sort(self):
        pass
        
    def merge_sort(self):
        pass
    
    def quick_sort(self):
        pass
    def run(self,func):
        snaps = list(func())
        self.animation = FuncAnimation(
            self.fig,
            self.update,
            fargs=(self.ax, self.bars,snaps),
            frames=len(self.array)*self.iterations,  
            interval=300, 
            repeat=False,
        )
        plt.show()
        


a = Algorithms([225, 42, 345, 103, 490, 273, 100, 469, 188, 7, 150, 420, 98, 260, 119, 363, 198, 287, 8, 364],5,True)
a.run(a.bubble_sort)

