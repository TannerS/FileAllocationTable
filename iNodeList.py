from iNode import  iNode

class iNodeList:

    def __init__(self, fat):
        self.node_list = []
        self.array = fat
        self.count = 0

    def add(self, node):
        print("NODELISTADD: "+ str(node.file_name))


        self.node_list.append(node)

        print("NODELISTADD: "+ str(self.node_list))


        self.allocate(node)
        self.count += 1

    def allocate(self, node):
        pointers = []
        pointers = self.array.insertNewBlockIndexes(node.size)
        node.setIndex(pointers[0])

    def find(self, node):
        print("DEBUG 1!!!!!!!")
        for i in range(0, len(self.node_list)):
            print("NODELISTFIND: " + str(self.node_list[i].file_name))
            print("NODELISTFIND@: " + str(node.file_name))
            print("NODELISTFIND2: " + str(self.node_list[i].size))
            print("NODELISTFIND2@: " + str(node.size))

            print("NODELISTFIND3: " + str(self.node_list[i].index))
            print("NODELISTFIND3@: " + str(node.index))
            print("DEBUG 2")
            if node.file_name == self.node_list[i].file_name:
                print("DEBUG 22%^&*(*&^%&*():::::" + str(i))
                return i
                # if node.size == self.node_list[i].size:
                #     print("DEBUG 222")
                #     if node.index == self.node_list[i].index:
                #         print("DEBUG 2222")
                #         return i
        return -1

    def remove(self, str_):
        print("DEBUG 3")
        index = self.find(iNode(str_, -1))
        print("DEBUG 4")

        node_obj = self.node_list[index]
        print("DEBUG 5")

        starting_index = int(node_obj.index)
        print("DEBUG 6: " + str(starting_index))

        self.array.removeBlocks(starting_index)
        print("DEBUG 7")
        print("INDEX: " + str(index))

        print("!@@@@@@@@@@@@@@@@: " + str(self.node_list))

        # self.node_list.remove(index)
        del self.node_list[index]

        print("DEBUG 8")

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