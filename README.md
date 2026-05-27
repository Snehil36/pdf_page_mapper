**Note:** This is a Python prototype used to develop and test the core logic. The final product will be a Chrome extension that runs entirely in the browser.

# PDF Page Mapper

## Purpose
Navigating through a textbook PDF is frustrating when the PDF page numbers don't match the printed page numbers. For example, a textbook's title page is PDF page 1, followed by a preface and index numbered in roman numerals — by the time you reach the main content, the PDF page number is much higher than the printed page number. This forces students to do mental arithmetic every time they want to jump to a specific page.

PDF Page Mapper solves this by automatically extracting the table of contents, calculating the offset between printed and PDF page numbers, and providing a corrected navigation map.

## How It Works
1. Extracts the first 50 pages of the PDF
2. Uploads them to the Gemini 2.5 AI API
3. Gemini identifies the table of contents and extracts chapter titles and printed page numbers
4. The offset between printed and PDF page numbers is calculated
5. A corrected TOC is returned mapping every chapter to its true PDF page

## Tech Stack
- Python
- PyMuPDF (PDF parsing)
- Google Gemini 2.5 API (AI-powered TOC extraction)

## How To Run
1. Clone the repo
2. Create a virtual environment: `python3 -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install pymupdf google-genai`
5. Set your Gemini API key: `export GEMINI_API_KEY="your-key-here"`
6. Run: `python3 main.py`

## Future Plans
- Chrome extension for in-browser PDF navigation
- Support for appendix and roman numeral page sections
- Clickable TOC that jumps to the correct PDF page
