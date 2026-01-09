# TQC+ 網頁資料擷取與分析 Python - 實作作品集

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Status](https://img.shields.io/badge/Status-Completed-green)

### About
本專案為 **TQC+ 網頁資料擷取與分析** 證照的完整實作紀錄。
內容涵蓋從 **「資料爬取」** -> **「清洗處理 (ETL)」** -> **「統計分析」** 到 **「視覺化圖表」** 的完整數據分析流程。

### Key Features
* **🕷️ 網路爬蟲 (Web Scraping):**
  熟練使用 `Requests` 與 `BeautifulSoup4` 抓取靜態/動態網頁，並能處理 API 串接與正規表達式 (Regex) 資料篩選。
* **📊 數據分析 (Data Analysis):**
  應用 `Pandas` 與 `NumPy` 進行資料清洗、缺失值處理、分組統計 (GroupBy) 及多維陣列運算。
* **📈 資料視覺化 (Visualization):**
  使用 `Matplotlib` 繪製專業統計圖表（含長條圖、圓餅圖、折線圖與直方圖），並實現多圖併列 (Subplot) 呈現。
* **💾 多元格式整合:**
  具備 `CSV`、`JSON`、`XML` 檔案讀寫能力，並能串接 `SQLite` 資料庫進行 SQL 查詢操作。

### Tech Stack
| Category | Tools |
|---|---|
| **Language** | Python 3.x |
| **Libraries** | Pandas, NumPy, Matplotlib, Requests, BeautifulSoup4 |
| **Data** | SQLite, JSON, CSV, XML |

## 💻 快速開始
```bash
# 1. 下載專案
git clone [https://github.com/rutingshi/TQC-_webdata_extraction_analysis.git](https://github.com/rutingshi/TQC-_webdata_extraction_analysis.git)

# 2. 進入資料夾並執行程式 (範例)
cd CJ101
python PYA101.py