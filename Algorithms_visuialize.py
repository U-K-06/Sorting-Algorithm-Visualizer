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
            for j in range(min_indx+1,len(self.array)):
                if self.array[j] < self.array[min_indx]:
                    min_indx =  j
            self.array[i],self.array[min_indx] = self.array[min_indx],self.array[i]
            yield self.array.copy()
        yield self.array.copy()

    def insertion_sort(self):
        for i in range(1,len(self.array)):
            key = self.array[i]
            j = i-1
            while(j>=0 and key < self.array[j]):
                self.array[j+1] = self.array[j]
                j = j-1
                yield self.array.copy()
            self.array[j+1] = key
            yield self.array.copy()
    def merge_sort(self):
        def merge_sort_recursive(arr, left, right):
            if right - left > 1:
                mid = (left + right) // 2
                yield from merge_sort_recursive(arr, left, mid)
                yield from merge_sort_recursive(arr, mid, right)
                yield from merge(arr, left, mid, right)

        def merge(arr, left, mid, right):
            merged = []
            i, j = left, mid
            while i < mid and j < right:
                if arr[i] <= arr[j]:
                    merged.append(arr[i])
                    i += 1
                else:
                    merged.append(arr[j])
                    j += 1
            while i < mid:
                merged.append(arr[i])
                i += 1
            while j < right:
                merged.append(arr[j])
                j += 1
            for k in range(left, right):
                arr[k] = merged[k - left]
                yield arr.copy()

        yield from merge_sort_recursive(self.array, 0, len(self.array))
        yield self.array.copy()
        self.reset_array()

    
    def quick_sort(self):
        pass
    def get_snaps(self,algo):
        return list(algo())

