from random import shuffle,randint
from time import sleep
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
class Algorithms:
    def __init__(self, array: list[int]):
        self.array = array
        self.copy = array.copy()

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
    def get_snaps(self,algo):
        return list(algo())

