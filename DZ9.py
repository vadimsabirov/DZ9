import pandas as pd
import numpy as np
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
data = data.melt(ignore_index=False).reset_index().pivot_table('variable', 'index', 'value', aggfunc='count').fillna(0).astype(int)
print(data)

