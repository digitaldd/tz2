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

timeFrame = {'Дневной': ['60d','1d'], 'Часовой': ['10d','60m'], 'Получасовой' : ['10d','30m']}
pathList1 = dd(timeFrame.get('Дневной')[0],timeFrame.get('Дневной')[1])
ts(pathList1)
patterns.anyPattern(pathList1[1])
patterns.anyPattern(pathList1[2])
pathList2 = dd(timeFrame.get('Часовой')[0],timeFrame.get('Часовой')[1])
ts(pathList2)
patterns.anyPattern(pathList2[1])
patterns.anyPattern(pathList2[2])
pathList3 = dd(timeFrame.get('Получасовой')[0],timeFrame.get('Получасовой')[1])
ts(pathList3)
patterns.anyPattern(pathList2[1])
patterns.anyPattern(pathList2[2])