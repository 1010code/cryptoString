## 前言
打包python module 到PYPI 上

## 建立專案
專案架構如下: 最外層資料夾要建立一個 `setup.py` 檔，該檔案是部署打包成PYPI可讀取的格式的設定檔。`cryptoString` 資料夾就是你想建立的 Package 名稱，資料夾內的 `__init__.py` 就可以自定義你個人化的函示庫。

```
.
├── cryptoString
│   └── __init__.py
└── setup.py
```

## 撰寫第一個 Python 函式庫
這個範例很簡單看資料夾名稱 `cryptoString` 可以猜得出來。我想實做一個中英文字串亂數的產生器，簡單來說呼叫此函式回隨機產生n個長度的字串Token。第一個 `RandomChar(num)` 函式，使用者可以呼叫此函式並宣告要回傳多少長度的Token內容。第二個

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
如果自己的python專案想要讓大家能夠安裝到python環境中，一定要撰寫setup.py，這邊針對還要上傳到PyPI，來客製化我們的setup.py，我們先來檢視一下目前的結構和等等我們要加入的幾個設定檔位置: