# Auto_GF 
透過selenium模擬網頁操作，自動儲GF序號，以完美世界2遊戲為範例。


# 使用說明

首先安裝Anaconda，並且創建一個虛擬環境(Python 3.8)後安裝 Spyder 並分段執行(F9) 即可使用

```
pip install selenium
pip install webdriver_manager
```

首先執行第一段程式碼，手動輸入帳密(我要是寫成小黑窗，估計你帳密也不敢打進去)
![demo](https://user-images.githubusercontent.com/101848874/163753849-5eff3cfa-0ae8-49c3-9d60-af2d473b9edc.gif)

然後接著跳到套領虛寶的頁面，然後修改select_by_index()裡面的數字，
代表第幾個帳號，第幾個伺服器，第幾個腳色名稱，調整好後選取按F9執行即可，下方有GIF示範圖。


```
#選擇遊戲帳號
Game_ID = Select(browser.find_element_by_xpath('//*[@id="Game_ID"]'))
Game_ID.select_by_index(3)

#選擇伺服器
Game_Svr = Select(browser.find_element_by_xpath('//*[@id="Game_Svr"]'))
Game_Svr.select_by_index(1)

#選擇角色名稱
Game_Role = Select(browser.find_element_by_xpath('//*[@id="Game_Role"]'))
Game_Role.select_by_index(2)
```

![demo1](https://user-images.githubusercontent.com/101848874/163753854-c78870e7-fbd3-40df-be64-65d314b148d6.gif)


序號範例:

cardInfo = [
	"W3EOD01000058236", 	"yqgMhQBc5fcjqQXS", 
	"W3EOD01000000293", 	"fsaY9raNU73netpd", 
]
