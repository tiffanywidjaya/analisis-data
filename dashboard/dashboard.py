import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day = pd.read_csv('dashboard/day.csv')
hour = pd.read_csv('dashboard/hour.csv')

st.title('Bike Sharing Analysis Dashboard')

st.header('Jumlah Penyewaan Sepeda per Hari')
fig1, ax1 = plt.subplots(figsize=(12,6))
sns.lineplot(data=day, x='dteday', y='cnt', ax=ax1)
ax1.set_xlabel('Tanggal')
ax1.set_ylabel('Jumlah Penyewaan')
ax1.set_title('Jumlah Penyewaan Sepeda Harian')
st.pyplot(fig1)

st.header('Rata-rata Penyewaan Sepeda per Jam')
workday = hour[hour['workingday'] == 1]
holiday = hour[hour['workingday'] == 0]
workday_avg = workday.groupby('hr')['cnt'].mean()
holiday_avg = holiday.groupby('hr')['cnt'].mean()

fig2, ax2 = plt.subplots(figsize=(12,6))
sns.lineplot(x=workday_avg.index, y=workday_avg.values, label='Hari Kerja', ax=ax2)
sns.lineplot(x=holiday_avg.index, y=holiday_avg.values, label='Hari Libur', ax=ax2)
ax2.set_xlabel('Jam')
ax2.set_ylabel('Rata-rata Jumlah Penyewa')
ax2.set_title('Pola Penyewaan Sepeda per Jam')
ax2.legend()
st.pyplot(fig2)