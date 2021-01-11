import pandas as pd
import talib
import numpy as np
import os
import addPlot
import candles
pd.options.mode.chained_assignment = None # отключение уведомлений

def tickers (folder):
    return list(filter(lambda x: x.endswith('.csv'), os.listdir(folder)))

def trendUpRed(df): #восходящий тренд красный пин бар
    flag1 = False
    flag2 = False
    flag3 = False
    candle1 = candles.Candle(df[-3:-2])
    candle2 = candles.Candle(df[-2:-1])
    candle3 = candles.Candle(df[-1:])
    if (candle1.Green > 0) & (candle1.bodyGreen >= 0.7):
        flag1 = True
        if list(candle2.PatternRedHighShadow)[0] & (candle2.High > candle1.High) & (candle2.Close >= candle1.Close) & (candle2.Low > (((float(candle1.High) - float(candle1.Low)) / 2) + candle1.Low)):
            flag2 = True
            if (candle3.Red > 0) & (candle3.Close <= candle1.Open) & (candle3.Open <= candle2.Close):
                flag3 = True
    return flag1 & flag2 & flag3

def trendUpGreen(df): #восходящий тренд зеленый пин бар
    flag1 = False
    flag2 = False
    flag3 = False
    candle1 = candles.Candle(df[-3:-2])
    candle2 = candles.Candle(df[-2:-1])
    candle3 = candles.Candle(df[-1:])
    if (candle1.Green > 0) & (candle1.bodyGreen >= 0.7):
        flag1 = True
        if list(candle2.PatternGreenHighShadow)[0] & (candle2.High > candle1.High) & (candle2.Open >= candle1.Close) & (candle2.Close > candle1.Low):
            flag2 = True
            if (candle3.Red > 0) & (candle3.Open <= candle2.Open) & (candle3.Close <= candle1.Open):
                flag3 = True
    return flag1 & flag2 & flag3

def trendDownRed(df): #нисходящий тренд красный пин бар
    flag1 = False
    flag2 = False
    flag3 = False
    candle1 = candles.Candle(df[-3:-2])
    candle2 = candles.Candle(df[-2:-1])
    candle3 = candles.Candle(df[-1:])
    if (candle1.Red > 0) & (candle1.bodyRed >= 0.7):
        flag1 = True
        if list(candle2.PatternRedBottomShadow)[0] & (candle2.Close <= candle1.Low) & (candle2.Low < candle1.Low) & (candle2.Open <= (((candle1.Open-candle1.Close) * 0.85) + candle1.Close)):
            flag2 = True
            if (candle3.Green > 0) & (candle3.Close > candle2.High) & (candle3.Open >= ((candle2.Close-(candle2.Open-candle2.Close)*0.85))) & (candle3.Low > candle2.Low):
                flag3 = True
    return flag1 & flag2 & flag3

def trendDownGreen(df): #нисходящий тренд зеленый пин бар
    flag1 = False
    flag2 = False
    flag3 = False
    candle1 = candles.Candle(df[-3:-2])
    candle2 = candles.Candle(df[-2:-1])
    candle3 = candles.Candle(df[-1:])
    if (candle1.Red > 0) & (candle1.bodyRed >= 0.7):
        flag1 = True
        if list(candle2.PatternGreenBottomShadow)[0] & (candle2.High <= (((float(candle1.High) - float(candle1.Low)) / 2)+candle1.Low)) & (candle2.Close <= ((candle1.Open-candle1.Close)*0.85) + candle1.Close) & (candle2.Open < candle1.Low) & (candle2.Low < candle1.Low):
            flag2 = True
            if (candle3.Green > 0) & (candle3.Close > candle2.High) & (candle3.Open >= (candle2.Open -((candle2.Close - candle2.Open) * 0.85))) & (candle3.Low > candle2.Low):
                flag3 = True
    return flag1 & flag2 & flag3


def anyPattern(folder):
    ticks = tickers(folder)
    for i in ticks:
        df = pd.read_csv(folder + '/' + i)
        if 'Date' not in df: #на мелких тф колонка называется Datetime
            df.rename(columns={'Datetime':'Date'}, inplace=True)
            df.rename(columns={'Unnamed: 0': 'Date'}, inplace=True)
        if (trendUpRed(df) | trendUpGreen(df) | trendDownRed(df) | trendDownGreen(df)):
            print(str(i)[:-4])
            df['signal'] = np.nan
            df.signal[-2:-1] = float(df.High[-2:-1]) * 1.01 #отметка свечи
            addPlot.mplot(df, df.signal, str(i)[:-4], folder)

folder1 = '/home/linac/Рабочий стол/data/20210107_10d30m/'
anyPattern(folder1)