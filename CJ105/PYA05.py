# 載入 sqlite3 模組
import sqlite3

# 建立資料庫連結
con = sqlite3.connect(r"C:\網頁爬蟲python\CJ105\read.db")
# 建立cursor物件
cur = con.cursor()

# 查詢Employee資料表
cur.execute("SELECT * FROM Employee")

# 印出查詢結果
for t in cur.fetchall():
    print(t)

# 關閉與資料庫的連結
con.close()
