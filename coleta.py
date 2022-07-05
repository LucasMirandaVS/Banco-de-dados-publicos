import wbgapi as wb
import pandas as pd

# Separando os df's 1 a 1
df1 =  wb.data.DataFrame(['NY.GDP.DEFL.KD.ZG.AD'], 
                    economy = wb.region.members('LCN'), # América Latina e Caribe
                    time=range(1995, 2021),
                    labels = True,
                    skipAggs=True, 
                    skipBlanks=True, 
                    columns='series').reset_index()
df1.drop('time', axis=1, inplace=True))
df1.rename(columns={"NY.GDP.DEFL.KD.ZG.AD":"Inflation, GDP deflator: linked series (annual %)"})
df1.to_csv('Inflation, GDP deflator(annual %).csv')

df2 =  wb.data.DataFrame(['NY.GDP.PCAP.CN'],
                    economy = wb.region.members('LCN'),
                    time=range(1995, 2021),
                    labels = True,
                    skipAggs=True, 
                    skipBlanks=True, 
                    columns='series').reset_index()
df2.drop('time', axis=1, inplace=True)
df2.rename(columns={"NY.GDP.PCAP.CN":"GDP per capita"})
df2.to_csv('GDP per Capita.csv')

df3 = wb.data.DataFrame(['SL.GDP.PCAP.EM.KD'],
                    economy = wb.region.members('LCN'), 
                    time=range(1995, 2021),
                    labels = True,
                    skipAggs=True, 
                    skipBlanks=True, 
                    columns='series').reset_index()
df3.drop('time', axis=1, inplace=True)
df3.rename(columns={"SL.GDP.PCAP.EM.KD":'GDP per person employed (constant 2017 PPP $)'})
df3.to_csv('GDP per person employed.csv')

df4 = wb.data.DataFrame(['NY.GDP.MKTP.KD.ZG'], 
                    economy = wb.region.members('LCN'), 
                    time=range(1995, 2021),
                    labels = True,
                    skipAggs=True, 
                    skipBlanks=True, 
                    columns='series').reset_index()
df4.drop('time', axis=1, inplace=True)
df4.rename(columns={"NY.GDP.MKTP.KD.ZG":'GDP growth (annual %)'})
df4.to_csv('GDP growth (annual %).csv')

df5 = wb.data.DataFrame(['NY.GDP.MKTP.CD'], 
                    economy = wb.region.members('LCN'),
                    time=range(1995, 2021),
                    labels = True,
                    skipAggs=True, 
                    skipBlanks=True, 
                    columns='series').reset_index()
df5.drop('time', axis=1, inplace=True)
df5.rename(columns={"NY.GDP.MKTP.CD":"GDP"})
df5.to_csv('GDP.csv')
