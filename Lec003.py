import numpy as np
import matplotlib.pyplot as plt 

# 用 streamlit 在網頁上畫圖
import streamlit as stlit

# 弳度
t = np.arange(0.,1.0, 0.05)
print(t)
# display(t) => .py檔裡面沒有display

# 畫 t 上去
stlit.write(t) 

y1 = np.sin(2 * np.pi * t) # 弳度換角度
# display(y1)
# print(y1) => py只能顯示數值

y2 = np.cos(2 * np.pi * t) # 弳度換角度
#display(y2)
# print(y2)

st.write(y1)
st.write(y2)
figure1 = plt.figure(figsize=(8,4))
plotF = figure1.add_subplot()
# axes2 = figure1.add_subplot()
plotF.plot(y1)
plotF.plot(y2)
# plt.show()
stlit.write(figure1)

# https://streamlit.io/ => 一個免費的 document
# Home/Streamlit library/Get started/Installation
# pip install streamlit
# Working with Streamlit is simple. First you sprinkle a few Streamlit commands into a normal Python script, then you run it with streamlit run