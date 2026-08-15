import pandas as pd
from turtle import pd

import numpy as np

# Original data
data = [10, 20, np.nan, np.nan, 30]
s = pd.Series(data)

print("Original:")
print(s.values)
print()

# 1. bfill with no limit (fills all NaNs)
s_bfill_all = s.bfill()
print("bfill() - no limit:")
print(s_bfill_all.values)
print()

# 2. bfill with limit=1 (fills only 1 NaN closest to next valid value)
s_bfill_limit1 = s.bfill(limit=1)
print("bfill(limit=1):")
print(s_bfill_limit1.values)
print()

# 3. Compare with ffill (no limit)
s_ffill_all = s.ffill()
print("ffill() - no limit:")
print(s_ffill_all.values)
print()

# 4. ffill with limit=1
s_ffill_limit1 = s.ffill(limit=1)
print("ffill(limit=1):")
print(s_ffill_limit1.values)