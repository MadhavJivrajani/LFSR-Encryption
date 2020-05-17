import lfsr
import numpy as np

rng = lfsr.LFSR(14,"fib",[0,0,0,0,0,0,0,1,0,1,0,1,1,1])
a = rng.generate_output_stream()
a = a.tolist()
a = list(map(str,a))
b = ''.join(a)
lst = {"11": 0, "00":0, "10":0, "01":0,"000":0, "001":0,"010":0, "011":0, "100":0, "101":0, "110":0, "111":0}
ct = []
for i in lst:
    lst[i] = b.count(i)

print(lst)
