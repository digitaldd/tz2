import pandas as pd
import numpy as np

class Candle():
    def __init__(self, df1):
        df = df1
        self.Low = df.Low
        self.Open = df.Open
        self.High = df.High
        self.Close = df.Close
        self.Volume = df.Volume
        self.Green = (df.Close - df.Open) > 0
        self.Red = (df.Open - df.Close) > 0
        self.bottomShadowGreen = (df.Open - df.Low) / (df.High - df.Low)
        self.bottomShadowRed = (df.Close - df.Low) / (df.High - df.Low)
        self.highShadowGreen = (df.High - df.Close) / (df.High - df.Low)
        self.highShadowRed = (df.High - df.Open) / (df.High - df.Low)
        self.bodyGreen = (df.Close - df.Open ) / (df.High - df.Low)
        self.bodyRed = (df.Open - df.Close ) / (df.High - df.Low)
'''
def candlePattern (df):
    df["index"] = np.arange(len(df)) # Добавляем индекс колонку
    candle = Candle(df)
    df3 = df.loc[candle.Green & (candle.bottomShadowGreen >= 0.6) & (candle.bodyGreen >= 0.2)] # зеленая свеча с нижним хвостом
    df4 = df.loc[candle.Red & (candle.bottomShadowRed >= 0.6) & (candle.bodyRed >= 0.2)] # красная свеча с нижним хвостом
    
    df5 = df.loc[candle.Green & (candle.highShadowGreen >= 0.6) & (candle.bodyGreen >= 0.2)] # зеленая свеча с верхним хвостом
    df6 = df.loc[candle.Red & (candle.highShadowRed >= 0.6) & (candle.bodyRed >= 0.2)] # красная свеча с верхним хвостом

    df2 = df[1:]# == candle.bodyRed>0

    df['signal'] = candle.Red & (candle.bottomShadowRed >= 0.6) & (candle.bodyRed >= 0.2)
    #df.signal[df.signal == False] = np.nan
    df.signal[:-1] = np.nan
    df.signal[-1:] = df.High[-1:] * 1.01
    print(df)
    #if len(df3) > 0:
     #   print(df.loc[df3])
      #  print(df[1:2])

df = pd.read_csv('/home/linac/Рабочий стол/data/SPY.csv')

'''
#candlePattern(df)
