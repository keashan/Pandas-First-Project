# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
#Read csv files as dataframes
keywords=pd.read_csv(r'C:\Users\keash\OneDrive\Work\My Work\2020\May\Fiverr\ekalb355 - 10\Keywords for Real Estate List.csv')
alllist=pd.read_csv(r'C:\Users\keash\OneDrive\Work\My Work\2020\May\Fiverr\ekalb355 - 10\Test List.csv')

#Add new column to source file if row matches any of keywords. (case is ignored here)
for index, rows in keywords.iterrows():
    mykey=rows.Keyword
    alllist.loc[alllist['owner'].str.contains(mykey,case=False),'coop']=1
    

#Fillter new column to find cooperate owners and asign them to new df
cooplist=alllist[alllist['coop']==1]
cooplist.drop('coop',axis=1,inplace=True)


#Create new list to hold states to keep
stlist=['TX','Texas']

#Add new column to source file with boolean values if values on above list is in the 'mail_state2' column
alllist['tx']=alllist['mail_state2'].isin(stlist)

#Filter who are in the state and not in cooperate list and added to new df
txlist=alllist[(alllist['coop']!=1) & (alllist['tx']==True)]
txlist.drop(['coop','tx'],axis=1,inplace=True)

#Filter who are not in the state and not in cooperate list and added to new df
olist=alllist[(alllist['coop']!=1) & (alllist['tx']==False)]
olist.drop(['coop','tx'],axis=1,inplace=True)

#Save each df as individual csv file
cooplist.to_csv(r'C:\Users\keash\OneDrive\Work\My Work\2020\May\Fiverr\ekalb355 - 10\COOP List.csv', index=False)
txlist.to_csv(r'C:\Users\keash\OneDrive\Work\My Work\2020\May\Fiverr\ekalb355 - 10\Texas List.csv', index=False)
olist.to_csv(r'C:\Users\keash\OneDrive\Work\My Work\2020\May\Fiverr\ekalb355 - 10\Other States List.csv', index=False) 

#Save all df to a single excel file. Each df is a seperate sheet in that file
writer = pd.ExcelWriter(r'C:\Users\keash\OneDrive\Work\My Work\2020\May\Fiverr\ekalb355 - 10\Processed Sheets.xlsx', engine='xlsxwriter')

txlist.to_excel(writer, sheet_name='Single Ownership',index=False)
cooplist.to_excel(writer, sheet_name='Coperate Ownership',index=False)
olist.to_excel(writer, sheet_name='Out of State',index=False)

writer.save()

print('Done')


# %%



