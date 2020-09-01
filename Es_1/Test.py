from timeit import default_timer as timer
import ArrayGen
import InsertionSort
import MergeSort


class Test:

    def __init__(self, Nmax):
        self.Nmax = Nmax

    def InsertionSortRandom(self):
        stop = False
        N = 2
        Navg = 10
        timerList = []
        while stop is not True:
            avgTime = 0
            for i in range(0, Navg):
                A = ArrayGen.RandomArray(N)
                start = timer()
                InsertionSort.InsertionSort(A)
                end = timer()
                avgTime += (end - start)
            timerList.append((avgTime / Navg))
            if N > self.Nmax:
                stop = True
            N += 1
        
        return timerList

    def MergeSortRandom(self):
        stop = False
        N = 2
        Navg = 10
        timerList = []
        while stop is not True:
            avgTime = 0
            for i in range(0, Navg):
                A = ArrayGen.RandomArray(N)
                start = timer()
                MergeSort.MergeSort(A, 0, len(A) - 1)
                end = timer()
                avgTime += (end - start)
            timerList.append((avgTime / Navg))
            if N > self.Nmax:
                stop = True
            N += 1
        return timerList

    def InsertionSortWorst(self):
        stop = False
        N = 2
        Navg = 10
        timerList = []
        while stop is not True:
            avgTime = 0
            for i in range(0, Navg):
                A = ArrayGen.DecreasingArray(N)
                start = timer()
                InsertionSort.InsertionSort(A)
                end = timer()
                avgTime += (end - start)
            timerList.append(avgTime / Navg)
            if N > self.Nmax:
                stop = True
            N += 1
        return timerList

    def MergeSortWorst(self):
        stop = False
        N = 2
        Navg = 10
        timerList = []
        while stop is not True:
            avgTime = 0
            for i in range(0, Navg):
                A = ArrayGen.DecreasingArray(N)
                start = timer()
                MergeSort.MergeSort(A, 0, len(A) - 1)
                end = timer()
                avgTime += (end - start)
            timerList.append((avgTime / Navg))
            if N > self.Nmax:
                stop = True
            N += 1
        return timerList

    def InsertionSortBest(self):
        stop = False
        N = 2
        timerList = []
        while stop is not True:
            A = ArrayGen.SortedArray(N)
            start = timer()
            InsertionSort.InsertionSort(A)
            end = timer()
            timerList.append((end - start))
            if N > self.Nmax:
                stop = True
            N += 1
        return timerList

    def MergeSortBest(self):
        stop = False
        N = 2
        timerList = []
        while stop is not True:
            A = ArrayGen.SortedArray(N)
            start = timer()
            MergeSort.MergeSort(A, 0, len(A) - 1)
            end = timer()
            timerList.append((end - start))
            if N > self.Nmax:
                stop = True
            N += 1
        return timerList
