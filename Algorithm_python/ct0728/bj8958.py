import sys

testCase = int(sys.stdin.readline().strip())

for i in range(testCase) :
    testCaseTmp = list(sys.stdin.readline().strip())
    count = 0
    sum = 0
    for j in range(len(testCaseTmp)) :

        if(testCaseTmp[j] == "O") :
            count += 1
            sum += count
        elif(testCaseTmp[j] == "X") :
            count = 0
    print(sum)