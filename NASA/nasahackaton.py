import pandas as pd
import seaborn as sns
import matplotlib.pyplot as ptl
from scipy import stats
import pylab
import scipy.stats as stats
import os
from scipy.stats import normaltest
from statsmodels.stats.diagnostic import lilliefors

df = pd.read_csv('PAR_A01_2018_Inventory.csv', sep=",")

medianHcom = df.Hcom.median()
df.Hcom.fillna(medianHcom, inplace=True)

medianHtot = df.Htot.median()
df.Htot.fillna(medianHtot, inplace=True)

df.Hcom.replace('NA',medianHcom)
df.Htot.replace('NA',medianHtot)