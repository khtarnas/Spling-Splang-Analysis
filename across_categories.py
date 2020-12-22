'''
Goal: Create bar graphs for each word conjugation across the different 
categories (initial or final)
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

    # Create a comparison graph for all categories under all conjugations
    for i in conjugations:
        from_conjugation(i, initials, 'initial_consonants')
        from_conjugation(i, finals, 'final_consonants')