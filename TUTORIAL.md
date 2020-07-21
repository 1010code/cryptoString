## 前言
打包python module 到 PYPI 上

## 建立專案
專案架構如下: 最外層資料夾要建立一個 `setup.py` 檔，該檔案是部署打包成PYPI可讀取的格式的設定檔。`cryptoString` 資料夾就是你想建立的 Package 名稱，資料夾內的 `__init__.py` 就可以自定義你個人化的函示庫。

```
.
├── cryptoString
│   └── __init__.py
└── setup.py
```

## 撰寫第一個 Python 函式庫
這個範例很簡單看資料夾名稱 `cryptoString` 可以猜得出來。我想實做一個中英文字串亂數的產生器，簡單來說呼叫此函式回隨機產生n個長度的字串Token。第一個 `RandomChar(num)` 函式，使用者可以呼叫此函式並宣告要回傳多少長度的Token內容。第二個函式是回傳目前的版本代號，此函式稍後會有用途做範例到時各位就會知道囉！

```py
#!/usr/bin/env python
# encoding=utf-8
import random

def RandomChar(num):
    string = 'abcdefghijklmnopqrstuvwxyz0123456789'
    randomStr = ''
    for i in range(num):
      randomStr += string[random.randint(0, 35)]
    return randomStr
 

def version():
    print('version: 1.0.0')
```

## setup.py 設定
如果自己的 Python 專案想要讓大家能夠安裝到每個人 Python 環境中，一定要撰寫 `setup.py`。這裡教各位設定 `setup.py` 裡的資訊，這裡要讓程式知道模組裡面的 metadata 使得 PYPI 平台可以識別其專案內容。

| 欄位名稱                      | 描述                       |
|-------------------------------|----------------------------|
| name                          | 專案名稱                   |
| packages                      | 套件名稱                   |
| version                       | 版本                       |
| author                        | 作者                       |
| author_email                  | 作者信箱                   |
| url                           | 專案頁面(通常為Github專案) |
| description                   | 專案描述                   |
| long_description              | PyPI上所顯示的README       |
| long_description_content_type | PyPI專案首頁的介紹格式     |
| packages                      | 該函式庫可被import的檔案   |
| install_requires              | 此專案相依的套件           |
| classifiers                   | 此專案的其他相關訊息       |
| python_requires               | Python版本限制             |

```py
#!/usr/bin/env python
# coding: utf-8
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='cryptoString',
    version='1.0.0',
    author='andy6804tw',
    author_email='andy6804tw@yahoo.com.tw',
    url='https://github.com/1010code/cryptoString',
    description='A module that returns alphanumeric strings.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    entry_points={
        'consoleScripts': [
            'cryptoString=cryptoString:version'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
```