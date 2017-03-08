
class iNode:

    def __init__(self, name, size):
        self.file_name = name
        self.size = size
        self.index = -1

    def setIndex(self, index):
        self.index = index

    def isEqual(self, object):
        if self.file_name == object.fileName:
            return True
        return False

    def hashCode(self):
        return(hash(self.file_name))

    def toString(self, pointers):
        str = ""
        str += self.file_name + ": " + pointers[0]

        for i in range(1, len(pointers)):
            str += " -> " + pointers[i]

        return str