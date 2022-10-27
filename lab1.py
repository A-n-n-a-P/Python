import pandas as pd

class workWithFile:
    fileContent = ''

    def __init__(self, nameFile):
        self.fileContent = pd.read_csv(nameFile)

    def sorting(self, column, value):
        self.fileContent.sort_values(by= self.fileContent.columns[column], ascending= value, inplace= True)

    def oneString(self):
#        row = self.fileContent.sample(1)
#        row2 = self.fileContent.loc[0]
        row3 = self.fileContent.take([1])
        return row3

    def amount(self):
        return self.fileContent.size

    def subsetOfString(self):
        randomSubset = self.fileContent.sample(frac= 0.5)
        subset = self.fileContent.take([1, 3, 5])
        return subset

    def writingToFile(self):
        self.fileContent.to_csv('sortingResult.csv')

fc = workWithFile('forLab1.csv')
print(fc.fileContent)
fc.sorting(1, True)
print("Sort result")
print(fc.fileContent)
print("One row from file")
print(fc.oneString())
print('Amount of elements')
print(fc.amount())
print('Subset of string')
print(fc.subsetOfString())
