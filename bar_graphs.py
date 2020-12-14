'''
Plan: Important word categories and data spreadsheets as pandas dataframes.
    Create an indiscriminate bar graph for the three categories across ALL
    words. Create a list of words in each category (i.e. the variable
    'sAndConsonants' will be all the words that start with sCC). For the words
    in that category, create a bar graph displaying the data. The list of words
    can be collected s.t. their position in the list, x, (starting at 0) is the
    only thing recorded. It can then be found by looking at the 3x + 7, 3x + 8,
    and 3x + 9 columns in the data for its category A, B, and C conjugations,
    respectively.
'''

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Import data
categories = pd.read_excel('word_categories.xlsx')
data = pd.read_excel('responses.xlsx')

# Edit data so only words and average responses remain
data = data.drop(data.columns[0:3], axis = 1, inplace = False) #removing unnecessary columns
mean = data[data.columns].mean() #finding the means of each column
data = data.append(mean, ignore_index = True) #add the means to the df to maintain df integrity
averages = data.drop(range(len(data.index) - 1), axis = 0, inplace = False) #remove unnecessary remaining rows

# bar graph creation function
def bar_graph(data, title):

    # Get items in each conjugation category
    A = [item for item in data if item.startswith('A')]
    B = [item for item in data if item.startswith('B')]
    C = [item for item in data if item.startswith('C')]

    # Get mean in each conjugation category and make them into a list
    A_mean = data[A].mean(axis=1).tolist()
    B_mean = data[B].mean(axis=1).tolist()
    C_mean = data[C].mean(axis=1).tolist()
    yAxis = A_mean + B_mean + C_mean

    # Plot that data using the following three conjugation categories:
    xAxis =  ["-ed", "/æ/", "/ʌ/"]
    plt.bar(xAxis,yAxis)
    plt.title(title)
    plt.xlabel('Past Tense Conjugation')
    plt.ylabel('Average Given Score')
    plt.show()

def get_category_words(data, category, section):
    x = categories.loc[categories[section] == category]
    words = x['A. "-ed"'].tolist() + x['B. "/æ/"'].tolist() + x['C. "/ʌ/"'].tolist()
    cat_averages = averages

    for col in cat_averages.columns:
        if not any(x in col for x in words):
            cat_averages = cat_averages.drop(col, axis = 1, inplace = False)
    bar_graph(cat_averages, category)

# Indiscriminate-data analysis
bar_graph(averages, 'All words')

# sCC analysis
get_category_words(data, 'sCC', 'initial_consonants')

# sC analysis
get_category_words(data, 'sC', 'initial_consonants')

# CC analysis
get_category_words(data, 'CC', 'initial_consonants')

# C analysis
get_category_words(data, 'C', 'initial_consonants')

# ŋ / ŋk (nasal) analysis
get_category_words(data, 'nasal', 'final_consonants')

# k / g analysis
get_category_words(data, 'k/g', 'final_consonants')

# n / m analysis
get_category_words(data, 'n/m', 'final_consonants')

# C (other consonant) analysis
get_category_words(data, 'C', 'final_consonants')

