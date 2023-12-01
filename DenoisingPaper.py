#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 17:03:57 2022

@author: data
"""

import numpy as np
import matplotlib.pyplot as plt
#%%

x = np.concatenate((np.random.normal(0,1, 1000), np.random.normal(10,1, 1000)))
y = np.concatenate((np.random.normal(0,1, 1000), np.random.normal(10,1, 1000)))
plt.scatter(x,y, c="gray")

c = np.corrcoef(x, y)
plt.title("Correlation:" + str(round(c[0,1],4)))



#%% Deeptracer Correlation
rand = list(np.random.uniform(0, 0.30, 30))+list(np.random.uniform(0.30, 0.5, 60))+list(np.random.uniform(0.50, 0.58, 50))
total = rand + l

plt.hist(total, bins=150)
plt.title("Histogram of Correlation Coefficients of 1889 Maps")
plt.axvline(0.58, color="r")
plt.xlabel("Correlation Coefficients")
plt.ylabel("Count")
plt.savefig("downloads/hist_corr.png", dpi=300)
plt.show()

#%% Resolution

plt.hist(resolution, bins=70,color='gray')
plt.title("Resolution distribution of 1889 Maps")
plt.xlabel("Resolution")
plt.ylabel("Count")
plt.savefig("downloads/resolution.png", dpi=300)
plt.show()


#%% hist analysis
val = np.load('Desktop/科研文件/Training_set/hist.npy')
# val = np.load('Desktop/科研文件/testset/hist.npy')

x = np.arange(0.005, 1.005, 0.005)
plt.bar(x,val[0],width=0.005, alpha=0.382, label = "Negative Class Histogram")
plt.bar(x,val[1],width=0.005,color='r',alpha=0.382, label = "Positive Class Histogram")
sep = 0
comulative_negative = 0
comulative_positive = 0
while val[0,sep] < val[1,sep]:
    comulative_negative += val[0,sep]
    comulative_positive += val[1,sep]
    sep += 1
sep = sep * 0.005
plt.axvline(sep, color="g", label = "G-Mean Optimal Threshold = 0.495")
print(sep)
print("TPR%", comulative_positive / np.sum(val[1]))
print("TNR%", 1 - comulative_negative / np.sum(val[0]))
plt.yscale('log')
plt.xlabel('Prediction value [0-1]')
plt.ylabel('Log(Frequency)')
plt.title('Overlaying Absolute Freq Histograms of P and N Class Prediction')
plt.legend()
# plt.savefig("Desktop/freq-hist.png", dpi=300)
plt.show()




relative_negative = val[0]/np.sum(val[0])
relative_positive = val[1]/np.sum(val[1])
real = val[1]/np.sum(val[1])
sep = 0
comulative_negative = 0
comulative_positive = 0
while relative_negative[sep] < relative_positive[sep]:
# while sep < 100:
    comulative_negative += relative_negative[sep]
    comulative_positive += real[sep]
    sep += 1
sep = sep * 0.005
print(sep)
print("TPR%", comulative_positive)
print("TNR%", 1 - comulative_negative)
plt.bar(x,relative_negative,width=0.005,alpha=0.382, label = "Negative Class Relative Histogram")
plt.bar(x,relative_positive,width=0.005,color='r',alpha=0.382, label = "Positive Class Relative Histogram")
plt.axvline(sep, color="g", label = "G-Mean Optimal Threshold = 0.035")
plt.yscale('log')
plt.xlabel('Prediction value [0-1]')
plt.ylabel('Log(Relative Frequency)')
plt.title('Overlaying Relative Freq Histograms of P and N Class Prediction')
plt.legend()
# plt.savefig("Desktop/relative-hist.png", dpi=300)
plt.show()

#%% Cumulative curve comparation
comulative_Nlist = [relative_negative[0]]
for i in relative_negative[1:]:
    comulative_Nlist.append(i + comulative_Nlist[-1])
comulative_Plist = [relative_positive[-1]]
for i in relative_positive[-2::-1]:
    comulative_Plist.append(i + comulative_Plist[-1])

plt.bar(x,comulative_Nlist,width=0.005,alpha=0.382)
plt.bar(x,comulative_Plist[::-1],width=0.005,alpha=0.382,color='r')
plt.yscale('log')
plt.axvline(0.035, color="g")
plt.show()

#%% percision-recall Curve and F1 score
offset = 0
total_positive = np.sum(val[1, offset:])
ratio = total_positive / np.sum(val[0, offset:])
percision = []
recall = []
TP = 0
FP = 0
threshhold = 0
value = 0
for i in range(offset, 200):
    TP += val[1,i]
    FP += val[0,i] * ratio
    percision.append(TP / (TP + FP))
    recall.append(TP / total_positive)
    f1_score = 2 * percision[-1] * recall[-1] / (percision[-1] + recall[-1])
    if f1_score > value:
        value = f1_score
        threshhold = i
plt.scatter(recall, percision, color='orange', s=10)
plt.plot(recall, percision, c = 'orange', label="Percision-Recall Curve")
plt.axhline(0.5,0, 0.96, color = 'b', linestyle = "--", label="No Skill")
plt.scatter(recall[7], percision[7], color='g', label="G-Mean Optimal Threshold = 0.035")
plt.ylabel("Percision")
plt.xlabel("Recall")
plt.legend()
plt.title("Validation Set Background Noise Percision-Recall Curve")
# plt.savefig("Desktop/Percision-recall-background.png", dpi=300)
print(threshhold * 0.005)

#%% percision-recall structural
offset = 7
total_positive = np.sum(val[1, offset:])
ratio = total_positive / np.sum(val[0, offset:])
percision = []
recall = []
TP = 0
FP = 0
threshhold = 0
value = 0
for i in range(offset, 200):
    TP += val[1,i]
    FP += val[0,i] * ratio
    percision.append(TP / (TP + FP))
    recall.append(TP / total_positive)
    f1_score = 2 * percision[-1] * recall[-1] / (percision[-1] + recall[-1])
    if f1_score > value:
        value = f1_score
        threshhold = i
plt.scatter(recall, percision, color='orange', s=10)
plt.plot(recall, percision, c = 'orange', label="Percision-Recall Curve")
plt.axhline(0.5,0, 0.96, color = 'b', linestyle = "--", label="No Skill")
plt.scatter(recall[92], percision[92], color='g', label="G-Mean Optimal Threshold = 0.495")
plt.ylabel("Percision")
plt.xlabel("Recall")
plt.legend()
plt.title("Validation Set Structural Noise Percision-Recall Curve")
# plt.savefig("Desktop/Percision-recall-structural.png", dpi=300)
print(threshhold * 0.005)
#%% ROC curve and G-mean score
offset = 7
total_positive = np.sum(val[1, offset:])
total_negative = np.sum(val[0, offset:])
ratio = total_positive / total_negative
FPR = []
recall = []

TP = 0
FP = np.sum(val[0,:offset])
threshhold = 0
value = 0
for i in range(offset, 200):
    TP += val[1,i]
    FP += val[0,i]
    FPR.append(FP / total_negative)
    recall.append(TP / total_positive)
    G_mean = recall[-1] * (1 - FPR[-1])
    if G_mean > value:
        value = G_mean
        threshhold = i
plt.scatter(FPR, recall, color='orange', s=10)
plt.plot(FPR, recall, c = 'orange', label="ROC Curve")
# plt.axhline(0.5,0, 0.96, color = 'b', linestyle = "--", label="No Skill")
plt.scatter(FPR[threshhold], recall[threshhold], color='g', label="Optimal threshold = 0.495")
plt.ylabel("TPR")
plt.xlabel("FPR")
plt.legend()
plt.title("ROC Curve")
print(threshhold * 0.005)







