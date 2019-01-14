import pandas as pd
df = pd.read_csv('kstones.csv', usecols=range(1, 5))
frames = list()
for i in range(8):
    count = df['Counts'].iloc[i]
    size = df['Size'].iloc[i]
    method = df['Method'].iloc[i]
    outcome = df['Outcome'].iloc[i]
    
    
    subset = dict()
    subset['Size'] = [size] * count
    subset['Method'] = [method] * count
    subset['Outcome'] = [outcome] * count

    frames += [pd.DataFrame(subset)]
df = pd.concat(frames)
df['Individual'] = range(df.shape[0])
df.set_index('Individual', inplace=True)
df.to_pickle('kstones.pkl')
