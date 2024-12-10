from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (update the path to the WebDriver executable)
driver = webdriver.Chrome()

store_website = 'https://www.skechers.id/storelocator'

try:
    # Load the webpage
    driver.get(store_website)

    # Wait for the page to load completely
    time.sleep(5)  # You can use WebDriverWait for better control over waiting

    # Find the button using its properties (adjust the selector as needed)
    # button = driver.find_element(By.XPATH, '//li[@data-filter="active-kids-en"]')  # Change the selector accordingly
    # Simulate clicking the button
    # button.click()
    # Wait for the content to load (if applicable)
    # time.sleep(0.5)

    # Now, scrape the page after the button is clicked
    page_source = driver.page_source
    # Use BeautifulSoup to parse the new page
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract the desired information
    # Use appropriate selectors based on the updated content
    extracted_data = soup.find_all('article')
    
    for item in extracted_data:
        print(item.text)

finally:
     driver.quit()  # Close the browser when done