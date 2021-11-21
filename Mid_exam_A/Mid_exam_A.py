import linecache
import time
class db:
    not_use = 0
    ans = ""

def two_pair(x):
    count = 3
    if db.ans[0:count] == x[-count:]:   
        while count < 20:
            if db.ans[0:count] == x[-count:]:
                count += 1
            else:
                db.ans = x[0:-count] + db.ans
                break
        
    elif db.ans[-count:] == x[0:count]: 
        while count < 20:
            if db.ans[-count:] == x[0:count]:
                count += 1
            else: 
                db.ans += x[count:]
                break
        
    else:
        db.not_use += 1

def find_taget(y ,z):
    k = 3
    if y[0:k] == z[-k:]:
        while k < 20:
            if y[0:k] == z[-k:]:
                k += 1
            else:
                db.ans = z[0:-k] + y
                break
        
    elif y[-k:] == z[0:k]:
        while k < 20:
            if y[-k:] == z[0:k]:
                k += 1
            else:
                db.ans = y + z[k:]
                break         

def serach():
    for i in range(2,len(open('mutant_R1.fastq', 'rU').readlines()),4):
        data_1 = linecache.getline('mutant_R1.fastq',i).strip()
        for j in range(2,len(open('mutant_R2.fastq', 'rU').readlines()),4):
            data_2 = linecache.getline('mutant_R2.fastq',j).strip()
            find_taget(data_1,data_2)
    
    for i in range(2,len(open('mutant_R1.fastq', 'rU').readlines()),4):
        data_1 = linecache.getline('mutant_R1.fastq',i).strip()
        if db.ans != "":    
            two_pair(data_1)
            
    for j in range(2,len(open('mutant_R2.fastq', 'rU').readlines()),4):
        data_2 = linecache.getline('mutant_R2.fastq',j).strip()
        if db.ans != "":    
            two_pair(data_2)
      
start = time.time()
line_1 = open('mutant_R1.fastq', 'r')
line_2 = open('mutant_R2.fastq', 'r') 
data_1 = line_1.readlines()
data_2 = line_2.readlines()
serach()
line_1.close()
line_2.close()
end = time.time()
print("Not used : ",db.not_use)
print("String lenght : ",len(db.ans))
print("Time used : %f(sec)" % (end - start))
#file = open('Midexam.txt','a+')
#file.write(db.ans)
#file.close()
