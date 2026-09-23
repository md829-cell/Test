# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # pip install numpy on console if you haven't done so
import seaborn as sns
import pandas as pd # pip install pandas on console if you haven't done so
import seaborn as sns
import matplotlib.pyplot as plt

#RUN THIS CELL TO INSTALL THE NEEDED PACKAGES AND LOAD THE DATAFRAME

df = pd.read_csv("AVDS 2026-2027 - Week 3 Data Student Copy")

df.drop('LotArea - delete', axis=1, inplace=True)

