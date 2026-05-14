import pandas as pd

df = pd.read_parquet('data/combined.parquet')
df_preprocessed = pd.read_parquet('data/preprocessed.parquet')

df.sample(n = 12000, random_state = 42).to_csv('data/sample.csv', index = False)
df_preprocessed.sample(n = 12000, random_state = 42).to_csv('data/sample_preprocessed.csv', index = False)
