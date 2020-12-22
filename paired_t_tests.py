'''
Plan: We will calculate the pairwise t value for each intra-category comparison
      (e.g. for the category of the initial sCC, we will calculate three t 
      values: -ed vs. -a-, -a- vs. -u-, and -u- vs. -ed)
'''
# Import libraries
import pandas as pd
import math

# Import data
categories = pd.read_excel('word_categories.xlsx')
data = pd.read_excel('responses.xlsx')
data = data.drop(data.columns[0:3], axis = 1, inplace = False) #remove unnecessary columns

# Important categories
conj_labels = ['A. Labels', 'B. Labels', 'C. Labels']
conjugations = ['"-ed"', '"/æ/"', '"/ʌ/"']
pairs = [(0, 1), (1, 2), (2, 0)]
initials = ['sCC', 'sC', 'CC', 'C']
finals = ['nasal', 'k/g', 'n/m', 'C']

# for every participant I have to average their -u- scores per category and compare it 
# find two values, find the difference btwn the two, calculate the means of all these
# differences. Calculate the t statistic. Confidence interval as well

# get a data frame of just words in the category we want
# make a data frame of only the difference between -ed and u (and for the other comparison)

# sCC initials, differences between -ed and u for each word in cat and each person,
# average across words per person then get the mean, sample size, and standard deviation

# Two different ones: one averages all before scores for a particular person and the after
# scores. one finds the difference for all words across all people, treats all of these as
# counting towards the sample size then calculates it.

def find_t(data, category, section, first_conj, second_conj):
    x = categories.loc[categories[section] == category]
    words = x[first_conj].tolist() + x[second_conj].tolist()

    cat_data = data
    for col in cat_data.columns:
        if not col in words:
            cat_data = cat_data.drop(col, axis = 1, inplace = False)
    
    differences = pd.DataFrame() #df containing all differences across words and people
    for i in range(0, len(cat_data.columns), 2):
        differences[cat_data.columns[i]] = cat_data[cat_data.columns[i]] - cat_data[cat_data.columns[i+1]]
    
    sample_size = len(differences.stack())
    mean = differences.stack().mean()
    std = differences.stack().std()
    t_value = abs(mean / (std*math.sqrt(sample_size)))
    file.write('\n' + 't-statistic: '+ str(t_value) + '\n')
    file.write('Significant with p-value of 0.05: ' + str(t_value < 0.05) + '\n')
    file.write('Significant with p-value of 0.01: ' + str(t_value < 0.01) + '\n')
    

file = open("t_values.txt", "w")

#pd.set_option("display.max_rows", None, "display.max_columns", None)
for i in pairs:
    file.write("Comparing the conjugations " + conjugations[i[0]] + ' and ' + conjugations[i[1]] + ':' + '\n')
    first = conj_labels[i[0]]
    second = conj_labels[i[1]]

    # Initial consonants analyses:
    for i in initials:
        file.write('\n' + 'Initial Consonant of ' + i + ':')
        find_t(data, i, 'initial_consonants', first, second)

    # Final consonants analyses:
    for i in finals:
        file.write('\n' + 'Final Consonant of ' + i + ':')
        find_t(data, i, 'final_consonants', first, second)

    file.write('\n')

file.close()