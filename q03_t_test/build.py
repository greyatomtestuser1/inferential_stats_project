import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def t_test(df=df):
    # Enter Code Here
    return p_value, p_value < 0.05