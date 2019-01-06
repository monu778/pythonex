import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Referred from https://www.datacamp.com/community/tutorials/web-scraping-using-python
url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
print (type(soup))

title = soup.title
print(title)

text = soup.get_text()
#print(soup.text)
all_links = soup.find_all('a')
for link in all_links:
    print(link.get("href"))

rows = soup.find_all('tr')
#print(rows[:10])
list_rows = []
for row in rows:
    row_td = row.find_all('td')
    #print(row_td)
    #print(type(row_td))
    str_cells = str(row_td)
    cleantext = BeautifulSoup(str_cells, "lxml").get_text()
    list_rows.append(cleantext)    

#print(list_rows)
df = pd.DataFrame(list_rows)
print(df.head(10))
#print(df[0])
df1 = df[0].str.split(',', expand=True)
print(df1.head(10))
df1[0] = df1[0].str.strip('[')
print(df1.head(10))
col_labels = soup.find_all('th')
all_header = []
col_str = str(col_labels)
cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
all_header.append(cleantext2)
print(all_header)
df2 = pd.DataFrame(all_header)
df3 = df2[0].str.split(',', expand=True)
print(df3.head())
frames = [df3, df1]

df4 = pd.concat(frames)
df4.head(10)
#first row to table header
df5 = df4.rename(columns=df4.iloc[0])
df5.head()

df5.info()
df5.shape
#You can drop all rows with any missing values.
df6 = df5.dropna(axis=0, how='any')
#table header is replicated as the first row in df5. It can be dropped using the following line of code.
df7 = df6.drop(df6.index[0])
df7.head()
df7.rename(columns={'[Place': 'Place'},inplace=True)
df7.rename(columns={' Team]': 'Team'},inplace=True)
df7.head()

df7['Team'] = df7['Team'].str.strip(']')
print(df7.head())

time_list = df7[' Chip Time'].tolist()

# You can use a for loop to convert 'Chip Time' to minutes

time_mins = []
for i in time_list:
    h, m, s = i.split(':')
    math = (int(h) * 3600 + int(m) * 60 + int(s))/60
    time_mins.append(math)

df7['Runner_mins'] = time_mins
df7.head()
#to calculate statistics for numeric columns only in the dataframe.
df7.describe(include=[np.number])

df7.boxplot(column='Runner_mins')
plt.grid(True, axis='y')
plt.ylabel('Chip Time')
plt.xticks([1], ['Runners'])
plt.show()
#Did the runners' finish times follow a normal distribution?
x = df7['Runner_mins']
ax = sns.distplot(x, hist=True, kde=True, rug=False, color='m', bins=25, hist_kws={'edgecolor':'black'})
plt.show()
#whether there were any performance differences between males and females of various age groups. 
# Below is a distribution plot of chip times for males and females.

f_fuko = df7.loc[df7[' Gender']==' F']['Runner_mins']
m_fuko = df7.loc[df7[' Gender']==' M']['Runner_mins']
sns.distplot(f_fuko, hist=True, kde=True, rug=False, hist_kws={'edgecolor':'black'}, label='Female')
sns.distplot(m_fuko, hist=False, kde=True, rug=False, hist_kws={'edgecolor':'black'}, label='Male')
plt.legend()
#You can use the groupby() method to compute summary statistics for males and females separately
g_stats = df7.groupby(" Gender", as_index=True).describe()
print(g_stats)
#a side-by-side boxplot comparison of male and female finish times.
f7.boxplot(column='Runner_mins', by=' Gender')
plt.ylabel('Chip Time')
plt.suptitle("")
