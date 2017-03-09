class BitMap:

    def __init__(self):
        self.bitmap = 0

    def insertNode(self, index):
        bit = 1

        for i in range(0, index):
            bit = bit << 1
        self.bitmap = self.bitmap | bit

    def removeNode(self, index):
        bit = 1

        for i in range(0, index):
            bit = bit << 1
        self.bitmap = self.bitmap ^ bit

    def __repr__(self):
        temp_bitmap = self.bitmap
        bits = 0
        binary_str = ""
        bin_str = ""
        final_str = ""

        for i in range(0, 8):
            bits = temp_bitmap & 0xFF
            temp_bitmap >>= 8
            # http://stackoverflow.com/questions/1395356/how-can-i-make-bin30-return-00011110-instead-of-0b11110
            binary_str = bin(bits)[2:].zfill(8)
            bin_str = binary_str

            # print("DEBUG: " +  bin_str)

            # if(temp_bitmap != 8):
                # convert to list to add front 0's
                #temp_bitmap_list = list( bin(temp_bitmap)[2:])
                # temp_bitmap_list = list( bin(temp_bitmap))

                # print(temp_bitmap)

                # http://stackoverflow.com/questions/869885/loop-backwards-using-indices-in-python
                # for i in range(8,-1,-1):
                #     temp_bitmap_list.insert(0, "0")
                    # print(temp_bitmap, end="")

                # bin_str.join(temp_bitmap_list)
                # bin_str.join("\n")

                # print(bin_str)

            # reviser stirng here???
            final_str += str((i) * 8)
            final_str += "  "
            final_str += bin_str[::-1]
            final_str += "\n"

           # print(final_str)

        return final_str
