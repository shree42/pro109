import plotly.figure_factory as ff
import random
import statistics
import plotly.graph_objects as go
import pandas as pd

df=pd.read_csv('data.csv')
rdscore=df["reading score"].tolist()

mean=statistics.mean(rdscore)
std=statistics.stdev(rdscore)

firstStdStart,firstStdEnd=mean-std,mean+std
secondStdStart,secondStdEnd=mean-(std*2),mean+(std*2)
thirdStdStart,thirdStdEnd=mean-(std*3),mean+(std*3)

amnt_of_heightdata_in_std1=[result for result in rdscore if result>firstStdStart and result<firstStdEnd]
amnt_of_heightdata_in_std2=[result for result in rdscore if result>secondStdStart and result<secondStdEnd]
amnt_of_heightdata_in_std3=[result for result in rdscore if result>thirdStdStart and result<thirdStdEnd]

print(std)

print("Percentage of data lies in first standard deviation",len(amnt_of_heightdata_in_std1)*100.0/len(rdscore))
print("Percentage of data lies in second standard deviation",len(amnt_of_heightdata_in_std2)*100.0/len(rdscore))
print("Percentage of data lies in third standard deviation",len(amnt_of_heightdata_in_std3)*100.0/len(rdscore))