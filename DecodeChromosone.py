#Pre: Binary Chromosone, numpy array of ones and zeros
#Ret: Variabels Enconded in the chromsone, Doubles

def decodeBinaryChromosone(chrom):
    intrevall = [0,1]
    diff = intrevall[1]-intrevall[0]
    varLength = 25
    numVar = int(chrom.size/25)

    decodeVar = []
    for i in range(numVar):
        pow = -1
        sum = 0
        for j in range(varLength):
            sum += chrom[i*varLength + j]*2**(pow)
            pow += -1
        decodeVar.append(intrevall[0]+diff/(1-2**(-varLength))*sum)

    return(decodeVar)
