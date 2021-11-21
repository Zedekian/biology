import linecache
import time

target = ""
start = time.time()
line_1 = open('Mid_exam_A_String.txt', 'r')
line_2 = open('wildtype.fna', 'r') 
data_1 = line_1.read()
data_2 = line_2.readlines()
for i in range(2,len(open('wildtype.fna', 'rU').readlines())):
    data_2 = linecache.getline('wildtype.fna',i).strip()
    target += data_2
target = target.upper()

line_1.close()
line_2.close()

if len(data_1) > len(target):
    long = data_1
    short = target
else:
    long = target
    short = data_1     

class db:
   ans = ""
   data = [short,long]
   count = 0
   match = 0
   mismatch = 0
   gap = 0
while (db.count + 1 ) < int(len(db.data[0])) - 1:
    if db.data[0][db.count] == db.data[1][db.count]:
        db.ans += db.data[0][db.count]
    else:
        if db.data[0][db.count] == db.data[1][db.count + 1]:
            db.data[0] = db.data[0][:db.count] + "_" + db.data[0][db.count:]
        elif db.data[0][db.count + 1] == db.data[1][db.count]:
            db.data[1] = db.data[1][:db.count] + "_" + db.data[1][db.count:]   
    db.count += 1

db.count = 0
while (db.count + 1 ) < int(len(db.data[0])) - 1:
    if ((db.data[0][db.count])  == "_")  or  ((db.data[1][db.count]) == "_"):
        db.gap += 1
    elif db.data[0][db.count] != db.data[1][db.count]:
        db.mismatch += 1
    elif db.data[0][db.count] == db.data[1][db.count]:
        db.match += 1
    db.count += 1


print("Match : ",db.match)
print("Mismatch : ",db.mismatch)
print("Gap : ",db.gap)
print("Total score: ",(db.match) + (db.mismatch * -2) + (db.gap * -3))
end = time.time()
print("Run time : %f(sec)" % (end - start))
#file_1= open('Mid_exam_B_String_1.txt','a+')
#file_2 = open('Mid_exam_B_String_2.txt','a+')
#file_1.write(db.data[0])
#file_2.write(db.data[1])
#file_1.close()
#file_2.close()