import pandas as pd


'''df=pd.Series([10,20,30,40,50,60,70,80])

#print(df)


df.index=['a','b','c','d','e','f','g','h']

print(df.index )
for i in df:
    print(i)


print(df)'''
#print(df[1:7:2])
#print(df['b':'g'])
#print(df[[1,2,3,6]])

#print(df.mean())
#print(df.max())
#print(df.quantile())

#print(df.quantile())

df2=[[100,'sakib',10000],[101,'xyz',20000],[102,'abc',30000]]
#print(pd.Series(df2))
a=(pd.DataFrame(df2))
print(a)
#print(a[:][:])
#print(a.dtypes)

#print(a.values)

#a.index=['e1','e2','e3']
#a.columns=['eno','ename','esal']

#a=pd.DataFrame(df2,index=['e1','e2','e3'],columns=['eno','ename','esal'])

#print(a)
#print(a['esal'].mean())

##CREATING DATAFRAME USING DICTIONARY

dic={'eno':[100,101,102],'ename':['sakib','xyz','abc'],'esal':[10000,20000,30000]}
a=pd.DataFrame(dic)
a=pd.DataFrame(dic,index=['a','b','cu'])
#print(a)
a.reset_index(drop=True ,inplace=True)

print(a)













