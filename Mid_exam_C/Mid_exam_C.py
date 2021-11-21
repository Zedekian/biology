import linecache
import time
import random
ans = ""
data = []
score_data = []
count = 0
match = 0
mismatch = 0
gap = 0
score_temp = []
score = []
target = []
temp = ""
start = time.time()
line = open('nucleotides.fasta', 'r')
data_set = line.read()
for i in range(2,len(open('nucleotides.fasta', 'rU').readlines())):   
    data_set = linecache.getline('nucleotides.fasta',i).strip() 
    if data_set.startswith('>',0,1):
        i += 1
        target.append(temp)
        temp = ""
    else:
        data_set = linecache.getline('nucleotides.fasta',i).strip()
        temp += data_set

line.close()

def two_pair_reset(source_1,source_2):
    global ans,match,mismatch,gap,data,short,long,score_data
    data.clear()
    
    if len(source_1) > len(source_2):
        long = source_1
        short = source_2
        data.append(short)
        data.append(long)
    else:
        long = source_2
        short = source_1
        data.append(short)
        data.append(long)
    match = 0
    mismatch = 0
    gap = 0
    count = 0
    ans = ""
    while (count + 1 ) < int(len(data[0])) - 1:
        if data[0][count] == data[1][count]:
            ans += data[0][count]
        else:
            if data[0][count] == data[1][count + 1]:
                data[0] = data[0][:count] + "_" + data[0][count:]
            elif data[0][count + 1] == data[1][count]:
                data[1] = data[1][:count] + "_" + data[1][count:]   
        count += 1
    
    count = 0
    while (count + 1 ) < int(len(data[0])) - 1:
        if ((data[0][count])  == "_")  or  ((data[1][count]) == "_"):
            gap += 1
        elif data[0][count] != data[1][count]:
            mismatch += 1
        elif data[0][count] == data[1][count]:
            match += 1
        count += 1
    score_data.append([match,mismatch,gap])
    return ((match) + (mismatch * -2) + (gap * -3))

j = 0
while j < 10:
    score.append(two_pair_reset(target[random.randint(0,len(target))],target[random.randint(0,len(target))]))
    j += 1

score_temp = sorted(score)
print("Total score : ",score_temp[-1])
print("Match ",score_data[score.index(score_temp[-1])][0])
print("Mismatch : ",score_data[score.index(score_temp[-1])][1])
print("Gap : ",score_data[score.index(score_temp[-1])][2])
end = time.time()
print("Run time : %f(sec)" % (end - start))
