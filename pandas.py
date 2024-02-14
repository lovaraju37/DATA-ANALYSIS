# -*- coding: utf-8 -*-
"""Pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jPSC-WBrHVj2qss9JsZGWFDQrkpTlVS1
"""

#importing pandas
import pandas as pd

a=['Mahesh','farhan','Akhil','Sai','Kamal','Gafoor','lova']
r=pd.Series(a,index=[39,36,35,16,8,57,44])
print(r)

#read csv file and text file
import pandas as pd
import numpy as np
data=pd.read_csv("/tableConvert.com_gyhh6h.csv")
#print(data)
data.shape
#data1=pd.read_csv("/content/Player.csv")
#print(data1)
#printing one row as series
#print(data.loc[1])
#shape()
data.shape
data_manual=data.tail(9)
for i in range(1,10,-1):
  data.drop([i],axis=0,inplace=True)
data_manual=pd.concat([data],axis=0)
data_manual.to_csv("Last_10_lines_csv")

#read XLSX file
import pandas as pd
data=pd.read_excel("/content/salesworkload.xlsx",sheet_name=1)
print(data)

from google.colab import drive
drive.mount('/content/drive')

#Taking 10 values for manual testing
data_testing=data.tail(10)
for i in range(21416,21416,-1):
  data.drop([i],axis=0,implace=True)

#concatination
import pandas as pd
import numpy as np
data=pd.read_csv("/content/tableConvert.com_gyhh6h.csv")
data.shape
data_manual=data.tail(9)
for i in range(1,0,-1):
  data.drop([i],axis=0,inplace=True)
data_manual=pd.concat([data],axis=0)
data_manual.to_csv("Last_10_lines_csv")

#groupby()
print(data_manual.groupby(['sum'])['Average'].count())

#Plotting of graph using "matplotlib.pyplot"
import numpy as np
import matplotlib.pyplot as plt
runs=np.array([100,50,91,78,89,25,34,19,9,10])
w=np.array([1,0,2,0,3,7,8,9,7,5])
plt.scatter(runs,w,color='blue')
plt.title('IndvsAus_score')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
#Generate array of 200 values between -pi & pi
tiger=np.linspace(-2*np.pi,2*np.pi,100)
print(tiger)

plt.plot(tiger,np.sin(tiger),color='black')#SIN plt.plot(x,y,,color,label....)
plt.title("sin(x)")
#Display plot
plt.show()

#pie chart
import numpy as np
import matplotlib.pyplot as plt
a=np.array([25,60,5,10])
labe=["AIML","PYTHON","PANDAS","NUMPY"]
explo=[0.2,0,0,0] #explode
plt.pie(a, labels=labe, explode=explo, startangle=180,textprops={'fontsize':44})
plt.show()

import numpy as np
import matplotlib.pyplot as plt
#creating x
overs=np.arange(5,50,5)
overs_a=np.arange(5,30,5)
#creating y
runs_i=np.array([25,51,84,131,160,189,220,250,267])
runs_a=np.array([15,41,94,100,151])
wickets=np.array([12,32,96])
#plotting
plt.plot(overs,runs_i,color='blue',label='India')
plt.plot(overs_a,runs_a,color='yellow',label='Aus')
#combining two graphs
plt.legend(loc='best')
#displaying the final graph
plt.show()

#subplot
import numpy as np
import matplotlib.pyplot as plt

a=[230,560,780,127,128]
b=[200,160,270,127,400]
years=[1,2,3,4]
profit_a=[(a[i]-a[i-1]) for i in range(1,len(a))]
profit_b=[(b[i]-b[i-1]) for i in range(1,len(b))]
plt.subplot(2,1,2)
plt.plot(years,profit_a,color='hotpink',linewidth='3',label='companyA',marker='+',ms='15',mec='k')
plt.legend(loc='best')
plt.subplot(2,1,1)
plt.plot(years,profit_b,color='black',linestyle='dotted',label='companyB',marker='*')
plt.legend(loc='best')
plt.show()

#Task1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load the dataset containing daily temperatures
# Assuming the dataset is in a CSV file named 'temperature_data.csv' with a column named 'temperature'
df = pd.read_csv('/content/city_temperature.csv')
print(df)


average_temperature = df['AvgTemperature'].mean()
highest_temperature = df['AvgTemperature'].max()
lowest_temperature = df['AvgTemperature'].min()
threshold = 30
days_above_threshold = df[df['AvgTemperature'] > threshold].shape[0]


print("Average temperature for the month:", average_temperature)
print("Highest temperature recorded:", highest_temperature)
print("Lowest temperature recorded:", lowest_temperature)
print("Number of days where temperature exceeded", threshold, "degrees Celsius:", days_above_threshold)
b.plot(kind='line',color='blue')
plt.title("Temperature for 50 days")
plt.xlabel("Days")
plt.ylabel("Temperature")