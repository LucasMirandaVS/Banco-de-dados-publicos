import wbgapi as wb
import pandas as pd

df1 =  wb.data.DataFrame(['NY.GDP.DEFL.KD.ZG.AD'], 
                    economy = wb.region.members('LCN'), # América Latina e Caribe
                    time=range(1995, 2021),
                    labels = True,
                    skipAggs=True, 
                    skipBlanks=True, 
                    columns='series').reset_index()

df1_1= pd.pivot_table(df1, values='NY.GDP.DEFL.KD.ZG.AD', index = 'economy', columns='time').dropna()

df1_1.to_csv('Inflation, GDP deflator(annual %).csv')
