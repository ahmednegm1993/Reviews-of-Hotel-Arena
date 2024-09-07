import pandas as pd

df=pd.read_excel(r'E:\\Data_analysis_projects\\hotel_reviews\dataset\\hotel_reviews.xlsx')
df=df[df['hotel_name']=='Hotel Arena']
df1=df.groupby('hotel_name')['reviewer_score'].count()
df2=df.pivot_table(index=None,
                   columns='hotel_name',
                   values='reviewer_score',
                   aggfunc='count'
)

print(df1)
print(df2)