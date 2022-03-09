import numpy as np
from scipy.stats import norm

def get_sigma_from_pvalue(pval, decimals=3):
    return np.abs(np.round(norm.ppf(pval), decimals))

def get_prob_from_sigma(sigma, decimals=10):
    return np.round(1-(norm.sf(sigma)*2), decimals)

def get_prob_from_pvalue(pval, decimals=10):
    return np.round(1-pval*2, decimals)

def get_pvalue_from_sigma(sigma, decimals=10):
    p = get_prob_from_sigma(sigma, decimals=decimals)
    return np.round((1-p)/2, decimals)


sigma = 4
prob = 0.9973
pval = np.round((1-prob)/2, 10)

print(f'1-Tail probability of {sigma} sigma = {get_prob_from_sigma(sigma)}')
print(f'1-Tail probability of {pval} pvalue = {get_prob_from_pvalue(pval)}')
print(f'{pval} pvalue = {get_sigma_from_pvalue(pval)} sigma')
print(f'{sigma} sigma = {get_pvalue_from_sigma(sigma)} pvalue')