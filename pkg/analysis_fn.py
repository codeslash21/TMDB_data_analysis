# Create the ffunctions necessary for our analysis

# import necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# create max_min function to get details of maximum and minimum of the given column
def max_min(df, col):
    '''
    args:  df: dataframe
           col: column name
    
    return a dataframe with two columns
    '''
    # get indices of max and min values
    max_idx = df[col].idxmax()
    min_idx = df[col].idxmin()
    
    # get the rows where max and min values are present
    max_row = pd.DataFrame(df.loc[max_idx])
    min_row = pd.DataFrame(df.loc[min_idx])
    max_row.columns = max_row.loc['original_title']
    min_row.columns = min_row.loc['original_title']
    
    return pd.concat([max_row, min_row], axis=1)


# Create function to make sns plot with top 10 values of the given column
def sns_plot(df, col, title, xlabel, color):
    '''
    args: df: dataframe
          col: column name,
          title,
          xlabel,
          color
          
    return: A seaborn plot
    '''
    info = pd.DataFrame(df.sort_values(by=col, ascending=False))
    x = list(info[col])[:10]
    y = list(info.original_title)[:10]

    plot_ax = sns.pointplot(x=x, y=y, color=color)
    plot_ax.set_title(title, fontsize=16)
    plot_ax.set_xlabel(xlabel, fontsize=14)
    sns.set(rc={'figure.figsize':(10,5)})
    sns.set_style('whitegrid')
    
    plt.setp(plot_ax.collections, alpha=0.8)
    plt.setp(plot_ax.lines, alpha=0.6)
    

# create function to create line plot to see the trend between two variables.
def cmp_line(df, var1, var2, xticks, title, xlabel, ylabel, color):
    '''
    args: 
        df: dataframe
        var1: column name to create a groupby object
        var2: column name to compare with the first column
        xticks: list of xticks
        title: title of the plot
        xlabel: label of X axis of the plot
        ylabel: label of Y axis of the plot
        color: color of the line
        
    return: A line plot
    '''
    df.groupby(var1)[var2].mean().plot(color=color, xticks=xticks)

    sns.set(rc={'figure.figsize':(10,5)})
    sns.set_style('whitegrid')

    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    
    
# Create function to devide the numerical columns into some levels and make bar plot to analyse relationship between two variables.
def cmp_bar(df, var1, var2, levels, title, xlabel, ylabel):
    '''
    args: 
        df: dataframe
        var1: column name whose values have to be leveled and create a new column with that
        var2: column name to compare with the newly created column
        title: title of the plot
        xlabel: label of X axis of the plot
        ylabel: label of Y axis of the plot
        
    return: A bar plot
    '''
    df[var1+'_level'] = pd.cut(df[var1], levels)

    df.groupby(var1+'_level')[var2].mean().plot(kind='bar', alpha=.9)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    
    
# Create function to make scatter plot to analyse the trend between two variables.
def cmp_scatter(df, var1, var2, title, xlabel, ylabel, color):
    '''
    args: 
        df: dataframe
        var1: column name whose values will be on X-axis
        var2: column name whose values will be on Y-axis
        title: title of the plot
        xlabel: label of X axis of the plot
        ylabel: label of Y axis of the plot
        color: color of the points
        
    return: A scatter plot
    '''
    plot_ax = sns.regplot(x=df[var1], y=df[var2], color=color)

    sns.set(rc={'figure.figsize':(10,5)})
    sns.set_style('whitegrid')

    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.setp(plot_ax.collections, alpha=.7)

    print('Correlation Coefficient is: ', df.corr().loc[var1, var2].round(10))
    
    
# Here create a function to count indivisual value in a column where values are combined and seperated by '|' in the 
# cells of the dataframe. This function take column_name as argument and return a pnadas Series.
def count_category(df, col):
    '''
    args: 
        df: dataframe
        col: column name whose values has to be counted
    
    return: A pnadas series with the counts of all unique values
    '''
    total_values = df[col].str.cat(sep='|')
    values_list = pd.Series(total_values.split(sep='|'))
    return values_list.value_counts(ascending=False)


# create a function to count the values using count_category() and make bar plot with that count
def category_plot(df, col, limit, plot_kind, text, title, xlabel, ylabel):
    '''
    args: df: dataframe
          col: column name whose alues have to be counted
          limit: Number of unique values to be in plot. -1 if all
          plot_kind: kind of the plot vertical or horizontal
          title: title of the plot
          xlabel: label of X axis of the plot
          ylabel: label of Y axis of the plot
        
    return: A bar plot
    '''
    total_count = count_category(df, col)
    print(text.format(total_count.shape[0]), '\n') # print number of unique values
    print(total_count.iloc[:3]) # Print top 3 counts
    
    total_count.iloc[:limit].plot(kind=plot_kind, fontsize=13, figsize=(14,7), alpha=.9)
    sns.set_style('whitegrid')

    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    
    
# create a function to visualize categorical variable over year
def category_over_yr(df, title, xlabel, ylabel):
    '''
    args: df: Dataframe used to create visualization
          title: title of the plot
          xlabel: xlabel of the plot
          ylabel: ylabel of the plot
          
    return: A bar diagram
    '''
    df.plot(kind='bar', figsize=(15,7), fontsize=14);

    # set style and label the plot
    sns.set_style('whitegrid');
    plt.title(title, fontsize=16, fontweight='bold');
    plt.xlabel(xlabel, fontsize=14);
    plt.ylabel(ylabel, fontsize=14);
    
    
# create a 'standerize' function which takes a dataframe as an argument and return that dataframe with standerize values.
def standerize(df):
    '''
    args: df: Dataframe
    
    return: Dataframe with standerize values
    '''
    return (df - df.mean()) / df.std()


