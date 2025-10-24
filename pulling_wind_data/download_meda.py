from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# List of URNs
with open("urn_list.txt", "r") as f:
    urns = [line.strip() for line in f if line.strip()]

# Set up Chrome options to automatically download to a folder
download_dir = os.path.join(os.getcwd(), "downloads")
os.makedirs(download_dir, exist_ok=True)

options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_dir}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)
driver.get("https://pds-atmospheres.nmsu.edu/data_and_services/atmospheres_data/PERSEVERANCE/retrieving_mars2020.html")
time.sleep(2)

textarea = driver.find_element(By.ID, "filename")
view_link = driver.find_element(By.XPATH, '//a[text()="View Data"]')

for urn in urns:
    print(f"Processing {urn}...")

    textarea = driver.find_element(By.ID, "filename")
    view_link = driver.find_element(By.XPATH, '//a[text()="View Data"]')

    textarea.clear()
    textarea.send_keys(urn)
    view_link.click()
    
    time.sleep(1)  

driver.quit()
print("All URNs processed!")
