# 金融新聞自動化摘要發送系統 

本專案是一個基於 Google Apps Script (GAS) 開發的自動化工作流，每日固定時間彙整特定關鍵字之金融新聞，並透過 AI 進行內容摘要後，自動發送電子郵件至指定信箱。

## 功能
* **自動化抓取**：每日定期從指定新聞來源（如 UDN 等）擷取包含特定關鍵字（類股）的金融新聞。
* **AI 協作摘要**：串接 Gemini API 進行文本分析，將繁雜的新聞內容提煉為簡明要點。
* **定時排程**：利用 Google Apps Script 的觸發器功能，於每日早上 7:00 派送郵件。

## 技術架構
* **開發環境**：Google Apps Script (GAS)
* **核心語言**：JavaScript
* **外部 API**：
    * **Gemini API**：負責新聞內容的邏輯分析與摘要生成。
    * **URL Fetch Service**：用於獲取遠端新聞網站的內容。
* **資料來源**：以 UDN 等新聞網站為主，確保新聞連結之穩定性。
* **派送系統**：Gmail

## 系統流程說明
1. **觸發階段**：GAS 時間驅動觸發器於每日上午 7:00 啟動腳本。
2. **抓取階段**：腳本向指定新聞來源發送請求，過濾出含有目標關鍵字的報導。
3. **處理階段**：將選定的新聞標題與內容傳送至 Gemini API，要求其生成精簡的摘要。
4. **派送階段**：將彙整好的摘要與原文連結組合成郵件內文，透過 MailApp 服務發送至指定信箱。

## 注意事項
* 需於 Google Cloud Console 取得有效之 API Key。
* 權限需包含 `https://www.googleapis.com/auth/script.external_request` 以及 `https://www.googleapis.com/auth/gmail.send`。
