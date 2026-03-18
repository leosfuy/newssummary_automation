# newssummary_automation
# Automated Financial News AI Synthesizer

AI workflow that automates the extraction, multi-document summarization, and delivery of daily financial market intelligence.

## Tech Stack & Workflow
* **Environment:** Google Apps Script 
* **AI Integration:** Google Gemini 2.5 Flash API
* **Data Source:** Google News RSS 
* ## Core Workflow
1. **Data Retrieval & Parsing:** Scrapes the Google News RSS feed for specific sector keywords. It parses the XML to extract only the relevant article titles and descriptions.
2. **AI Processing & Synthesis:** Sends the parsed raw text to the Gemini API. The prompt is strictly configured to group the news by industry sectors and synthesize the content into summaries, explicitly instructed not to generate information outside the provided text.
3. **Formatting & Delivery:** Drops messy tracking URLs to keep the output clean. It then formats the AI's response into a readable HTML structure and emails it directly to the user via Google Apps Script.
4. **Error Monitoring:** Wraps the execution in a try-catch block. If the RSS fetch or API call fails, the script safely aborts the email generation and sends an error log notification to the developer instead.

## Output Example
 **[View Sample HTML Output (Open with Browser)](sample.html)**


## How It Works (Workflow)
1. **Trigger:** A daily time-driven trigger awakens the script at 7:00 AM.
2. **Fetch:** Scrapes the Google News RSS feed for the keyword "類股" (Sector Stocks) within the last 48 hours.
3. **Parse:** Extracts titles, sources, and descriptions for up to 30 articles using XML parsing.
4. **Synthesize:** Sends the raw text batch to the Gemini API with a heavily engineered prompt, asking it to categorize the news and write comprehensive summaries using HTML tags.
5. **Deliver:** Wraps the AI's output in styled HTML and sends it via the `MailApp` service to the user's inbox.

## Setup Instructions
If you want to run this workflow yourself:
1. Create a new project on [Google Apps Script](https://script.google.com/).
2. Copy the code from `main.js` and paste it into the editor.
3. Replace `YOUR_GEMINI_API_KEY` and `YOUR_EMAIL_ADDRESS` with your actual credentials.
4. Set up a Time-driven Trigger to run the `sendDailyStockNews` function daily.
