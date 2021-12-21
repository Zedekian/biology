import time
start = time.time()

class db:
    
    target = [
           [],                                          #A
           [0.5000],                                    #B
           [0.4286,0.7143],                             #C
           [1.0000,0.8333,1.0000],                      #D
           [0.2500,0.6667,0.4286,1.0000],               #E
           [0.6250,0.2000,0.6667,0.8000,0.7778],        #F
           [0.3750,0.7778,0.3333,0.8571,0.3750,0.7500]  #G 
    ]

    def word_length(start, end):
        labels = []
        for i in range(ord(start),ord(end) + 1):
            labels.append(chr(i))
        return labels
    
    def Find_the_smallest(word):
        min_mun = float("inf")
        temp_1, temp_2 = 0 , 0

        for i in range(len(word)):
            for j in range(len(word[i])):
                if word[i][j] < min_mun:
                    min_mun = word[i][j]
                    temp_1 = i
                    temp_2 = j
        
        return temp_1, temp_2

    def Find_the_biggest(word):
        max_mun = float("-inf")
        temp_1, temp_2 = 0 , 0

        for i in range(len(word)):
            for j in range(len(word[i])):
                if word[i][j] > max_mun:
                    max_mun = word[i][j]
                    temp_1 = i
                    temp_2 = j
        
        return temp_1, temp_2

    def add_target(word, x, y):
        
        temp_list = []
        if y < x:
            x, y = y, x
        
        for i in range(0, x):
            temp_list.append((word[x][i] + word[y][i]) / 2)
        word[x] = temp_list

        for j in range(x + 1, y):
            word[j][x] = (word[j][x] + word[y][j]) / 2

        for k in range(y + 1, len(word)):
            word[k][x] = (word[k][x] + word[k][y]) / 2
            del word[k][y]
        
        del word[y]

    def add_words(word, x, y):
        if y < x:
            x, y = y, x
        
        word[x] = "(" + word[x] + "," + word[y] + ")"
        del word[y]
    
    def single_linkage(list, word):
        
        while len(word) > 1:
            
            temp_1, temp_2 = db.Find_the_smallest(list)

            db.add_target(list, temp_1, temp_2)

            db.add_words(word, temp_1, temp_2)

        return word[0]

node_words = db.word_length("A","G")
print("Single linkage : ",db.single_linkage(db.target, node_words))
end = time.time()
print("Time used : %f(sec)" % (end - start))
