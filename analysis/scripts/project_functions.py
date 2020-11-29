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

def discard_children_region(df):
    
    df.drop(['children', 'region'], axis = 1, inplace = True)
    return df

def display_big_picture(df):
    
    #displays the general form of all the data
    
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
    plt.xlabel("Charges ($)")
    plt.ylabel("Count")
    
def cost_is_smoker(df):
    
    plt.figure(figsize = (10, 8))
    sns.boxplot(x = "smoker", y = "charges", data = df)
    plt.xlabel("isSmoker?", fontsize = 15)
    plt.ylabel("Charges ($)", fontsize = 15)
    plt.title("Charges by Smoker Status", fontsize = 15)
    
def cost_by_age(df):
    
    plt.figure(figsize = (10, 8))
    sns.scatterplot(x = "age", y = "charges", data = df)
    plt.xlabel("Age", fontsize = 15)
    plt.ylabel("Charges ($)", fontsize = 15)
    plt.title("Charges Across Age", fontsize = 15)
    
def cost_by_sex(df):
    
    plt.figure(figsize = (10, 8))
    sns.catplot(x = "sex", y = "charges", data = df, kind = "violin")
    plt.xlabel("Sex", fontsize = 15)
    plt.ylabel("Charges ($)", fontsize = 15)
    plt.title("Charges by Sex", fontsize = 15)
    
def smokers_by_sex(df):
    
    df1 = df[df['smoker'] == 'yes']
    df1  = df1.groupby(['sex'])['smoker'].count()
    print("smoker = YES")
    print(df1.head())
    
    print('\n')
    
    df2 = df[df['smoker'] == 'no']
    df2  = df2.groupby(['sex'])['smoker'].count()
    print("smoker = NO")
    print(df2.head())
    
def cost_bmi_by_sex(df):
    
    plt.figure(figsize = (10, 8))
    sns.scatterplot(x = "bmi", y = "charges", data = df, hue = "sex")
    plt.xlabel("BMI", fontsize = 15)
    plt.ylabel("Charges ($)", fontsize = 15)
    plt.title("Charges Across BMI by Sex", fontsize = 15)
    
def cost_by_bmi(df):
    
    plt.figure(figsize = (10, 8))
    sns.scatterplot(x = "bmi", y = "charges", data = df)
    plt.xlabel("BMI", fontsize = 15)
    plt.ylabel("Charges ($)", fontsize = 15)
    plt.title("Charges Across BMI", fontsize = 15)
    
def cost_by_children(df):
    plt.figure(figsize = (10, 8))
    sns.catplot(x = "children", y = "charges", data = df, kind = "violin")
    plt.suptitle("Charges by Number of Children", fontsize = 15)
    plt.xlabel("Number of Children", fontsize = 15)
    plt.ylabel("Charges ($)", fontsize = 15)
    
def cost_by_age_and_smoker(df):
    
    plt.figure(figsize = (10, 8))
    sns.scatterplot(x = "age", y = "charges", hue = "smoker", data = df)
    plt.xlabel("Age", fontsize = 15)
    plt.ylabel("Charges ($)", fontsize = 15)
    plt.title("Charges by Age and Smoker Status", fontsize = 15)
    
def cost_by_bmi_and_smoker(df):
    
    plt.figure(figsize = (10, 8))
    sns.scatterplot(x = "bmi", y = "charges", hue = "smoker", data = df)
    plt.xlabel("BMI", fontsize = 15)
    plt.ylabel("Charges ($)", fontsize = 15)
    plt.title("Charges Across BMI by Smoker Status", fontsize = 15)
    
def cost_by_region(df):
    
    plt.figure(figsize = (10, 8))
    sns.catplot(x = 'region', y = 'charges', data = df, kind = 'violin')
    plt.xlabel("Region", fontsize = 15)
    plt.ylabel("Charges ($)", fontsize = 15)
    plt.title("Charges by Region", fontsize = 15)
    
    #this function will produce how many % of the entire sample are smoker versus how many % of the most expensive medical cost people from 25% sample are smoker 
def show_smoker_table(df):
    smoker = df.loc[df['smoker'] == 'yes']
    return smoker
    
    #this function will show how many people are smoker in the sample
def show_num_smoker(df):
    return len(df.loc[df['smoker'] == 'yes'].index)
    
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

#this function finds how many smoker are in the top 25% sample with highest medical charges

def how_many_smoker_in_25_sample(df):
    #wrangle data by making a df based on charges sorting
    df2 = df.sort_values(by=['charges'],ascending=False)
    top25 = df2.iloc[0:335]
    return len(top25.loc[top25['smoker'] == 'yes'].index)


# this function compares the smoker among the top 25% of sample with highest medical charges with original sample using a bar graph to represent how much % of the sample are smokers
def compare_smoker(df):
    r1 = 255/335
    r2 = 274/1334
    d = {'samples': ['top 25% with highest medical charges', 'original sample'], 'percent of people that are smokers':[r1,r2]}
    df5 = pd.DataFrame(data=d)
    sns.barplot(x='samples',y='percent of people that are smokers',data=df5)
    
    
# this function will compare the distribution of overweight, underweight people in the orginal sample versus the top 25% of the sample with highest medical charges 
def compare_weight(df):
    df2 = df.sort_values(by=['charges'],ascending=False)
    top25 = df2.iloc[0:335]
    numWeightInSample = len(df.loc[df['bmi'] < 15].index) + len(df.loc[df['bmi'] > 30].index)
    numWeightIn25Sample = len(top25.loc[top25['bmi'] < 15].index) + len(top25.loc[top25['bmi'] > 30].index)
    r1 = numWeightIn25Sample/335
    r2 = numWeightInSample/1334
    d = {'samples': ['top 25% with highest medical charges', 'original sample'], 'percent people that are underweight or overweight':[r1,r2]}
    df5 = pd.DataFrame(data=d)
    sns.barplot(x='samples',y='percent people that are underweight or overweight',data=df5)
    
                 
                 
# this function will compare does smokers pay more on average than non smoker?
def charge_smoker(df):
                 sns.barplot(x = "smoker", y = "charges", data = df)
                 plt.xlabel("Smoker?")
                 plt.ylabel("Charges")
                 
# this function will show the relationship between bmi and charges
def charges_bmi(df):
                 sns.scatterplot(x = "bmi", y = "charges", data = df)
                 plt.xlabel("BMI")
                 plt.ylabel("Charges")

#this function will produce a plot to show the relationship between risk_score and charges
def cost_by_risk_factor(df):
    sns.catplot(x = "Risk Score Total", y = "charges", data = df, kind = "violin")
    plt.suptitle("Charges by risk score")
    plt.xlabel("risk score")
    plt.ylabel("Charges")
                 
                 
        
        
        
    
    
                                                                      
                                                                      
                                    


    
    