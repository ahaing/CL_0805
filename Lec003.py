import numpy as np
import matplotlib.pyplot as plt 

# 弳度

t = np.arange(0.,1.0, 0.05)
print(t)
#display(t) => .py檔裡面沒有display

y1 = np.sin(2 * np.pi * t) # 弳度換角度
#display(y1)
print(y1)
y2 = np.cos(2 * np.pi * t) # 弳度換角度
#display(y2)
print(y2)

figure1 = plt.figure(figsize=(8,4))
plotF = figure1.add_subplot()
# axes2 = figure1.add_subplot()
plotF.plot(y1)
plotF.plot(y2)
plt.show()

# https://streamlit.io/ => 一個免費的 document
# Home/Streamlit library/Get started/Installation
# pip install streamlit