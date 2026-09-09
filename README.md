

```markdown
# Fake Python Jobs Web Scraper

This project is a web scraper designed to collect job listings from the [Real Python Fake Jobs](https://realpython.github.io/fake-jobs/) website. It serves as an educational tool to understand HTML parsing, data extraction, and file handling using Python.

## Project Structure

The project contains two Python scripts to demonstrate different levels of complexity and best practices:

1.  **`scraper.py`**: The beginner-friendly script using standard libraries.
2.  **`scraper_pro.py`**: The advanced script incorporating Pandas, error handling, and data filtering.

---

## Prerequisites

You need Python 3 installed on your machine. You will also need to install the required external libraries.

### Installation

Open your terminal or command prompt and run:

```bash
pip install requests beautifulsoup4 pandas
```

*   `requests`: For fetching web pages.
*   `beautifulsoup4`: For parsing HTML.
*   `pandas`: For data manipulation and CSV export (Used in `scraper_pro.py`).

---

## File Descriptions

### 1. `scraper.py` (Basic Version)

This script is the starting point of the project. It demonstrates the fundamental workflow of web scraping: **Fetch, Parse, Extract, Save**.

**Features:**
*   Fetches the HTML content using the `requests` library.
*   Parses the HTML using `BeautifulSoup`.
*   Iterates through job cards to extract the Title, Company, Location, and URL.
*   Saves the data to a CSV file using Python's built-in `csv` module.

**Output:**
*   Creates a file named `jobs.csv` containing **all** job listings found on the page.

**Key Code Logic:**
*   Uses `soup.find_all()` to locate job containers.
*   Uses a standard file writer loop to append data to the CSV row by row.

---

### 2. `scraper_pro.py` (Advanced Version)

This script builds upon the basics by introducing industry-standard tools and robust coding practices. It is designed to be more reliable, secure, and useful for data analysis.

**Features:**
*   **User-Agent Spoofing:** Sets a `User-Agent` header in the request. This makes the script appear as a standard web browser (Chrome), reducing the likelihood of being blocked by anti-scraping measures.
*   **Data Filtering:** Includes logic to filter job results. Currently, it filters to only save jobs containing "Python" in the title.
*   **Error Handling:** Uses `try...except` blocks to handle network errors or missing HTML elements without crashing the entire script.
*   **Pandas Integration:** Uses the `pandas` library to organize data into a DataFrame before saving. This allows for cleaner data manipulation and analysis.
*   **Relative URL Handling:** Automatically fixes partial URLs (e.g., converting `/jobs/1` to `https://realpython.github.io/jobs/1`).

**Output:**
*   Creates a file named `python_jobs.csv` containing **only filtered** job listings.
*   Prints a preview of the data to the console.

**Key Code Logic:**
*   Filters data using `if "python" not in title.lower(): continue`.
*   Collects data into a list of dictionaries: `jobs_data.append({...})`.
*   Exports data efficiently: `df.to_csv(filename, index=False)`.

---

## Usage

### Running the Basic Scraper
To scrape all jobs and save them using the standard library:

```bash
python scraper.py
```

**Result:** Check for `jobs.csv` in your project folder.

### Running the Pro Scraper
To scrape only Python-related jobs with advanced error handling and Pandas:

```bash
python scraper_pro.py
```

**Result:** Check for `python_jobs.csv` in your project folder.

---

## Customization

### Changing the Filter in `scraper_pro.py`
To filter for different job types (e.g., "Senior" roles), open `scraper_pro.py` and modify the filtering logic inside the loop:

```python
# Change "python" to whatever keyword you prefer
if "senior" not in title.lower():
    continue
```

### Changing the Target URL
To scrape a different website, update the `url` variable at the top of either script. **Note:** You will need to inspect the new website's HTML structure and update the CSS class names (e.g., `card-content`, `title`, `company`) in the `soup.find()` methods accordingly.

---

## Future Improvements

Potential features to add for further learning:
*   **Pagination:** Modify the script to loop through multiple pages of results if the URL structure supports it (e.g., `page=1`, `page=2`).
*   **Command Line Arguments:** Use the `argparse` library to let users specify the filter keyword (e.g., `python scraper_pro.py --keyword "Engineer"`) from the terminal.
*   **Database Storage:** Instead of CSV, save the data to a SQLite or MongoDB database.
*   **Email Alerts:** Send an email notification when a new job matching specific criteria is posted.

## License

This project is open source and available for educational purposes.
```
