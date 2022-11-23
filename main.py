import camelot
import numpy as np
import pandas as pd
from sklearn import svm

# PDF file to extract tables from
file = "Cardapio\sample.pdf"

# extract all the tables in the PDF file
tables = camelot.read_pdf(file)

# number of tables extracted
print("Total tables extracted:", tables.n)

# print the first table as Pandas DataFrame
print(tables[0].df)

# convert to array
data = []
for i in range(tables.n):
    data.append(tables[i].df.to_numpy())

# Remove comments
train = data[0:4]
test = data[5]
# svm train
y = [0, 0, 1, 1]
clf = svm.SVC()
clf.fit(train, y)

print(np.round(np.clip(clf.predict(test), 0, 1)).astype(bool))  # binary
