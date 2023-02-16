import csv
import cleaning
import webscraping
import pandas as pd
import matplotlib
import numpy as np
import csv
import matplotlib.pyplot as plt

#Grupby Make Brands
file=pd.read_csv('cleandata.csv')
uniq=file.Make.unique()
for i in uniq:
    dataFrame = file[file['Make'].str.contains(i)]
    with open(f'{i}.txt', 'w', newline='') as f:
        writer = csv.writer(f)

        writer.writerow([dataFrame])

