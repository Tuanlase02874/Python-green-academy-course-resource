import requests
from bs4 import BeautifulSoup
import json
import time

# Function to fetch the webpage content with a User-Agent header
def fetch_page_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None

# Function to parse the webpage and extract data
def menu_cooking_parse_product_data(html_content):
    #print(html_content)  # Added line to print the raw HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    #print(soup.prettify())
    # List to store the extracted data
    products = []
    
    # Example selector (need to adjust based on the webpage structure)
    product_containers = soup.find_all('div', class_='menu-cooking topmenu')
    print("product_containers:", product_containers)
    for container in product_containers:
        # Find all anchor tags within the container
        for link_tag in container.find_all('a', href=True):
            # Extract the image source
            img_tag = link_tag.find('img', src=True)
            if img_tag:
                img_src = img_tag['src']
                # Extract the link
                product_link = link_tag['href']
                # Add extracted data to the list
                products.append({
                    'Image Source': img_src,
                    'Product Link': product_link
                })

    return products

# Main function to execute the web crawler
def main():
    url = "https://www.dienmayxanh.com/vao-bep/mon-canh"
    html_content = fetch_page_content(url)
    
    
    if html_content:
        menu_cooking_dict = menu_cooking_parse_product_data(html_content)
        # Convert the list of products to JSON format
        with open('menu_cooking_dict.json', 'w', encoding='utf-8') as f:
            json.dump(menu_cooking_dict, f, ensure_ascii=False, indent=4)
        print("Data extraction completed. Output saved to 'products.json'.")

if __name__ == "__main__":
    main()
    # Implement a delay to prevent overloading the server (polite scraping)
    time.sleep(2)
