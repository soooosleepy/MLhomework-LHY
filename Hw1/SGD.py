import DataExtract
import numpy as np
import random
import pandas as pd



def LossFuction(parametes,dataset):
    #parameters has the form of [b,w1,w2,w3...wn]
    #each iterm of the dateset has the form of [yhat,x1,x2,x3...xn]
    lf = 0
    for ii in dataset:
        temp = parametes[0]
        for jj in range(1,len(parametes)):
            temp += parametes[jj]*ii[jj]
        temp_lf = (ii[0] - temp)**2
        lf += temp_lf
    return lf

def Gradient(parametes,data):
    returnvalue = []
    temp = parametes[0]
    for ii in range(1,len(parametes)):
        temp += parametes[ii]*data[ii]
    temp1 = (data[0] - temp)*2
    # print(parametes)
    # print(temp)
    for ii in data:
        returnvalue.append(ii*temp1)
    return returnvalue



def Adagrad(parameters,newdata,sum_of_grad_square,learningrate):
    para = []
    newgrad = Gradient(parameters,newdata)
    # print(newgrad)
    sum_of_grad_square.append((np.linalg.norm(newgrad))**2)
    c = sum(sum_of_grad_square)
    const = -(learningrate/(c**0.5))
    # print(const)
    # print(sum_of_grad_square)
    grad = []
    for ii in newgrad:
        a = ii*const
        grad.append(a)
        # print(ii)
        # print(const)
    for ii in range(len(grad)):
        para.append(parameters[ii] - grad[ii])
        # print(grad[ii])
    return para



p = DataExtract.readdata('train.csv')
plist = []
for ii in p:
    temp = []
    temp.append(ii.temp)
    temp.append(ii.CH4)
    temp.append(ii.CO)
    temp.append(ii.NMHC)
    temp.append(ii.NO)
    temp.append(ii.NO2)
    temp.append(ii.NOx)
    temp.append(ii.O3)
    temp.append(ii.PM10)
    temp.append(ii.PM25)
    temp.append(ii.rainfall)
    temp.append(ii.RH)
    temp.append(ii.SO2)
    temp.append(ii.THC)
    temp.append(ii.WD_HR)
    temp.append(ii.wind_direct)
    temp.append(ii.wind_speed)
    temp.append(ii.WS_HR)
    plist.append(temp)
for ii in range(len(plist[0])):
    temp = []
    for jj in range(len(plist)):
        if(plist[jj][ii] != -1):
            temp.append(plist[jj][ii])
    arr_mean = np.mean(temp)
    arr_std = np.std(temp,ddof=1)
    for jj in range(len(plist)):
        if(plist[jj][ii] != -1):
            plist[jj][ii] = (plist[jj][ii] - arr_mean)/arr_std

# print(plist[2343])
database = []
for ii in range(9,len(plist)):
    if((plist[ii-9][2] != -1) and (plist[ii-8][1] != -1) and(plist[ii-7][1] != -1) and(plist[ii-6][1] != -1) and(plist[ii-5][1] != -1) and(plist[ii-4][1] != -1) and(plist[ii-3][1] != -1) and(plist[ii-2][1] != -1) and(plist[ii-1][1] != -1) and(plist[ii][1] != -1)):
        temp = []
        temp.append(plist[ii][9])
        for jj in range(9):
            for kk in range(len(plist[1])):
                temp.append(plist[ii-jj][kk])
        database.append(temp)

# print(database[1][1])
random.shuffle(database)

print(np.shape(database))
init_parameters = [0 for i in range(163)]

dataset1 = [database[i] for i in range(0,1884)]
dataset2 = [database[i] for i in range(1884,3768)]
dataset3 = [database[i] for i in range(3768,5652)]

print(LossFuction(init_parameters,dataset1))
print(LossFuction(init_parameters,dataset2))
print(LossFuction(init_parameters,dataset3))

sum_of_grad2 = [0]

# learingrate = 0.08
# trainingset = dataset1
# for ii in range(len(dataset1)):
#     init_parameters = Adagrad(init_parameters,trainingset[ii],sum_of_grad2,learingrate)
#     lf1 = LossFuction(init_parameters,trainingset)
#     lf2 = LossFuction(init_parameters,dataset3)
#     # print(sum_of_grad2)
#     print("loop: " + str(ii+1) + "| lossfunction on training set: " + str(lf1) + "| lossfunction on testing set: " + str(lf2))



data1 = pd.read_csv('test.csv',header = None)
list1 = data1.values.tolist()

temp_testingset = []
for ii in range(len(list1)):
    temp = []
    for jj in range(len(list1[ii])):
        if(jj > 1):
            if(list1[ii][jj] == "NR"):
                temp.append(0)
            else:
                temp.append(float(list1[ii][jj]))
    temp_testingset.append(temp)
testingset = []
for ii in range(240):
    temp = [-1]
    for jj in range(9):
        for kk in range(18):
            temp.append(temp_testingset[kk][jj])
    testingset.append(temp)
    for ll in range(18):
        del(temp_testingset[0])
print(testingset)


