import csv
from collections import Counter
import pandas as pd
import plotly.express as px

with open('class1.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
total_marks = 0
total_entries = len(file_data)
for marks in file_data:
    total_marks += float(marks[1])
mean = total_marks/total_entries
#print(mean)
print("Mean (Average) is -> "+str(mean))

df = pd.read_csv("class1.csv")
fig = px.scatter(df, x = "Student Number", y = "Marks") 
fig.show()