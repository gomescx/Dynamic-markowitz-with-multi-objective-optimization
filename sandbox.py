#%%
import pandas as pd
import numpy as np
numbers = [1,2,3,np.nan,4,np.nan]
df = pd.Series(numbers)
print(df[df.isnull()])