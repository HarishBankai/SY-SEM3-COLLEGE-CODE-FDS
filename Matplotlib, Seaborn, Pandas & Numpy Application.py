import pandas as pd                                                                                   #import pandas library in the notebook
import numpy as np                                                                                    #import numpy library in the notebook
import matplotlib.pyplot as plt                                                                        #import matplotlib library in the notebook
import seaborn as sns                                                                                #import seaborn library in the notebook

#make a sample dataset

data = {
    'DM' : [86, 90, 75, 78, 82, 95] ,
    'DSA' : [77, 80, 85, 68, 89, 95] ,
    'FDS' : [96, 70, 65, 88, 72, 78] , 
    'ADEC' : [76, 80, 75, 68, 82, 87] ,
    'CEP' : [66, 80, 75, 84, 92, 95] , 
    'M2' : [50, 70, 85, 64, 52, 77] 
}

#CREATE A DATAFRAME

df = pd.DataFrame(data)

variance = df.var()                                                                                           #declare variance in pd library                                                       
mean = df.mean()                                                                                           #declare mean in pd library
median = df.median()                                                                                       #declare mean in pd library

print("\nMean : \n", mean)                                                                                   #print mean
print("\nVariance : \n", variance)                                                                         #print variance 
print("\nMedian : \n", median)                                                                             #print median

#HEATMAP FROM SEABORN SNS LIBRARY TO SHOW THE CORRELATION MATRIX

plt.figure(figsize=(10, 10))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidth=0.5)                                         #sns.heatmap: A function from the Seaborn library, used to create a heatmap.
                                                                                                            df.corr(): Computes the correlation matrix of the DataFrame df. 
#continue                                                                                                   annot=True: Displays the correlation values on the heatmap.
#right side just explains the syntax                                                                        cmap='coolwarm': Specifies the colormap, which in this case transitions between cool & warm colors.
                                                                                                           linewidth=0.5: Adds a thin line between the cells for better visual separation.

plt.title("Correlation Matrix :")             #print the matrix
plt.show()                                    #display the matrix


#now use HISTPLOT to show the graph
#this is for DM 

plt.figure(figsize=(10, 10))
sns.histplot(df['DM'], kde=True, color='red', bins=10)
plt.title("Normal Distribution - DM Scores")
plt.xlabel("Score")
plt.xlabel("Frequency")
plt.show()

#this is for DSA

plt.figure(figsize=(10, 10))
sns.histplot(df['DSA'], kde=True, color='blue', bins=10)
plt.title("Normal Distribution - DSA Scores")
plt.xlabel("Score")
plt.xlabel("Frequency")
plt.show()

#this is for FDS

plt.figure(figsize=(10, 10))
sns.histplot(df['FDS'], kde=True, color='green', bins=10)
plt.title("Normal Distribution - FDS Scores")
plt.xlabel("Score")
plt.xlabel("Frequency")
plt.show()

#this is for ADEC

plt.figure(figsize=(10, 10))
sns.histplot(df['ADEC'], kde=True, color='pink', bins=10)
plt.title("Normal Distribution - ADEC Scores")
plt.xlabel("Score")
plt.xlabel("Frequency")
plt.show()

#this is for CEP

plt.figure(figsize=(10, 10))
sns.histplot(df['CEP'], kde=True, color='grey', bins=10)
plt.title("Normal Distribution - CEP Scores")
plt.xlabel("Score")
plt.xlabel("Frequency")
plt.show()

#this is for M2

plt.figure(figsize=(10, 10))
sns.histplot(df['M2'], kde=True, color='purple', bins=10)
plt.title("Normal Distribution - M2' Scores")
plt.xlabel("Score")
plt.xlabel("Frequency")
plt.show()
