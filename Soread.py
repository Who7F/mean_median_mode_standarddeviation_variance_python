import pandas as pd #pip instill seaborn
import numpy as np
#import re
import matplotlib.pyplot as plt
import seaborn as sns #pip instill seaborn

#pandas docs reference
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.var.html

def main():
    print("start")
    data = pd.read_csv("operations.csv",parse_dates=[0])
    #data = pd.read_csv("operations.csv")
    print(data)

    
    for cat in data["categ"].unique():
        subset = data[data.categ == cat]
        print("-"*20)
        print('mean:',subset['amount'].mean())
        print('medum:',subset['amount'].median())
        print('mode:',subset['amount'].mode())
        
        print('Variance:',subset['amount'].var(ddof = 0))
        print('Dtandard deviation:',subset['amount'].std(ddof = 0))
        print('Skew',subset['amount'].skew())
        print('Unbiased kurtosis', subset['amount'].kurtosis())

        subset['amount'].hist()
        plt.show()
        f = input('Press enter for next')

    expenses = data[data['amount'] < 0]
    exp = -expenses['amount'].values
    n = len(exp)
    lorenz = np.cumsum(np.sort(exp))/exp.sum()
    lorenz = np.append([0],lorenz)

    plt.axes().axis('equal')
    xaxis = np.linspace(0-1/n,1+1/n,n+1)
    print(xaxis)
    plt.plot(xaxis,lorenz,drawstyle='steps-post')
    plt.show()

if __name__=='__main__':
    main()
