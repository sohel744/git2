import pandas as pd

##CREATING DATAFRAME USING FILES


#df=pd.read_clipboard()
#print(df)


#df=pd.read_csv('E:/file/Salaries.csv')

#SPEACIAL FUNCTION TO DATAFRAME ROWS
#print(df.head()) #first five record
#print(df.head(10)) #first ten record
#print(df.tail()) #last five record
#print(df.tail(10)) #last ten record



#print(df)
#print(df['gender'])

'''df2=pd.read_csv('E:/file/populations.txt',sep='\t',comment='#',header=None,names=['year','hare','lynx','carrot'])
print(df2.head())'''

## ATTRIBUTES
#1 ndim
#2 shape
#3 size
#4 dtypes
#5 index
#6 column
#7 values
#8 axes
#df.columns=['a','b','c','d','e','f']
#print(df.ndim)
#print(df.shape)
#print(df.size)
#print(df.dtypes)
#print(df.index)
#print(df.columns)
#print(df.values)
#print(df.values.T[-1])
#print(df.values.T[-1].mean())

#print(df['f'].mean())
#print(df.axes)

df=pd.read_csv('E:/file/Salaries.csv')
#print(df)
#print(df['salary'].mean())

##DATAFRAME SLICING

#slice column

#print(df['salary'])
#col=['rank','salary']
#print(df[col])
#print(df[['rank','salary']].head())
#print(df[['salary']].head())# we can get dataframe not series

# slice row if you want to slice row pass the range of rows

#print(df[0:3])

#print(df[0:7])


## slicing speacific and specific column

#1. df.loc[rowrange , colrange]  ==> slice based on row labels and column labels
#2. df.iloc[rowrange, colrange]  ==> slice based on row index position and column index position

#all rows
#print(df.loc[0:10,:])


##speacific rows with all columns
#print(df.loc[[15,9,6,7,22],:])

## speacific row with speacific column
#print(df.loc[[1,4,7,34],['rank','salary','gender']])

## speacific row with range of column
#print(df.loc[[1,4,7,34],'rank':'gender'])


##speacific rows and speacific column based on index position
#print(df.iloc[:,[0,-2,-1]].head())

###CONDITIONAL SLICING

#print(df['salary']>50000)  #we can get true
#print(df[df['salary']>50000]) #we can get values
#print(df[(df['rank']=='Prof') & (df['salary']>50000)])
#print(df[(df['rank']=='Prof') & (df['salary']<80000)])
#print(df[(df['rank']=='AssocProf') & (df['salary']<80000)])


