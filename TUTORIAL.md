## 前言
打包python module 到 PyPI 上

## 建立專案
專案架構如下: 最外層資料夾要建立一個 `setup.py` 檔，該檔案是部署打包成PyPI可讀取的格式的設定檔。`cryptoString` 資料夾就是你想建立的 Package 名稱，資料夾內的 `__init__.py` 就可以自定義你個人化的函示庫。

```
.
├── README.md
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
如果自己的 Python 專案想要讓大家能夠安裝到每個人 Python 環境中，一定要撰寫 `setup.py`。這裡教各位設定 `setup.py` 裡的資訊，這裡要讓程式知道模組裡面的 metadata 使得 PyPI 平台可以識別其專案內容。唯一值得一提的是 `entry_points` 還記得先前定義好的 `version()` 函式嗎，如果安裝好套件直接在終端機輸入 `cryptoString` 將會回傳版本號。因此 PyPI 不僅能夠下載匯入函式庫也能當作腳本語言，如果有寫過 Node.js 朋友一定對 npm 不陌生。其實 npm 與 PyPI 兩者做的內容都是一樣的差別在於一個是 JavaScript 的 Package，一個是 Python 的 Package。

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
| entry_points                  | 設定shell script呼叫路徑 |

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

`setup.py` 寫完後，可以先通過命令校驗 setup 有沒有錯誤地方。正常會出現 `running check` 的字串。如果輸入指令後沒有跑出任何錯誤訊息代表正確無誤。

```sh
python setup.py check
```

## 打包函式庫
首先我們必須透過 `pip` 下載打包的套件(安裝一次即可)，這裏使用 `setuptools` 套件來打包函式庫以及 `wheel` 建立 wheel file。

```sh
pip install setuptools wheel
```

安裝好 `setuptools` 後我們就能執行 `setup.py` 進行打包囉！

```sh
python setup.py sdist bdist_wheel
```

打包完成後可以看到有三個資料，分別是 `build`、`cryptoString.egg-info`、`dist`。

![](https://i.imgur.com/9rOjEOx.png)

## 發佈到PyPI
使用 `pip` 安裝 `twine` 套件(安裝一次即可)。此套件會把 `dist/*` 裡的相關資料發布到PyPI。

```sh
pip install twine
```

安裝完成後就能將剛打包好的資料發布到PyPI。發布前需要先到 [PyPI](https://pypi.org/) 註冊一個帳號。接著輸入以下指令時會要求你輸入帳密，輸入成功後就會幫你將函式庫上傳到PyPI囉！

```py
python -m twine upload dist/*
```