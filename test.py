from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set Chrome options to run in headless mode
chrome_options = Options()

chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model (useful for running in containers)

# Ensure ChromeDriver is correctly downloaded and set up
chrome_driver_path = ChromeDriverManager().install()
print(chrome_driver_path)
# Correctly setup the ChromeDriver Service
service = Service()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Specify the URL of the website
    url = 'https://batdongsan.com.vn/ban-nha-rieng-duong-ngo-tat-to-phuong-22/ban-nguyen-huu-canh-giap-q1-60m-gia-5-6-ty-pr40633937'  # Replace with the website you want to download content from

    # Open the website
    driver.get(url)
    time.sleep(5)
    # Get the page source (HTML content)
    page_content = driver.page_source

    # Save the content to a text file
    with open('website_content_alonhadat.txt', 'w', encoding='utf-8') as file:
        file.write(page_content)

    print('Website content saved to "website_content.txt"')

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
