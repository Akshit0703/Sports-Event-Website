from bs4 import BeautifulSoup
from selenium import webdriver

   # Initialize the webdriver
driver = webdriver.Chrome()  # Or webdriver.Firefox()

   # Load the dynamic website
driver.get("https://www.goal.com/en-in/live-scores")

   # Wait for the JavaScript to load (adjust time as needed)
driver.implicitly_wait(10)  

   # Get the page source after JavaScript execution
page_source = driver.page_source

   # Parse the HTML with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")
print(soup)

   # Extract data using BeautifulSoup as usual
data = soup.find_all("a", class_="competition_name__O93QA")
for dataitem in data:
    print(dataitem.text)

   # Close the browser
driver.quit()
