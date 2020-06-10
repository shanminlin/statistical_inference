#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy.stats import norm



df = pd.read_csv('data/data_without_difference.csv')

convert_old = df[df['group'] == 'control']['convert'].sum()
convert_new = df[df['group'] == 'treatment']['convert'].sum()

n_new = len(df[df['group'] == 'treatment'])
n_old = len(df[df['group'] == 'control'])

z_score, p_value = sm.stats.proportions_ztest([convert_old, convert_new], [n_old, n_new], alternative='smaller')

print('z_score: {}, p_value: {}'.format(z_score, p_value))
print('Significance of z-score: {}'.format(norm.cdf(z_score))) 
print('Critical value: {}'.format(norm.ppf(1-(0.05)))) 
    
