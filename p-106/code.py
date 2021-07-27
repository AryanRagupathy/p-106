import plotly.express as px
import csv
import pandas as pd


df=pd.read_csv("data2.csv")
fig=px.scatter(df,x="Days Present",y="Marks In Percentage")
fig.show() 

df2=pd.read_csv("data.csv")
fig2=px.line(df2,x="sleep in hours",y="Coffee in ml")
fig2.show()
