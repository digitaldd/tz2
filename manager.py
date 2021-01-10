import pandas as pd
import time
import yfinance as yf
import os
from download import download as dd
from trend import trendSort as ts
import patterns


'''
Управляет скачиванием данных, определением тренда и запуском стратегий
'''

timeFrame = {'d': ['60d','1d'], '60m': ['10d','60m'], '30m' : ['10d','30m'], '15m' : ['10d','15m']}
pathList1 = dd(timeFrame.get('d')[0],timeFrame.get('d')[1])
ts(pathList1)
patterns.anyPattern(pathList1[1])
patterns.anyPattern(pathList1[2])
pathList2 = dd(timeFrame.get('60m')[0],timeFrame.get('60m')[1])
ts(pathList2)
patterns.anyPattern(pathList2[1])
patterns.anyPattern(pathList2[2])
pathList3 = dd(timeFrame.get('30m')[0],timeFrame.get('30m')[1])
ts(pathList3)
patterns.anyPattern(pathList3[1])
patterns.anyPattern(pathList3[2])
pathList4 = dd(timeFrame.get('15m')[0],timeFrame.get('15m')[1])
ts(pathList4)
patterns.anyPattern(pathList4[1])
patterns.anyPattern(pathList4[2])