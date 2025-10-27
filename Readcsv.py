import pandas as pd

df= pd.read_csv('/Users/kishorebattula/Downloads/Pipeline_Contractor_Awarded_Engagements.csv', sep=',')
print(df.shape)
print((df.info()))


