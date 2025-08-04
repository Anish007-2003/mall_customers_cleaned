import pandas as pd

df = pd.read_csv("C:\\Users\\ANISH SAHA\\Downloads\\archive\\Mall_Customers.csv")


print(df.head())
print(df.info())


df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]


print("\nMissing values:\n", df.isnull().sum())

df = df.drop_duplicates()


df['gender'] = df['gender'].str.strip().str.lower()
df['gender'] = df['gender'].replace({'m': 'male', 'f': 'female'})


df['age'] = df['age'].astype(int)
df['annual_income_(k$)'] = df['annual_income_(k$)'].astype(int)
df['spending_score_(1-100)'] = df['spending_score_(1-100)'].astype(int)


df.rename(columns={'annual_income_(k$)': 'annual_income_k',
                   'spending_score_(1-100)': 'spending_score'}, inplace=True)


df.to_csv("C:\\Users\\ANISH SAHA\\Downloads\\mall_customers_cleaned.csv", index=False)


print("\nCleaned dataset preview:\n", df.head())
