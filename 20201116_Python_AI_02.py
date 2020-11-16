# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns

#%%
plt.plot([1,2], [100,200])
plt.title("My Plot")
plt.show()

#%%

tips = sns.load_dataset("tips")
print(type(tips))

#%% pandas 라이브러리 - 데이터 처리 라이브러리
import pandas as pd

## 데이터 살펴보고, 데이터를 처리한다

#%% 행과 열 확인
print(tips.shape)

#%% 행의 제목
print(tips.columns)

#%% 

print(tips.head(3))
print(tips.tail())

#%% 데이터 셋의 전체 정보를 보고 싶다

print(tips.info())

#%%
#url을 이용하여 html 정보를 가져오기
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
print(soup.title)

KOSPI = soup.find("span" , id = "KOSPI_now")
print("네이버 금융 - 코스피 지수:", KOSPI.text)

KOSDAQ = soup.find("span", id = "KOSDAQ_now")
print("네이버 금융 - 코스닥 지수:", KOSDAQ.text)