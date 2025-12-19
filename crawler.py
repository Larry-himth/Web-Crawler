import requests, urllib.parse, time
from bs4 import BeautifulSoup as bs

to_visit = []
visited = set()

link = input("Paste the URL here:\n")
to_visit.append(link)

while(to_visit):
    current_link = to_visit.pop()
    
    if current_link in visited:
        continue
    try:
        r = requests.get(current_link)
    except requests.RequestException:
        continue
    
    visited.add(current_link)
    soup = bs(r.text, "html.parser")
    
    title = soup.title.string if soup.title else "No title"
    print(f"Title: {title}\n url: {current_link}\n")
    
    for a_tag in soup.find_all("a",href=True):
        href = a_tag["href"]
        
        next_url = urllib.parse.urljoin(current_link,href)
        
        if urllib.parse.urlparse(next_url).scheme in ["http","https"] and next_url not in visited:
            to_visit.append(next_url)
        
    time.sleep(1)