def read_file(fpath):
   BLOCK_SIZE = 1024
   with open(fpath) as f:
        block = f.read(BLOCK_SIZE)
        if block:
            print("!!")
            yield block
        else:
            print("!")
            return
def readf(path):
    with open(path) as f:
        line = f.readline()
        while line:
            print(line)
            line = f.readline()
read_file("aab.txt")
#readf("aab.txt")