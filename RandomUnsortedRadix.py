import random
my_file = open("Input.txt", "r")

data = []
for line in my_file.readlines():
    line = line.strip()
    data.append(line.split(" "))
my_file.close()

n = int(data[0][0])
m = int(data[1][0])
data.pop(0)
data.pop(0)
S = []      #list of subsets
W = []      #list of weights
R = []      #list of ratios

for i in range(0,len(data)):
    if (i % 2) == 0:                #line is even and therfore contians the subset
        S.append([int(x) for x in data[i]])
    else:                           #line is odd and therefore contains the wight of the subset
        W.append((data[i][0]))
        R.append([len(S[-1])/int(W[-1]), len(R)+1])

radixRatio = [None] *n

for i in range(0,m):                                #Goes through every subset
    for j in range (0,len(S[i])):                   #Goes through every value of the subset.
        if radixRatio[int(S[i][j]) -1] == None:
            radixRatio[int(S[i][j]) -1]= [R[i]]
        else:
            radixRatio[int(S[i][j]) -1].append(R[i])

for k in range(0,100000):
    U = []
    weight = 0
    answer = []
    N = [i for i in range(1,n+1)]

    while not len(N)==0 :
        i = random.choice(N)
        if not(i in U):
            randomIndex=random.randrange(0,len(radixRatio[i-1]))
            set = S[radixRatio[i-1][randomIndex][1] -1]
            weight = weight + int(W[radixRatio[i-1][randomIndex][1] -1])
            answer.append(int(radixRatio[i-1][randomIndex][1]))
            for j in range(0,len(set)):
                U.append(set[j])
        N.remove(i)
    if k==0:
        bestweight=weight
        bestanswer=answer
    elif weight < bestweight:
        bestweight = weight
        bestanswer = answer
    if (k%1000) ==0:
        print(bestweight)
        print(*bestanswer, sep=' ')

answer.sort()
print(bestweight)
print(bestanswer)
print(*bestanswer, sep=' ')
