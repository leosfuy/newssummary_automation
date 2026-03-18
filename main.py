function sendDailyStockNews() {
  var apiKey = 'YOUR_GEMINI_API_KEY'; 
  var emailAddress = 'GMAILADDRESS@gmail.com'; 

  try {
    // === 1. 使用 Google 新聞搜尋「類股」，並限制「1天內 (when:1d)」 ===
    var rssUrl = 'https://news.google.com/rss/search?q=類股+when:1d&hl=zh-TW&gl=TW&ceid=TW:zh-Hant';
    var response = UrlFetchApp.fetch(rssUrl);
    var xml = XmlService.parse(response.getContentText());
    var channel = xml.getRootElement().getChild('channel');
    
    if (!channel) throw new Error("無法取得 Google 新聞資料。");
    
    var entries = channel.getChildren('item');
    var newsList = "";
    var addedCount = 0;
    
    // 抓取前 30 篇提供給 AI 進行深度統整
    for (var i = 0; i < Math.min(30, entries.length); i++) {
      var title = entries[i].getChildText('title');
      var sourceName = entries[i].getChild('source').getText(); 
      var desc = entries[i].getChildText('description') || "";
      
      // 這次我們完全不抓網址，只把標題、來源和內文摘要餵給 AI
      newsList += "【" + sourceName + "】標題：" + title + "\n摘要細節：" + desc + "\n\n";
      addedCount++;
    }

    Logger.log("✅ 成功抓取 " + addedCount + " 篇 Google 類股新聞！（無網址版）");
    if (addedCount === 0) throw new Error("今日沒有相關的類股新聞。");

    // === 2. 呼叫 AI (強化「深度綜合摘要」，並移除網址要求) ===
    var prompt = "你是專業的財經分析師。請『嚴格且僅限於』根據以下提供的新聞素材進行分類與深度摘要整理。絕對禁止捏造素材中未提及的資訊。\n\n🎯 核心任務：\n1. 將新聞依據「產業板塊或類股主題」分門別類，使用 <h3> 作為分類標題（例如：科技半導體類股、金融保險類股）。\n2. 在每個分類標題下，先寫一段「綜合深度摘要」。這個摘要必須非常詳細，統整該類別下所有相關新聞的重大事件、數據表現、法人動向與市場影響，讓讀者不需看原文也能完全掌握具體發生了什麼事。重點字句請用 <b>粗體</b> 標示。\n3. 在深度摘要的下方，列出組成這段摘要的新聞來源清單（僅包含媒體與標題，絕對不要生成任何網址連結）。\n\n請嚴格遵守以下 HTML 輸出格式（直接輸出 HTML，請勿加上 ```html 標記，絕對不要使用 Markdown 例如 **）：\n\n<h3>[分類標題]</h3>\n<p>[綜合深度摘要：詳細統整該分類下的新聞內容，請寫得豐富且具體]</p>\n<ul>\n  <li>【媒體名稱】新聞標題</li>\n  <li>【媒體名稱】新聞標題</li>\n</ul>\n<hr>\n\n嚴格限定的新聞素材如下：\n" + newsList;
    
    var apiUrl = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=' + apiKey;
    
    var payload = {
      "contents": [{"parts": [{"text": prompt}]}]
    };

    var options = {
      "method": "post",
      "contentType": "application/json",
      "payload": JSON.stringify(payload),
      "muteHttpExceptions": true
    };

    var apiResponse = UrlFetchApp.fetch(apiUrl, options);
    var json = JSON.parse(apiResponse.getContentText());
    
    if (json.error) throw new Error("API 錯誤：" + json.error.message);
    if (!json.candidates || json.candidates.length === 0) throw new Error("AI 回傳了空值。");

    var summary = json.candidates[0].content.parts[0].text;
    var cleanSummary = summary.replace(/```html/gi, "").replace(/```/g, "");

    // === 3. 發送常規電子郵件 ===
    var dateString = Utilities.formatDate(new Date(), "GMT+8", "yyyy/MM/dd");
    var subject = "📊 【全網類股深度解析早報】" + dateString;
    
    
    MailApp.sendEmail({
      to: emailAddress,
      subject: subject,
      htmlBody: "<div style='font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif; line-height: 1.8; font-size: 15px; color: #333;'>" + cleanSummary + "</div>"
    });
    Logger.log("✅ 報表發送成功！");

  } catch(e) {
    Logger.log("❌ 發生錯誤: " + e.toString());
    MailApp.sendEmail({
      to: emailAddress,
      subject: "⚠️ 【系統通知】早報執行失敗",
      htmlBody: "<div style='font-family: sans-serif; color: #d93025;'><p>發生錯誤：</p><p><b>" + e.toString() + "</b></p></div>"
    });
  }
}