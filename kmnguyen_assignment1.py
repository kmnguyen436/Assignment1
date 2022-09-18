#-------------------------------------------------------------------------
# AUTHOR:  Kayla Nguyen
# FILENAME: contact_lens.cvs
# SPECIFICATION: This program reads in a csv file and outputs a decision tree
# FOR: CS 4210- Assignment #1
# TIME SPENT: It took me 2 hours to complete this assignment.
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original categorical training features to numbers and add to the 4D array X.
#For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
# my code
category_dict = {
    "Young": 1,
    "Prepresbyopic": 2,
    "Presbyopic": 3,
    "Myope": 1,
    "Hypermetrope": 2,
    "Yes": 1,
    "No": 2,
    "Reduced": 1,
    "Normal": 2
}

X = [[category_dict[db[row][col]] for col in range(len(db[row]) - 1)] for row in range(len(db))]


#transform the original categorical training classes to numbers and add to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#my code
Y = [category_dict[db[row][col]] for row in range(len(db)) for col in range(len(db[row])-1,len(db[row]))]


#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion='entropy', )
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()

