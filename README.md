# AI Webscraper

An AI-powered tool for extracting data from websites using natural language prompts. 

## Description

This project uses a combination of web scraping and AI techniques to make data extraction from websites more accessible.  You provide a website URL and describe the data you want to extract using a natural language prompt.  The tool uses the Ollama large language model to understand your request and intelligently parse the website's content to return the desired information. 

## Key Features

- **Web Scraping:** Uses Selenium for robust website interaction and BeautifulSoup for HTML parsing. 
- **AI-Powered Data Extraction:**  Employs the Ollama AI model (through the Langchain library) for advanced text understanding and data retrieval based on user prompts. 
- **User-Friendly Interface:**  Built with Streamlit to provide an easy-to-use web interface for running the scraper. 

## Installation

1. **Clone the repository:** `git clone https://github.com/SteffySenson/ai-webscraper.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Download ChromeDriver:**  Get the ChromeDriver executable that matches your Chrome browser version from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) and place it in your project directory. 

## Usage

1. **Run the Streamlit app:** `streamlit run main.py`
2. **Enter a website URL:** Paste the URL of the website you want to scrape.
3. **Describe the data to extract:** Provide a natural language description of the information you need. Be as specific as possible. 
4. **Click "Scrape Site" and "Parse Content":** The tool will scrape the website and attempt to extract the requested data based on your prompt.

## Example

**URL:** https://www.example.com/product/123
**Prompt:** "Find the product name, current price, and whether it's in stock."

**Possible Output:**

Product Name: Awesome Widget
Price: $29.99
In Stock: Yes

## Notes

- This project is for educational and experimental purposes. Always respect websites' terms of service and use web scraping ethically. 
- The accuracy of data extraction depends on the complexity of the website and the clarity of the prompt. 
- You may need to adjust the prompt and parsing logic for optimal results on different websites. 

## Contributing

Contributions are welcome! If you have ideas for improvement or find any bugs, feel free to open an issue or submit a pull request.
