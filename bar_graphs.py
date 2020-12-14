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

# Important categories
conjugations = ['A. "-ed"', 'B. "/æ/"', 'C. "/ʌ/"']
initials = ['sCC', 'sC', 'CC', 'C']
finals = ['nasal', 'k/g', 'n/m', 'C']










'''
Function that takes in data and title and makes a bar graph (for the three
different conjugation types)
'''
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
    plt.ylim(0, 7)
    plt.title(title)
    plt.xlabel('Past Tense Conjugation')
    plt.ylabel('Average Given Score')
    plt.show()


'''
Function that takes in category names and the section in which the category is
applicable (e.g. 'initial_consonants) and makes a bar graph.
'''
def graph_cat(data, category, section):
    x = categories.loc[categories[section] == category]
    words = x['A. "-ed"'].tolist() + x['B. "/æ/"'].tolist() + x['C. "/ʌ/"'].tolist()
    
    cat_averages = averages
    for col in cat_averages.columns:
        if not any(x in col for x in words):
            cat_averages = cat_averages.drop(col, axis = 1, inplace = False)

    title = section + ' = ' + category
    bar_graph(cat_averages, title)


'''
Function that displays a bar_graph of the average score given to a specific
category under a specific conjugation type with the parameters of a conjugation
type, the types of categories being considered and the section in which they
are being considered.
'''
def from_conjugation(conjugation, types, section):
    aves = []
    for i in types: 
        words = categories.loc[categories[section] == i][conjugation].tolist()
        conj_ave = averages
        for col in conj_ave.columns:
            if not any(x in col for x in words):
                conj_ave = conj_ave.drop(col, axis = 1, inplace = False)
        aves.append(conj_ave.mean(axis=1).tolist()[0])

    plt.bar(types, aves)
    plt.ylim(0, 7)
    plt.title(conjugation + ' ' + section)
    plt.xlabel('Consonant Categories')
    plt.ylabel('Average Given Score')
    plt.show()













testing = False

if not testing:
    
    # Indiscriminate-data analysis
    bar_graph(averages, 'All words')

    # Initial consonants analyses:
    for i in initials:
        graph_cat(data, i, 'initial_consonants')

    # Final consonants analyses:
    for i in finals:
        graph_cat(data, i, 'final_consonants')
    
    # Create a comparison graph for all categories under all conjugations
    for i in conjugations:
        from_conjugation(i, initials, 'initial_consonants')
        from_conjugation(i, finals, 'final_consonants')

