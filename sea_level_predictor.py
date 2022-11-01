import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv ('epa-sea-level.csv',header=0)
       
    # Create scatter plot
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)
    
    # Create first line of best fit
    (slope, intercept, rvalue, pvalue, stderr) = linregress(x,y)
    for i in range(37):
      x=x.append(pd.Series([2014+i]))
    y_pred = intercept + slope*x   
    plt.plot(x,y_pred, color="red")
  
    # Create second line of best fit  
    
    df_new=df.loc[(df['Year']>=2000) & (df['Year']<=df['Year'].max())]
    x=df_new['Year']
    y=df_new['CSIRO Adjusted Sea Level']
    (slope, intercept, rvalue, pvalue, stderr) = linregress(x,y)
    for i in range(37):
      x=x.append(pd.Series([2014+i]))
    y_pred = intercept + slope*x 
    plt.plot(x,y_pred, color="green")

  
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()