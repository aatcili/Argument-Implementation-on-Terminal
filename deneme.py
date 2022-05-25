from  datetime import datetime, timedelta
import pandas as pd
import numpy as np
import sys

df = pd.DataFrame()
days = pd.date_range(datetime.today(), datetime.now() + timedelta(7), freq='D' )
df["days"] = days
df["actual"] = np.random.randint(300,400,8)
df["predict"] = np.random.randint(300,400,8)
df["days"] = df["days"].dt.strftime('%Y-%m-%d')

df["days"] = pd.to_datetime(df["days"])

first = sys.argv[1]
second = sys.argv[2]
format = '%Y-%m-%d'

first = datetime.strptime(first, format)
second = datetime.strptime(second, format)

print(df[(df["days"] > first) & (df["days"] < second)])