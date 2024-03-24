
class Helper:

    def __init__(self) -> None:
        pass

    def calculateDieMean(probArr, numFaces):
        mean = 0
        for i in range(1, numFaces + 1):
            mean = i * probArr[i - 1] + mean
        return mean

    def calculateDieVar(probArr, numFaces, mean):

        doubleVal = 0
        for i in range(1, numFaces + 1):
            doubleVal = pow(i, 2) * probArr[i - 1] + doubleVal
        
        return doubleVal - pow(mean, 2)
    
    def subtractArr(lArr, rArr, arrSize):
        arr = [0] * arrSize
        i = 0
        for x in lArr:
            arr[i] = abs(rArr[i] - x)
            i = i + 1
            
        return arr