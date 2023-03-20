from selenium import webdriver
from selenium.webdriver.common.by import By
from config import PATH
import time
import os 


options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    executable_path=PATH,
    options=options,

)

l = []

url = "https://www.w3schools.com/html/default.asp"

try:
    driver.get(url=url)
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/a[25]").click()
    def a():
        driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/div[1]/div[2]/a[2]").click()
        l.append(driver.current_url)
    for i in range(100):
        a()
    
    

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
    
