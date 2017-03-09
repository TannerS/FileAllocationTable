from iNode import  iNode

class iNodeList:

    def __init__(self, fat):
        self.node_list = []
        self.array = fat
        self.count = 0

    def add(self, node):
        self.node_list.append(node)
        self.allocate(node)
        self.count += 1

    def allocate(self, node):
        pointers = []
        pointers = self.array.insertNewBlockIndexes(node.size)
        node.setIndex(pointers[0])

    def find(self, node):
        for i in range(0, len(self.node_list)):
            if node.file_name == self.node_list[i].file_name:
                return i
        return -1

    def remove(self, str_):
        index = self.find(iNode(str_, -1))
        node_obj = self.node_list[index]
        starting_index = int(node_obj.index)
        self.array.removeBlocks(starting_index)
        # self.node_list.remove(index)
        del self.node_list[index]
        self.count -= 1

    def toString(self):
        if self.count == 0:
            return "No i-nodes currently allocated"
        str = ""

        for i in range(0, len(self.node_list)):
            node = self.node_list[i]
            pointers = self.array.getPointers(node.index)
            str += node.toString(pointers) + "\n"
        return str