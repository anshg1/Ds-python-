import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Initialize the queue and stack with the starting URL
start_url = "https://en.m.wikipedia.org/wiki/Discrete_mathematics"
queue = [start_url]
stack = []

# Set the maximum number of pages to crawl
max_pages = 20
crawled_pages = 0

while queue and crawled_pages < max_pages:
    # Get the next URL from the queue
    current_url = queue.pop(0)

    # Fetch the content of the current page
    response = requests.get(current_url)
    if response.status_code != 200:
        continue

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Process the page content here (e.g., scraping data, saving files, etc.)

    # Add the current URL to the stack to keep track of the traversal path
    stack.append(current_url)

    # Find and add all linked URLs to the queue
    for link in soup.find_all('a'):
        next_url = link.get('href')
        if next_url and next_url.startswith('http'):
            next_url = urljoin(current_url, next_url)
            if next_url not in stack and next_url not in queue:
                queue.append(next_url)

    # Increment the crawled pages counter
    crawled_pages += 1

# Print the traversal path (stack) for demonstration purposes
print("Traversal Path:")
for url in stack:
    print(url)
