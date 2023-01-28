# https://www.codechef.com/problems/ZCO12001
n = int(input())
A = list(map(int, input().split()))

nes_dep_lst = []
first_pos_lst = []
loop_count_lst = []
loop_fir_pos_lst = []
count, dep, f_pos, loop_count, loop_fir_pos = 0, 0, 0, 0, 0

for i in range(n):
    if (A[i] == 1):
        count+=1 #checking well formedness ()(())()(()())(()())
        loop_count+=1              
    else:       
        count-=1       
        loop_count+=1

    if (count>dep):
        dep = count
        f_pos = i

    if (count == 0):
        nes_dep_lst.append(dep) #inserting depth in list
        first_pos_lst.append(f_pos+1)
        dep = 0
        loop_count_lst.append(loop_count)
        loop_fir_pos_lst.append(i-loop_count+2)
        loop_count=0
        
print(max(nes_dep_lst), end=" " )    
print(first_pos_lst[nes_dep_lst.index(max(nes_dep_lst))], end=" ")
print(max(loop_count_lst), end=" ")
print(loop_fir_pos_lst[loop_count_lst.index(max(loop_count_lst))])