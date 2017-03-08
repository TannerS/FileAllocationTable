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
        return self.node_list.index(node)

    def remove(self, str):
        node = self.find(iNode(str, -1))
        node_obj = self.node_list[node]
        starting_index = node_obj.index
        self.array.removeBlocks(starting_index)
        self.node_list.remove(node)
        self.count -= 1

    def toString(self):
        if self.count == 0:
            return "No i-nodes currently allocated"

        str = ""

        for i in range(0, len(self.node_list)):
            node = self.node_list[0]
            pointers = self.array.getPointers(node.index)
            str += node.toString(pointers) + "\n"

        return str