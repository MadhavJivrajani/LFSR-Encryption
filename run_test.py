import lfsr

rng = lfsr.LFSR(14,"fib",[0,0,0,0,0,0,0,1,0,1,0,1,1,1])
k = rng.generate_output_stream()
k = k.tolist()
lmao = {}
prev_k = k[0]
ct = 0
total = 0
for i in k[1::]:
    if i != prev_k:
        total += 1
        if(ct+1 not in lmao.keys()):
                lmao[ct+1] = 1
        else:
                lmao[ct+1] += 1
        ct = 0
        prev_k = i
    else:
            ct+=1

for i in sorted(list(lmao.keys())):
    print(i, lmao[i])
print(total)
