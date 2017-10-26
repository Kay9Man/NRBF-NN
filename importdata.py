import matplotlib.pyplot as plt

rawtrain = []
rawtest = []
trainX = []
trainY = []
testX = []
testY = []

with open("TRAIN10X.DAT") as file:
    for line in file:
        rawtrain.append(line.rstrip('\n\r '))
with open("TEST10X.DAT") as file:
    for line in file:
        rawtest.append(line.rstrip('\n\r '))
i = 0
while i < len(rawtrain):
    if rawtrain[i] != '':
        trainX.append(rawtrain[i])
        trainY.append(rawtrain[i+2])
        i += 5
i = 0
while i < len(rawtest):
    if rawtest[i] != '':
        testX.append(rawtest[i])
        testY.append(rawtest[i+2])
        i += 5


print('Train X:')
print(trainX)
print('Train Y:')
print(trainY)
print('Test X:')
print(testX)
print('Test Y:')
print(testY)
