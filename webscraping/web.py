import requests
from bs4 import BeautifulSoup
def fetch_page(url):
      try:
            respone =requests.get(url)
            respone.raise_for_status()
            return respone.text
      except requests.RequestException as e:
            print(f"error feching {url} :{e}")
def parse_page(content):
        soup =BeautifulSoup(content,"html.parser")
        results =[]
        for a_tage in soup.find_all("a",href =True):
              title =a_tage.get_text().strip()
              link = a_tage['href']
              results.append((title,link))
        return results

def scrape_web(url):
      print(f"starting scrape for {url}")
      page_content =fetch_page(url)

      if not page_content:
            print(f"faild to retrive content from {url}")
      parsed_data =parse_page(page_content)
      print(f"Scraping complete for {url}. Found{len(parsed_data)} links .")
      for title,link in parsed_data:
            print(f"Titale: {title}, Link: {link}")
if __name__ == "__main__":
      url = input("please enter the target website")
      scrape_web(url) 