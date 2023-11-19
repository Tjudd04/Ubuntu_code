from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Ensure GUI is off
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
webdriver_service = Service()

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=options)

driver.get("http://www.google.com")
print(driver.title)

driver.quit()
