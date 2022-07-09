from queue import PriorityQueue

class HhufmanNode(object):
    def __init__(self):
        self.data = None
        self.char = None
        self.left = None
        self.right = None
        return
    def __eq__(self, other):
        return self.data == other.data

    def __lt__(self, other):
        return self.data < other.data
    
def printcode(root, s):
    if root.right is None and root.left is None:
        print(root.char + ":" + s)
        return
    printcode(root.left, s + "0")
    printcode(root.right, s + "1")
    
def Huffmancode(root, s):
    global g
    if root.right is None and root.left is None:
        g = {}
        g[root.char] = s
        return
    Huffmancode(root.left, s + "0")
    Huffmancode(root.right, s + "1")
        
def createfile(huffmancode):
    t = open("compressfile.txt", "x")
    
    
file = open("textfile","r")
char_list = list(file.read()) # list characters
main_char = list(dict.fromkeys(char_list)) # list characters bedon tekrar
temp = dict(zip(main_char, (char_list.count(i) for i in main_char)))# conver to dictionary
temp.pop('\n')
q = PriorityQueue()

for key,value in temp.items():
    node = HhufmanNode()
    node.data = value
    node.char = key    
    q.put(node)
        
root = HhufmanNode()
while q.qsize() > 1:
    x = q.get()
    y = q.get()
    f = HhufmanNode()
    f.char = x.char+y.char
    f.data = x.data+y.data
    f.left = x
    f.right = y        
    root = f    
    q.put(f)

Huffmancode(root, "")
print(g)

