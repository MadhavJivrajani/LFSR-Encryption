from PIL import Image
from lfsr import LFSR
from functools import reduce
from feedback import feedback_poly, one_hot_encode


lfsr = LFSR(15, 'fib', [1 for _ in range(15)])
s = ""
ints =  lfsr.get_ints()
value  = 0
im = Image.open(r"output.png")
px = im.load()
width, height = im.size
print("Height :", height, " And width : ", width)
for i in range(width):
    for j in range(height):
        r, g, b = px[i, j]
        r = (r) ^ ints[value]
        value = (value+1) % (len(ints))
        g = (g) ^ ints[value]
        value = (value+1)%(len(ints))
        b = (b) ^ ints[value]
        value = (value+1) % (len(ints))
        px[i, j] = (r, g, b)
        
im.show()
im.save("output.png")
