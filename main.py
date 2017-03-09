from BitMap import BitMap
from FatArray import FatArray
from iNodeList import iNodeList
from iNode import iNode

def main():
    map = BitMap()
    fat = FatArray(map)
    list = iNodeList(fat)
    # set_ = dict()
    set_ = set()
    # set_ = {}
    quit = False

    while not quit:
        response = input("Enter a command (\"put <name> <size>\", \"inodes\", \"del <name>\", \"bitmap\", and \"quit\"): ").replace('\n', '')
        response = response.strip().split()

        if len(response) >= 1:
            if response[0] == "del":
                if len(response) is not 2:
                    print("Error with command del 1")
                elif response[1] in set_:
                    list.remove(response[1])
                    set_.remove(response[1])
                else:
                    print("Error with command del 2")
            elif response[0] == "put":
                if len(response) == 3:

                        size = int(response[2])
                        if fat.freeSpace() >= size:
                            set_.add(response[1])
                            list.add(iNode(response[1], int(size)))
                        else:
                            print("Error with command put 2")
                else:
                    print("Error with command put 1")
            elif response[0] == "bitmap":
                print(map)
            elif response[0] == "inodes":
                print(list.toString())
            elif response[0] == "quit":
                quit = True
            else:
                print("Command not supported")

if __name__ == "__main__":
    main()