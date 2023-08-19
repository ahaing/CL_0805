import csv
import pandas as pd
import streamlit as st
import ffn

def getStockNames() -> pd.Series:
    with open('codeSearch.csv',encoding='utf-8',newline='') as file:
        next(file)
        csv_reader = csv.reader(file)
        stock_codes = {}
        for item in csv_reader:
            key  =  item[2]
            stock_codes[key] = item[3]
        
    code_series:pd.Series = pd.Series(stock_codes)
    return code_series

def get_dataFrame(menu:list, start_year) -> pd.DataFrame:
    stock_data = ffn.get(menu, start=start_year)
    return stock_data

def displayData(dataFrame:pd.DataFrame,start_year) -> None:
    st.subheader(f'{start_year}~目前的歷史資料')
    st.dataframe(dataFrame)

def rename_columns_name(dataFrame:pd.DataFrame,mapping:pd.Series) -> pd.DataFrame:
    ser1:pd.Series = mapping[dataFrame.columns.str[:4]]
    dataFrame.columns = ser1.values
    return dataFrame

#多重選取
stockNames:pd.Series = getStockNames()
print(stockNames)
stock_name_id = stockNames.index + "_" + stockNames.values
options = st.sidebar.multiselect('請選擇',
                       stock_name_id,
                       placeholder='股票:')

names:list[str] = []
for name in options:
    name_string = name.split("_")[0]
    names.append(name_string + ".TW")
#print(names)


if len(names) != 0:
    start_year = st.sidebar.selectbox("起始年份",range(2000,2023))
    dataFrame:pd.DataFrame = get_dataFrame(names,f"{start_year}-01-01")
    dataFrame1 = rename_columns_name(dataFrame,stockNames)
    displayData(dataFrame1,start_year=start_year)