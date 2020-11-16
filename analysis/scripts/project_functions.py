import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

def load_clean_df(path):

    df = (
            
        #read data to df, drop NULLs.
        pd.read_csv(path)
        .dropna()
        
    )
    
    return df

def display_big_picture(df):
    
    #displays the general form of all the data
    print(df.describe())
    
    plt.figure(figsize = (25, 20))
    
    plt.subplot(7, 7, 1)
    plt.hist(df.age, edgecolor = "black")
    plt.xlabel("age")
    
    plt.subplot(7, 7, 2)
    plt.hist(df.sex, edgecolor = "black")
    plt.xlabel("sex")
    
    plt.subplot(7, 7, 3)
    plt.hist(df.bmi, edgecolor = "black")
    plt.xlabel("bmi")
    
    plt.subplot(7, 7, 4)
    plt.hist(df.children, edgecolor = "black")
    plt.xlabel("children")
    
    plt.subplot(7, 7, 5)
    plt.hist(df.smoker, edgecolor = "black")
    plt.xlabel("smoker")
    
    plt.subplot(7, 7, 6)
    plt.hist(df.region, edgecolor = "black")
    plt.xlabel("region")
    
    plt.subplot(7, 7, 7)
    plt.hist(df.charges, edgecolor = "black")
    plt.xlabel("charges")
    
    plt.show()
    
def cost_is_smoker(df):
    
    
    
def remove_smokers_highlowBMI_highAge(df):
        
    # this function is just to remove at-risk populations from a set of data to showcase method chaining. This may not have any application to the actual project.
        
    df = (
            
        #remove low bmi, high bmi, smokers, high age --> risk groups. Remove smoker column because all are NO.
        df
        .loc[lambda x: x['bmi'] > 18]
        .loc[lambda x: x['bmi'] < 28]
        .loc[lambda x: x['smoker'] == 'no']
        .loc[lambda x: x['age'] < 40]
        .drop('smoker', 1)

    )
        
    return df