'''
Goal: Create bar graphs for each word category across the three different 
      conjugation options.
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
    plt.ylabel('Mean Score')
    plt.show()
    #plt.savefig(title)


'''
Function that takes in category names and the section in which the category is
applicable (e.g. 'initial_consonants) and makes a bar graph.
'''
def graph_cat(data, category, section, title):
    x = categories.loc[categories[section] == category]
    words = x['A. Labels'].tolist() + x['B. Labels'].tolist() + x['C. Labels'].tolist()
    
    cat_averages = averages
    for col in cat_averages.columns:
        if not col in words:
            cat_averages = cat_averages.drop(col, axis = 1, inplace = False)

    bar_graph(cat_averages, title)


testing = False

if not testing:
    
    # Indiscriminate-data analysis
    bar_graph(averages, 'All words')

    # Initial consonants analyses:
    for i in initials:
        title = 'Initial Consonant Set of ' + i
        graph_cat(data, i, 'initial_consonants', title)

    # Final consonants analyses:
    for i in finals:
        title = 'Final Consonant Set of '
        if i == 'nasal':
            title += 'ŋ/ŋk'
        else:
            title += i

        graph_cat(data, i, 'final_consonants', title)