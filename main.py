from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import PATH
import time
import os 
from listening import l

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    executable_path=PATH,
    options=options,

)



url = "https://webtopdf.com/"

try:
    driver.get(url=url)
    def a():
        for i in range(len(l)):
            f = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/section[2]/div[1]/div[1]/input")
            f.send_keys(f"{l[i]}")
            driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/section[2]/div[1]/div[2]/button[2]").click()
            time.sleep(27)
            driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/section[2]/div[1]/div[2]/div[1]/div[2]/a/img").click()
            time.sleep(7)
            driver.find_element(By.XPATH, "/html/body/form/div[3]/div[1]/header/div/div[1]/a/img").click()
            time.sleep(3)
            
    a()
    

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
