# newssummary_automation
# 📈 Automated Financial News AI Synthesizer

AI workflow that automates the extraction, multi-document summarization, and delivery of daily financial market intelligence.

## 🛠️ Tech Stack & Features
* **Environment:** Google Apps Script 
* **AI Integration:** Google Gemini 2.5 Flash API
* **Data Source:** Google News RSS 
* **Key Features:**
  * **Multi-Document Summarization:** Aggregates redundant news into concise, high-density summaries.
  * **Zero-Hallucination Prompt Engineering:** Strict prompt constraints to prevent the AI from generating facts not present in the source text.
  * **Automated Data Sanitization:** Strips out broken or tracking-heavy URLs to ensure a clean reading experience.
  * **Error Handling & Fallback:** Built-in try-catch logic with automated error-alert emails to the developer if scraping or API calls fail.

## 📷 Output Example


## ⚙️ How It Works (Workflow)
1. **Trigger:** A daily time-driven trigger awakens the script at 7:00 AM.
2. **Fetch:** Scrapes the Google News RSS feed for the keyword "類股" (Sector Stocks) within the last 48 hours.
3. **Parse:** Extracts titles, sources, and descriptions for up to 30 articles using XML parsing.
4. **Synthesize:** Sends the raw text batch to the Gemini API with a heavily engineered prompt, asking it to categorize the news and write comprehensive summaries using HTML tags.
5. **Deliver:** Wraps the AI's output in styled HTML and sends it via the `MailApp` service to the user's inbox.

## 💻 Setup Instructions
If you want to run this workflow yourself:
1. Create a new project on [Google Apps Script](https://script.google.com/).
2. Copy the code from `main.js` and paste it into the editor.
3. Replace `YOUR_GEMINI_API_KEY` and `YOUR_EMAIL_ADDRESS` with your actual credentials.
4. Set up a Time-driven Trigger to run the `sendDailyStockNews` function daily.
