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
    
    plt.figure(figsize = (30, 25))
    
    plt.subplot(7, 7, 1)
    plt.hist(df.age, edgecolor = "black")
    plt.xlabel("Age")
    plt.ylabel("Count")
    
    plt.subplot(7, 7, 2)
    plt.hist(df.sex, edgecolor = "black")
    plt.xlabel("Sex")
    plt.ylabel("Count")
    
    plt.subplot(7, 7, 3)
    plt.hist(df.bmi, edgecolor = "black")
    plt.xlabel("BMI")
    plt.ylabel("Count")
    
    plt.subplot(7, 7, 4)
    plt.hist(df.children, edgecolor = "black")
    plt.xlabel("Children")
    plt.ylabel("Count")
    
    plt.subplot(7, 7, 5)
    plt.hist(df.smoker, edgecolor = "black")
    plt.xlabel("Smoker")
    plt.ylabel("Count")
    
    plt.subplot(7, 7, 6)
    plt.hist(df.region, edgecolor = "black")
    plt.xlabel("Region")
    plt.ylabel("Count")
    
    plt.subplot(7, 7, 7)
    plt.hist(df.charges, edgecolor = "black")
    plt.xlabel("Charges")
    plt.ylabel("Count")
    
def cost_is_smoker(df):
    
    sns.barplot(x = "smoker", y = "charges", data = df)
    plt.xlabel("isSmoker?")
    plt.ylabel("Charges")
    
def cost_by_age(df):
    
    plt.figure(figsize = (8, 6))
    sns.scatterplot(x = "age", y = "charges", data = df)
    plt.xlabel("Age")
    plt.ylabel("Charges")
    
def cost_by_sex(df):
    
    plt.figure(figsize = (10, 5))
    sns.barplot(x = "sex", y = "charges", data = df)
    plt.xlabel("Sex")
    plt.ylabel("Charges")
    
def smokers_by_sex(df):
    
    df1 = df[df['smoker'] == 'yes']
    df1  = df1.groupby(['sex'])['smoker'].count()
    print(df1.head())
    
    print('\n')
    
    df2 = df[df['smoker'] == 'no']
    df2  = df2.groupby(['sex'])['smoker'].count()
    print(df2.head())
    
def cost_by_bmi(df):
    
    plt.figure(figsize = (8, 6))
    sns.scatterplot(x = "bmi", y = "charges", data = df)
    plt.xlabel("BMI")
    plt.ylabel("Charges")
    
def cost_by_bmi_and_sex(df):
    
    plt.figure(figsize = (8, 6))
    sns.scatterplot(x = "bmi", y = "charges", hue = "sex", data = df)
    plt.xlabel("BMI")
    plt.ylabel("Charges")
    
def cost_by_children(df):
    
    sns.catplot(x = "children", y = "charges", data = df, kind = "violin")
    plt.suptitle("Charges by Number of Children")
    plt.xlabel("Number of Children")
    plt.ylabel("Charges")
    
def cost_by_age_and_smoker(df):
    
    plt.figure(figsize = (8, 6))
    sns.scatterplot(x = "age", y = "charges", hue = "smoker", data = df)
    plt.xlabel("Age")
    plt.ylabel("Charges")
    
def cost_by_bmi_and_smoker(df):
    
    plt.figure(figsize = (8, 6))
    sns.scatterplot(x = "bmi", y = "charges", hue = "smoker", data = df)
    plt.xlabel("BMI")
    plt.ylabel("Charges")
    
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