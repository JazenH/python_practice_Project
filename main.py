Tlist = [4,55,6,78,12,34,56,677,88]
max_N = Tlist[0]
max_Ind = 0
i=0
for i in range(i+1, len(Tlist)):
    if max_N < Tlist[i]:
        max_N = Tlist[i]
        max_Ind = i
print(f'The max number is Tlist[{max_Ind}] = {max_N}')