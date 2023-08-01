# imports
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dt



tesla_df = pd.read_csv('data/TESLA Search Trend vs Price.csv')
bitcoin_daily = pd.read_csv('data/Daily Bitcoin Price.csv')
bitcoin_df = pd.read_csv('data/Bitcoin Search Trend.csv')
ue_df = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-19.csv')
ue20_df = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-20.csv')

# tesla

tesla_shape = tesla_df.shape
tesla_column = tesla_df.columns
tesla_largest_number = tesla_df["TSLA_WEB_SEARCH"].max()
tesla_df.MONTH = pd.to_datetime(tesla_df.MONTH)

# tesla plot

plt.figure(figsize=(14,8), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)
plt.xticks(fontsize=14, rotation=45)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_ylim(0,700)
ax2.set_ylim(0,40)
ax1.set_xlim([tesla_df.MONTH.min(), tesla_df.MONTH.max()])
plt.xlabel('Date')
ax1.set_ylabel('TSLA Stock price', fontsize = '14',color='skyblue')
ax2.set_ylabel('Searched Trend', fontsize = '14',color="red")

ax1.xaxis.set_major_locator(dt.YearLocator())
ax1.xaxis.set_minor_locator(dt.MonthLocator())

ax1.plot(tesla_df.MONTH,tesla_df.TSLA_USD_CLOSE,color='skyblue',linewidth=3)
ax2.plot(tesla_df.MONTH,tesla_df.TSLA_WEB_SEARCH, "red",linewidth=3)

# bitcoin

bitcoin_shape = bitcoin_df.shape
bitcoin_column = bitcoin_df.columns
bitcoin_largest_number = bitcoin_df["BTC_NEWS_SEARCH"].max()
bitcoin_df.MONTH = pd.to_datetime(bitcoin_df.MONTH)
print(bitcoin_df.BTC_NEWS_SEARCH.max())
bitcoin_daily.dropna(inplace=True)

bitcoin_daily.DATE = pd.to_datetime(bitcoin_daily.DATE)
daily_bitcoin_to_monthly = bitcoin_daily.resample('M', on='DATE').last()
print(daily_bitcoin_to_monthly.CLOSE.max())

# bitcoin plot

plt.figure(figsize=(14,8), dpi=120)
plt.title('Bitcoin News Search vs Resambled Price', fontsize=18)
plt.xticks(fontsize=14, rotation=45)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_ylim(0,15000)
ax2.set_ylim(0,100)
ax1.set_xlim([bitcoin_df.MONTH.min(), bitcoin_df.MONTH.max()])
plt.xlabel('Date')
ax1.set_ylabel('BTC price', fontsize = '14',color='skyblue')
ax2.set_ylabel('Search Trend',fontsize = '14',color="gray")

ax1.xaxis.set_major_locator(dt.YearLocator())
ax1.xaxis.set_minor_locator(dt.MonthLocator())

ax1.plot(daily_bitcoin_to_monthly.index,daily_bitcoin_to_monthly.CLOSE, marker='o',color='skyblue',linewidth=3)
ax2.plot(daily_bitcoin_to_monthly.index,bitcoin_df.BTC_NEWS_SEARCH, linestyle="--",color="blue",linewidth=3)

# ue (2004-19)

ue_shape = ue_df.shape
ue_column = ue_df.columns
ue_largest_number = ue_df["UE_BENEFITS_WEB_SEARCH"].max()
roll_df = ue_df[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
ue_df.MONTH = pd.to_datetime(ue_df.MONTH)

# ue plot(2004-19)

plt.figure(figsize=(14,8), dpi=120)
plt.title('ue', fontsize=18)
plt.xticks(fontsize=14, rotation=45)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_ylim(0,15)
ax2.set_ylim(0,110)
ax1.set_xlim([ue_df.MONTH.min(), ue_df.MONTH.sort_values(ascending=True)[:-2].max()])
plt.xlabel('Date')
ax1.set_ylabel('Unrate', fontsize = '14',color='skyblue')
ax2.set_ylabel('Web Search',fontsize = '14',color="blue")
ax1.grid(color='grey', linestyle='--')

ax1.xaxis.set_major_locator(dt.YearLocator())
ax1.xaxis.set_minor_locator(dt.MonthLocator())

ax1.plot(ue_df.MONTH,ue_df.UNRATE, marker='o',color='skyblue',linewidth=3)
ax2.plot(ue_df.MONTH,ue_df.UE_BENEFITS_WEB_SEARCH, linestyle="--",color="blue",linewidth=3)

# rolling 6mont ue(2004-19)

plt.figure(figsize=(14,8), dpi=120)
plt.title('Rolled eu', fontsize=18)
plt.xticks(fontsize=14, rotation=45)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_ylim(0,15)
ax2.set_ylim(0,110)
ax1.set_xlim([ue_df.MONTH.min(), ue_df.MONTH.sort_values(ascending=True)[:-2].max()])
plt.xlabel('Date')
ax1.set_ylabel('Unrate', fontsize = '14',color='skyblue')
ax2.set_ylabel('Web Search',fontsize = '14',color="blue")
ax1.grid(color='grey', linestyle='--')

ax1.xaxis.set_major_locator(dt.YearLocator())
ax1.xaxis.set_minor_locator(dt.MonthLocator())

ax1.plot(ue_df.MONTH,roll_df.UNRATE, marker='o',color='skyblue',linewidth=3)
ax2.plot(ue_df.MONTH,roll_df.UE_BENEFITS_WEB_SEARCH, linestyle="--",color="blue",linewidth=3)


# ue(2004-20)
ue20_df.MONTH = pd.to_datetime(ue20_df.MONTH)

plt.figure(figsize=(14,8), dpi=120)
plt.title('eu 2004-20', fontsize=18)
plt.xticks(fontsize=14, rotation=45)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_ylim(0,15)
ax2.set_ylim(0,110)
ax1.set_xlim([ue20_df.MONTH.min(), ue20_df.MONTH.max()])
plt.xlabel('Date')
ax1.set_ylabel('Unrate', fontsize = '14',color='skyblue')
ax2.set_ylabel('Web Search',fontsize = '14',color="blue")
ax1.grid(color='grey', linestyle='--')

ax1.xaxis.set_major_locator(dt.YearLocator())
ax1.xaxis.set_minor_locator(dt.MonthLocator())

ax1.plot(ue20_df.MONTH,ue20_df.UNRATE, marker='o',color='skyblue',linewidth=3)
ax2.plot(ue20_df.MONTH,ue20_df.UE_BENEFITS_WEB_SEARCH, linestyle="--",color="blue",linewidth=3)


