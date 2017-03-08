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
        response = input("Enter a command, quit to exit").replace('\n', '')
        response = response.strip().split()

        if response[0] == "del":
            if len(response) is not 2:
                print("Error with command del 1")
            elif response[1] in set_:
                list.remove(response[1])
                set_.remove(response[1])
            else:
                print("Error with command del 2")
        elif response[0] == "put":
            args = None

            if len(response) == 2:
                args = response[1].split(",")

            if args is not None and len(args) == 2:
                if args[0] not in set_:

                    size = int(args[1])

                    if fat.freeSpace() >= size:
                        set_.add(args[0])
                        list.add(iNode(args[0], size))
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