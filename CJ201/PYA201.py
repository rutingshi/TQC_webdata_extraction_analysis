# 載入模組
import requests
import re

url = 'https://www.codejudger.com/target/5201.html'

# 使用 GET 請求
htmlfile = requests.get(url)
# 驗證HTTP Status Code
if htmlfile.status_code == 200:
    # 欲搜尋的字串
    s = input("請輸入欲搜尋的字串 : ")
    l = re.findall(s, htmlfile.text)
    if s in htmlfile.text:
        print(s, "搜尋成功")
        print(s, "出現 %d 次" % len(l))
    else:
        print(s, "搜尋失敗")
        print(s, "出現 0 次")
else:
    print("網頁下載失敗")
