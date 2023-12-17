import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from datetime import timedelta

def time_to_seconds(time):
    return time.dt.hour * 3600 + time.dt.minute * 60 + time.dt.second

def seconds_to_time(seconds):
    return str(timedelta(seconds=seconds))

df = pd.read_csv("C:/Users/holge/OneDrive/Desktop/PythonKurs/PythonUdemyTutorial/Teil7_Data/DataToAnalyze.csv", delimiter=";")

df['Datum'] = pd.to_datetime(df['Datum'])

df['Wochenendtag'] = df['Datum'].dt.dayofweek.isin([5,6])

plt.figure(figsize=(18,8))

ax1 = sns.scatterplot(data=df, x="Datum", y=time_to_seconds(df['Datum']), hue='Wochenendtag', s=60)
ax1.set_xlabel("Datum")
ax1.set_ylabel("Uhrzeit")

ax1.xaxis.set_major_locator(mdates.DayLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m'))

ax1.set_yticks(range(0,24*3600,2*3600))
ax1.set_yticklabels([seconds_to_time(x) for x in range(0, 24*3600, 2*3600)])

ax1.legend().set_visible(False)

plt.show()
