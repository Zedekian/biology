source_1 = "ATTAGACCTG"
source_2 = "CCTGCCGGAA"
source_3 = "AGACCTGCCG"
source_4 = "GCCGGAATAC"
class db:
    ans = ""
    data = [source_1,source_2,source_3,source_4]
def find_first ():
    
    while len(db.ans) == 0:
        count = int(len(source_1) / 2 )+ 1
        for i in range(int(len(db.data) - 1),-1,-1):   #serach from last
            for j in range(int(len(db.data) - 2),-1,-1):
                if (db.data[i][-count:] in db.data[j][0:count]) == True:
                    db.ans = db.data[i] + db.data[j][count:]
                    remove_1 = db.data[i]
                    remove_2 = db.data[j]
                    db.data.remove (remove_1)
                    db.data.remove (remove_2)
                    return 
        count += 1
        for i in range(0,int(len(db.data)),1):     #serach from first
            for j in range(i + 1,int(len(db.data)),1):
                if (db.data[i][-count:] in db.data[j][0:count]) == True:
                    db.ans = db.data[i] + db.data[j][count:]
                    remove_1 = db.data[i]
                    remove_2 = db.data[j]
                    db.data.remove (remove_1)
                    db.data.remove (remove_2)
                    return   
        count += 1    
find_first()
def find_last ():
    count = int(len(source_1) / 2 )+ 1
    while len(db.data) != 0:
        for i in range(int(len(db.data) - 1),-1,-1):   #serach from last
            if (db.ans[-count:] in db.data[i][0:count]) == True:
                db.ans = db.ans + db.data[i][count:]
                remove_1 = db.data[i]
                db.data.remove (remove_1)
                return 
        count += 1
while len(db.data) != 0:
    find_last()
print(db.ans)
