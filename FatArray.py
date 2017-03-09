from threading import Thread
from time import sleep

class FatArray:

    def __init__(self, map):
        # http://stackoverflow.com/questions/6142689/initialising-an-array-of-fixed-size-in-python
        self.fat_array = [0] * 64
        self.map = map
        self.available_blocks = 64

    def getNextFreeIndex(self, start):
        for i in range(start, 64):
            if self.fat_array[i] == 0:
                # print("I: " + str(i))
                return i
        return -1

    def insertNewBlockIndexes(self, size):
        indexes = []
        counter = size
        starting_index = self.getNextFreeIndex(0)
        curr_index = starting_index

        while counter > 0 and self.fat_array[curr_index] != -1:
            next_free_index = self.getNextFreeIndex(curr_index + 1)
            self.fat_array[curr_index] = next_free_index
            self.map.insertNode(curr_index)
            indexes.append(curr_index)
            self.available_blocks -= 1

            if counter == 1 and curr_index != -1:
                self.fat_array[curr_index] = -1

            curr_index = next_free_index
            counter -= 1

        return indexes

    def removeBlocks(self, start):
        curr = start
        next = None

        while self.fat_array[curr] != -1:
            # print("DEBUG =====: " + str(self.fat_array[curr]))
            next = self.getNextBlockIndex(curr)
            # print("DEBUG 100000")
            self.removeBlock(curr)
            # print("DEBUG 234567890")
            self.available_blocks += 1
            # print("DEBUG 109876543")
            curr = next

        self.fat_array[curr] = 0
        self.map.removeNode(curr)
        self.available_blocks += 1

    def removeBlock(self, index):
        self.fat_array[index] = 0
        self.map.removeNode(index)

    def getPointers(self, start):
        pointers = []
        curr = start
        next = -1

        while self.fat_array[curr] != -1:
            next = self.getNextBlockIndex(curr)
            pointers.append(curr)
            curr = next
        pointers.append(curr)
        return pointers

    def getNextBlockIndex(self, index):
        return self.fat_array[index]

    def freeSpace(self):
        return self.available_blocks