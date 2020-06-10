#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def hypothesis_test(df):
    """Tests whether the difference in conversion rate is statistically significant."""
    
    p = df['convert'].mean()
    print('The probability of a user converting: {}'.format(p))
    # Compute the observed difference between conversion rates
    p_treatment = df[df['group'] == 'treatment']['convert'].mean()
    p_control = df[df['group'] == 'control']['convert'].mean()
    current_diff = p_treatment - p_control
    print('Difference in treatment group conversion and control group conversion: {:.4f}'.format(current_diff))
    print('Check whether the traffic is comparable for both pages:')
    print(df['group'].value_counts(normalize=True))

    
    n_new = len(df[df['group'] == 'treatment'])
    n_old = len(df[df['group'] == 'control'])
    
    all_diffs = []
    for _ in range(10000):
        new_page_converted = np.random.choice([1, 0], size=n_new, p=[p, (1-p)])
        old_page_converted = np.random.choice([1, 0], size=n_old, p=[p, (1-p)])
        diff = new_page_converted.mean() - old_page_converted.mean()
        all_diffs.append(diff)
    all_diffs = np.array(all_diffs)
    return all_diffs, current_diff

def plot_diff(all_diffs, current_diff):
    
    # Plot all simulated differences in conversion rate
    plt.hist(all_diffs);
    plt.xlabel('Differences')
    plt.ylabel('Count')
    plt.title('Differences in conversion rate')
    
    # Plot current difference in conversion rate
    plt.axvline(current_diff, c='red')
    plt.show()

def compute_p_value(all_diffs, current_diff):
    p_value = (all_diffs > current_diff).sum() / len(all_diffs)
    return p_value


if __name__ == '__main__':
    df_1 = pd.read_csv('data/data_with_difference.csv')
    all_diffs_1, current_diff_1 = hypothesis_test(df_1)
    plot_diff(all_diffs_1, current_diff_1)
    p_value_1 = compute_p_value(all_diffs_1, current_diff_1)
    print('p-value: ', p_value_1)
    print('\n')
    df_2 = pd.read_csv('data/data_without_difference.csv')
    all_diffs_2, current_diff_2 = hypothesis_test(df_2)
    plot_diff(all_diffs_2, current_diff_2)
    p_value_2 = compute_p_value(all_diffs_2, current_diff_2)
    print('p-value: ', p_value_2)
    
