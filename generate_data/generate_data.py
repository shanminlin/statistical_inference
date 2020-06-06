# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import random

# set seed to replicate
# np.random.seed(0)

def generate_conversion_data(size, p_control, p_treatment):
    """Generate user conversion data for control and treatment groups"""
    convert_control = np.random.binomial(size=size//2, p=p_control, n=1)
    convert_treatment = np.random.binomial(size=size//2, p=p_treatment, n=1)
    
    # Create control and treatment data
    control_data = pd.DataFrame()
    control_data['convert'] = convert_control
    control_data['group'] = 'control'
    treatment_data = pd.DataFrame()
    treatment_data['convert'] = convert_treatment
    treatment_data['group'] = 'treatment'
    
    # Combine control and treatment data
    data = pd.concat([control_data, treatment_data], axis=0)
    
    # Generate unique integer ids, Sample without replacement,
    ids = random.sample(range(1, size+1), size)
    data['user_id'] = ids
    
    # Rearange columns
    data = data[['user_id', 'group', 'convert']]
    # Shuffle rows
    data = data.sample(frac=1).reset_index(drop=True)
    return data

if __name__ == '__main__':
    data_with_difference = generate_conversion_data(50000, 0.15, 0.20)
    data_without_difference = generate_conversion_data(100, 0.15, 0.16)
    # Export
    data_with_difference.to_csv('data/data_with_difference.csv', index=False)
    data_without_difference.to_csv('data/data_without_difference.csv', index=False)