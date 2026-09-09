import requests
from bs4 import BeautifulSoup
import csv

# 1. Define the URL
url = "https://realpython.github.io/fake-jobs/"

# 2. Fetch the page
response = requests.get(url)

# Check if the request was successful (Status code 200)
if response.status_code == 200:
    print("Successfully fetched the page!")
    
    # 3. Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the container that holds all job cards
    # Based on the site structure, all jobs are inside div with class "column"
    # and the actual details are in div with class "card-content"
    results = soup.find(id="ResultsContainer")
    job_elements = results.find_all("div", class_="card-content")
    
    # Open a CSV file to write the data
    with open("jobs.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["Job Title", "Company", "Location", "URL"])
        
        # 4. Loop through each job element and extract data
        for job in job_elements:
            # Extract Title
            title_element = job.find("h2", class_="title")
            title = title_element.text.strip() if title_element else "N/A"
            
            # Extract Company
            company_element = job.find("h3", class_="company")
            company = company_element.text.strip() if company_element else "N/A"
            
            # Extract Location
            location_element = job.find("p", class_="location")
            location = location_element.text.strip() if location_element else "N/A"
            
            # Extract Link
            # The link is usually inside the 'title' h2 tag within an <a> tag
            link_element = job.find("a")
            # Handle relative URLs (e.g., /jobs/1) by adding the base domain
            link_url = "https://realpython.github.io" + link_element["href"] if link_element else "N/A"
            
            # Write the row to the CSV
            writer.writerow([title, company, location, link_url])
            
    print("Scraping complete. Data saved to jobs.csv")

else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")