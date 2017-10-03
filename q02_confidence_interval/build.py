import math
import numpy as np
import scipy.stats as stats
import pandas as pd



df = pd.read_csv('data/house_pricing.csv')

np.random.seed(10)
sample = np.random.choice(a= df['GrLivArea'], size = 500)

def confidence_interval(sample=sample):
    # Enter Code Here
    return confidence_interval