# Web Scraping and Summarization using Cohere

This project demonstrates how to scrape text from a webpage and summarize it using Cohere's Natural Language Processing (NLP) API. It combines web scraping with text summarization to condense lengthy articles or web content into concise summaries.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- Cohere API Key (sign up at [Cohere](https://www.cohere.ai/))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/your_project.git
   cd your_project
   ```

2. Install required Python packages:
   ```bash
   pip install cohere beautifulsoup4 requests
   ```

## Usage

1. Replace `'YOUR_API_KEY'` in the script (`Web_scraper.py`) with your actual Cohere API key.

2. Run the script with the URL of the webpage you want to summarize:
   ```bash
   python summarize_webpage.py https://example.com/article
   ```

   Replace `https://example.com/article` with the URL of the webpage you want to summarize.

3. The script will fetch the webpage content, summarize it using Cohere, and print the summary.

## Example

Here's an example of how to summarize a webpage using this script:

```bash
python Web_scraper.py https://example.com/sample-article
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Cohere for providing the NLP capabilities used in this project.
- BeautifulSoup for facilitating web scraping.
- Requests for HTTP requests handling.

