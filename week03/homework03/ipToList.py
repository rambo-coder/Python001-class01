def ipToList(startIP, endIP):
    resultLIst = []
    sArray = startIP.split('.')

    startNum = sArray[3]
    endNum = endIP.split('.')[3]

    for i in range(int(startNum),int(endNum)+1):
        resultLIst.append(sArray[0]+'.'+sArray[1]+'.'+sArray[2]+'.'+str(i))
    return resultLIst

