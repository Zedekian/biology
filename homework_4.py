import linecache
import time
start = time.time()
data_1 = 'sequence.fasta'   #DNA's data
data_2 = 'virus1.fa'
class db:   
    ans_dic = {}
    dic = {     #Genetic code,'X' = Stop
        'UUU' : 'F','UUC' : 'F','UUA' : 'L','UUG' : 'L',
        'CUU' : 'L','CUC' : 'L','CUA' : 'L','CUG' : 'L',
        'AUU' : 'I','AUC' : 'I','AUA' : 'I','AUG' : 'M',
        'GUU' : 'V','GUC' : 'V','GUA' : 'V','GUG' : 'V',
        'UCU' : 'S','UCC' : 'S','UCA' : 'S','UCG' : 'S',
        'CCU' : 'P','CCC' : 'P','CCA' : 'P','CCG' : 'P',
        'ACU' : 'T','ACC' : 'T','ACA' : 'T','ACG' : 'T',
        'GCU' : 'A','GCC' : 'A','GCA' : 'A','GCG' : 'A',
        'UAU' : 'Y','UAC' : 'Y','UAA' : 'X','UAG' : 'X',
        'CAU' : 'H','CAC' : 'H','CAA' : 'Q','CAG' : 'Q',
        'AAU' : 'N','AAC' : 'N','AAA' : 'K','AAG' : 'K',
        'GAU' : 'D','GAC' : 'D','GAA' : 'E','GAG' : 'E',
        'UGU' : 'C','UGC' : 'C','UGA' : 'X','UGG' : 'W',
        'CGU' : 'R','CGC' : 'R','CGA' : 'R','CGG' : 'R',
        'AGU' : 'S','AGC' : 'S','AGA' : 'R','AGG' : 'R',
        'GGU' : 'G','GGC' : 'G','GGA' : 'G','GGG' : 'G',
    }

    def Loding_String(DNA):
        ans = ""
        for i in range(2, len(open(DNA, 'rU').readlines())):
            temp = linecache.getline(DNA, i).strip()
            ans += temp
        ans = ans.upper()
        return db.DNA_to_RNA(ans)

    def DNA_to_RNA(length):
        ans = ""
        for i in range(0, len(length)):
            if length[i] == 'T':
                ans += 'U'
            elif length[i] == 'N':
                ans += 'U'
            elif length[i] == 'R':
                ans += 'A'
            elif length[i] == 'W':
                ans += 'A'
            elif length[i] == 'Y':
                ans += 'C'
            else:
                ans += length[i]
        return ans
    
    def reverse(str):
        return str[len(str)::-1]

    def DNA_complement(str):
        ans = ""
        for i in range(0, len(str)):
            if str[i] == 'U':
                ans += 'A'
            elif str[i] == 'A':
                ans += 'U'
            elif str[i] == 'C':
                ans += 'G'
            elif str[i] == 'G':
                ans += 'C'
        return ans

    def Pair_by_gene(word):
        letter = []
        for count_1 in range(0,3):    #First to third of the leader
            ans = ""
            temp = ""
            for i in range(count_1, len(word)):
                temp_1= word[i]
                temp += temp_1
                if len(temp) == 3:
                    ans += db.dic[temp]
                    temp = ""
            letter.append(ans)
            
        
        word = db.reverse(db.DNA_complement(word))  #Complement and reverse
       
        for count_2 in range(0,3):  #First to third of the leader*2
            ans = ""
            temp = ""  
            for k in range(count_2, len(word)):
                temp_1= word[k]
                temp += temp_1
                if len(temp) == 3:
                    ans += db.dic[temp]
                    temp = ""
            letter.append(ans)
        return letter
    
    def The_longest(word):
        letter = []
        for i in range(0, len(word)):
            letter.append(db.Find_the_longest(word[i]))
        letter.sort(reverse=True)
        return letter[0],db.ans_dic[letter[0]]      #**Final Answer**
    
    def Find_the_longest(word):
        temp = ""
        letter_1 = []
        letter_2 = []
        for i in range(0, len(word)):
            if word[i] == 'M':
                count = i + 1
                for j in range(i, len(word)):
                    temp += word[j]
                    if word[j] == 'X':
                        letter_1.append(temp)
                        db.ans_dic[len(temp)] = (count * 3, (j + 1) * 3)  #Serial number in dic
                        temp = ""
                        count = 0
                        i = j
                        break

        for k in range(0, len(letter_1)):   #Serach the longest length
            letter_2.append(len(letter_1[k]))
        letter_2.sort(reverse=True)     #Sort by high to low
        return letter_2[0]      #Return the longest one

print("The longest length ans SN in",data_1,"is :",db.The_longest(db.Pair_by_gene(db.Loding_String(data_1))))
print("The longest length ans SN in",data_2,"is :",db.The_longest(db.Pair_by_gene(db.Loding_String(data_2))))
end = time.time()
print("Time used : %f(sec)" % (end - start))

