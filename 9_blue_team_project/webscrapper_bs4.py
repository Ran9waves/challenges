from bs4 import requests #communicates with web servers using HTTP
import BeautifulSoup4 #parses HTML documents
URL = "https://letsdefend.io" #target website
page = requests.get(URL) #sends a GET request to the target website
soup = BeautifulSoup4 (page.content,"html.parser") #parses the HTML content of the page
results = soup.find("meta",{"name":"description"}) #extracts the content of the meta description tag
results = results["content"] #prints the extracted content
print(results)