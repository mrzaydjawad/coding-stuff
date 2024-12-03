import os
import requests
from bs4 import BeautifulSoup
import re
from time import sleep

def create_directory(directory_name):
    """Create a directory if it does not exist."""
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

def is_valid_file(file_path, file_type):
    """Check if the downloaded file is valid by checking the file type."""
    try:
        with open(file_path, 'rb') as f:
            header = f.read(4)  # Read the first 4 bytes to check the file type
            if file_type == 'pdf' and header[:4] == b'%PDF':
                return True
            elif file_type == 'doc' and header[:2] == b'\xd0\xcf':  # DOC files start with 0xD0 0xCF (MS Office formats)
                return True
            else:
                print(f"Invalid file: {file_path}")
                return False
    except Exception as e:
        print(f"Error checking file validity: {e}")
        return False

def download_file(url, save_path, retries=3):
    """Download a file from a URL and save it to a specified path."""
    try:
        # Retry logic in case of temporary issues
        for attempt in range(retries):
            print(f"Downloading {url} (Attempt {attempt + 1}/{retries})")
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, stream=True, allow_redirects=True)
            
            # Ensure the response is valid
            response.raise_for_status()

            # Get content length (if available) to validate download size
            content_length = response.headers.get('Content-Length')

            # Write the file in chunks to avoid memory overload
            with open(save_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)

            # Validate file size and type
            if content_length:
                downloaded_size = os.path.getsize(save_path)
                if int(content_length) != downloaded_size:
                    print(f"Warning: Downloaded file size doesn't match the expected size for {url}")
                    os.remove(save_path)  # Remove the incomplete file
                    return False

            # Check if the file is valid
            if is_valid_file(save_path, 'pdf' if save_path.endswith('.pdf') else 'doc'):
                print(f"Downloaded successfully: {save_path}")
                return True
            else:
                print(f"Downloaded file is corrupted: {save_path}")
                os.remove(save_path)  # Remove the corrupted file

            # Sleep before retrying
            sleep(2)

        print(f"Failed to download after {retries} attempts: {url}")
        return False
    
    except PermissionError as e:
        print(f"PermissionError: Cannot write to {save_path}. {e}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")
    return False

def scrape_past_papers(base_url, output_dir):
    """Scrape all DOC and PDF links from the website and download them."""
    try:
        next_page = base_url
        downloaded_urls = set()  # Set to keep track of downloaded URLs

        while next_page:
            print(f"Scraping: {next_page}")
            response = requests.get(next_page, headers={'User-Agent': 'Mozilla/5.0'})
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all links
            links = soup.find_all('a', href=True)
            for link in links:
                href = link['href']
                if href and (href.endswith('.doc') or href.endswith('.pdf')):  # Filter for .doc and .pdf files
                    full_url = href if href.startswith('http') else f"{base_url.rstrip('/')}/{href.lstrip('/')}"

                    # Skip if the file is already downloaded
                    if full_url in downloaded_urls:
                        print(f"Skipping duplicate file: {full_url}")
                        continue

                    # Add URL to the set to prevent duplicates
                    downloaded_urls.add(full_url)

                    # Sanitize the filename
                    filename = re.sub(r'[<>:"/\\|?*]', '_', href.split('/')[-1])
                    save_path = os.path.join(output_dir, filename)
                    
                    # Download the file
                    download_file(full_url, save_path)

            # Pagination logic: Find the "Next Page" link
            next_page_tag = soup.find('a', string=lambda x: x and "Next" in x)  # Adjust based on the website structure
            next_page = None
            if next_page_tag:
                next_href = next_page_tag['href']
                next_page = next_href if next_href.startswith('http') else f"{base_url.rstrip('/')}/{next_href.lstrip('/')}"

        print("Scraping completed.")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {base_url}: {e}")

if __name__ == "__main__":
    base_url = "https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-o-level-pakistan-studies-2059/past-papers/"  # Replace with actual URL
    output_dir = "e:\docs\past papers"  # Change this to your desired save location

    create_directory(output_dir)
    scrape_past_papers(base_url, output_dir)
