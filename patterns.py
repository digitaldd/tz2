import pandas as pd
import talib
import numpy as np
import os
import addPlot
import candles
pd.options.mode.chained_assignment = None # отключение уведомлений

def tickers (folder):
    return list(filter(lambda x: x.endswith('.csv'), os.listdir(folder)))
'''
def hammer(df):
    df1 = df.copy()
    df1['ham'] = talib.CDLHAMMER(df1.Open,df1.High, df1.Low, df1.Close)
    df1.loc[df1.ham == 0] = np.nan
    df1.ham = df1.loc[(df1.ham == 100) | (df1.ham == - 100),'High'] * 1.01
    return list(df1.ham)
    #return [np.nan if i==False else 100 for i in list(talib.CDLHAMMER(df.Open,df.High, df.Low, df.Close))] # молот

def man(df):
    df1 = df.copy()
    df1['man'] = talib.CDLHANGINGMAN(df1.Open, df1.High, df1.Low, df1.Close)
    df1.loc[df1.man == 0] = np.nan
    df1.man = df1.loc[(df1.man == 100) | (df1.man == - 100), 'High'] * 1.01
    return list(df1.man)

def anyPattern(folder):
    ticks = tickers(folder)
    for i in ticks:
        df = pd.read_csv(folder + '/' + i)  # , index_col=0, parse_dates=True)
        #if df.Volume[0] >= int(df.loc[:60].Volume.mean()) * 2:
        if True:
            manRes = man(df)
            if str(manRes[-1]).count('nan') == 0 :
                print("man", manRes[-1])
                try:
                    df.index = pd.to_datetime(df.Date) #на дневном Date!!!
                    df.drop(['Date'], axis = 'columns', inplace = True)
                except: pass
                try:
                    df.index = pd.to_datetime(df.Datetime)
                    df.drop(['Datetime'], axis='columns', inplace=True)
                except: pass
                addPlot.mplot(df,manRes,str(i)[:-4],folder, 'Повешенный')

            hamRes = hammer(df)
            if str(hamRes[-1]).count('nan') == 0:
                print("ham", hamRes[-1])
                try: # если ранее уже был изменен индекс на дату, здесь будет исключение
                    df.index = pd.to_datetime(df.Date)
                    df.drop(['Date'], axis='columns', inplace=True)
                except: pass
                try:
                    df.index = pd.to_datetime(df.Datetime)
                    df.drop(['Datetime'], axis='columns', inplace=True)
                except: pass
                addPlot.mplot(df,hamRes,str(i)[:-4],folder,'Молот')
    #patterns = {'Молот':'CDLHAMMER', 'Повешенный':'CDLHANGINGMAN'}

#folder1 = '/home/linac/Рабочий стол/data/20201224_10d60m/down/'
#anyPattern(folder1)
'''

def anyPattern(folder):
    ticks = tickers(folder)
    for i in ticks:
        df = pd.read_csv(folder + '/' + i)  # , index_col=0, parse_dates=True)
        if 'Date' not in df: # на мелких тф колонка называется Datetime
            df.rename(columns={'Datetime':'Date'}, inplace=True)
        candle = candles.Candle(df)
        try:
            if int(df[-1:].Volume) >= int(df.loc[:60].Volume.mean()) * 1.5: # объем + нижний хвост
                if str(folder).__contains__('down'):
                    df3 = df.loc[candle.Green & (candle.bottomShadowGreen >= 0.6) & (candle.bodyGreen >= 0.2)] # нижний хвост
                    df4 = df.loc[candle.Red & (candle.bottomShadowRed >= 0.6) & (candle.bodyRed >= 0.2)]
                else: # верхний хвост
                    df3 = df.loc[candle.Green & (candle.highShadowGreen >= 0.6) & (
                                candle.bodyGreen >= 0.2)]  # зеленая свеча с верхним хвостом
                    df4 = df.loc[candle.Red & (candle.highShadowRed >= 0.6) & (
                                candle.bodyRed >= 0.2)]  # красная свеча с верхним хвостом
                if (str(df[-1:].Date) == str(df3[-1:].Date)) | (str(df[-1:].Date) == str(df4[-1:].Date)):
                    print(str(i)[:-4])
                    df['signal'] = np.nan
                    df.signal[-1:]= float(df.High[-1:]) * 1.01
                    addPlot.mplot(df, df.signal, str(i)[:-4], folder)
        except: pass

#folder1 = '/home/linac/Рабочий стол/data/20210107_10d60m/up/'
#anyPattern(folder1)