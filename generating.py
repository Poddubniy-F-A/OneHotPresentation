import random
import pandas as pd

COL_NAME = 'whoAmI'


def df_gen():
    lst = ['robot'] * 10
    lst += ['human'] * 10
    random.shuffle(lst)
    return pd.DataFrame({COL_NAME: lst})
