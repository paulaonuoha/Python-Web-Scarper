import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. CONFIGURATION
url = "https://realpython.github.io/fake-jobs/"
base_url = "https://realpython.github.io"

# 2. HEADERS (Mimic a real browser)
# This prevents the website from blocking the script immediately.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

def main():
    print("Fetching webpage...")
    
    # 3. REQUEST WITH HEADERS
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Check for HTTP errors (like 404 or 500)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return

    # 4. PARSE HTML
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    job_elements = results.find_all("div", class_="card-content")

    # List to hold all job data before converting to DataFrame
    jobs_data = []

    print(f"Found {len(job_elements)} job postings. Extracting data...")

    # 5. LOOP, FILTER, AND EXTRACT
    for job in job_elements:
        try:
            # --- Extraction ---
            title_element = job.find("h2", class_="title")
            company_element = job.find("h3", class_="company")
            location_element = job.find("p", class_="location")
            link_element = job.find("a")

            # Get text safely
            title = title_element.text.strip() if title_element else "N/A"
            company = company_element.text.strip() if company_element else "N/A"
            location = location_element.text.strip() if location_element else "N/A"
            
            # Handle relative URLs (e.g., /jobs/123 -> https://site.com/jobs/123)
            link_url = base_url + link_element["href"] if link_element else "N/A"

            # --- FILTERING LOGIC ---
            # CHANGE THIS: Modify the string below to filter for different jobs
            # Example: if "Senior" in title: ...
            if "python" not in title.lower():
                continue  # Skip this job if it doesn't have "python" in the title

            # --- DATA COLLECTION ---
            jobs_data.append({
                "Job Title": title,
                "Company": company,
                "Location": location,
                "Apply Link": link_url
            })

        except AttributeError:
            # This handles cases where a specific tag (like h2 or h3) is missing
            print("Skipping a job card due to missing data.")
            continue

    # 6. SAVE WITH PANDAS
    if jobs_data:
        df = pd.DataFrame(jobs_data)
        
        # Print a preview to the console
        print("\n--- Preview of Scraped Data ---")
        print(df.head())
        
        # Save to CSV
        filename = "python_jobs.csv"
        df.to_csv(filename, index=False)
        print(f"\nSuccessfully saved {len(jobs_data)} jobs to '{filename}'.")
    else:
        print("No jobs matched your filter criteria.")

if __name__ == "__main__":
    main()