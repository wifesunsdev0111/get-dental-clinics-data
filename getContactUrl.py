import re
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


# URL to fetch HTML content from
def available_urls(url, key):
    # key = "contact"
    # url =  "https://cameronstationdentalcare.com"
    # # driver = webdriver.Chrome()
    # driver.maximize_window()
    # url = "https://cameronstationdentalcare.com"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    html_content = str(soup.find_all())
    pattern = rf"{url}[\w\-\./?=&]+"

    urls = re.findall(pattern, html_content)
    unique_urls = set(urls)
    unique_urls.add(url)

    # for index_url in re.findall(r'href="([^"]+)"', html_content):
    #     complete_url = urljoin(url, index_url)
    #     unique_urls.add(complete_url)
    if key == "name":
        keywords = ["doctor", "meet", "provider", "team", "about", "staff"]
    else:
         keywords = ["contact"]

    for index_url in re.findall(r'href="([^"]+)"', html_content):
  
        complete_url = urljoin(url, index_url)
        if any(keyword in complete_url for keyword in keywords):
            unique_urls.add(complete_url)


    # unique_urls = set(urls)
    # print(unique_urls)

    filtered_urls = [
        url for url in unique_urls
        if not re.search(r"\.[a-zA-Z0-9]+$", url) and any(keyword in url for keyword in keywords)
    ]
    # filtered_urls.append(url)
    print(filtered_urls)
    return filtered_urls

# available_urls()
