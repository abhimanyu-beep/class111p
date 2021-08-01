import pandas as p 
import csv 
import plotly.figure_factory as ff
import statistics 
import random 
import plotly.graph_objects as go 
df=p.read_csv("medium.csv")
data=df["title"].tolist()
def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
meanlist=[]
for i in range(0,1000):
    setofmean=randomsetofmean(100)
    meanlist.append(setofmean)
mean=statistics.mean(meanlist)
print(mean)
sd1=statistics.stdev(meanlist)
print(sd1)
fsdstart,fsdend=mean-sd1,mean+sd1
ssdstart,ssdend=mean-(2*sd1),mean+(2*sd1)
thsdstart,thsdend=mean-(3*sd1),mean+(3*sd1)
print("sd1",fsdstart,fsdend)
print("sd2",ssdstart,ssdend)
print("sd3",thsdstart,thsdend)
df=p.read_csv("sample1.csv")
data=df["title1"].tolist()
mean1=statistics.mean(data)
print(mean1)
figure=ff.create_distplot([meanlist],["title1"],show_hist=False)
figure.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
figure.add_trace(go.Scatter(x=[mean1,mean1],y=[0,0.17],mode="lines",name="meanofstudents who had math labs"))
figure.add_trace(go.Scatter(x=[fsdend,fsdend],y=[0,0.17],mode="lines",name="fsdend"))
figure.add_trace(go.Scatter(x=[ssdend,ssdend],y=[0,0.17],mode="lines",name="ssdend"))
figure.add_trace(go.Scatter(x=[thsdend,thsdend],y=[0,0.17],mode="lines",name="thsdend"))
figure.show()

df=p.read_csv("sample2.csv")
data=df["title2"].tolist()
mean2=statistics.mean(data)
print(mean2)
figure=ff.create_distplot([meanlist],["title2"],show_hist=False)
figure.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
figure.add_trace(go.Scatter(x=[mean2,mean2],y=[0,0.17],mode="lines",name="meanofstudents who had math labs"))
figure.add_trace(go.Scatter(x=[fsdend,fsdend],y=[0,0.17],mode="lines",name="fsdend"))
figure.add_trace(go.Scatter(x=[ssdend,ssdend],y=[0,0.17],mode="lines",name="ssdend"))
figure.add_trace(go.Scatter(x=[thsdend,thsdend],y=[0,0.17],mode="lines",name="thsdend"))
figure.show()
zscore=(mean-mean2)/sd1
print("zscore",zscore)





