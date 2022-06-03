import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

serv_obj= Service("C:\Drivers\chromedriver_win32\chromedriver")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

#INITIATE A SEARCH

driver.get("https://www.justpark.com/")
driver.maximize_window()

#INPUT LOCATION
driver.find_element(By.XPATH, "//input[@id='search-box']").send_keys("London uk")
time.sleep(3)
act=ActionChains(driver)
act.send_keys(Keys.ENTER).perform()

#ARRIVAL DATE AND TIME
driver.find_element(By.XPATH,"//span[@data-cy='booking-start-date']").click()
arrivalDay=driver.find_element(By.XPATH,"//td[@aria-label='Saturday, June 4, 2022']")
arrivalDay.click()

arrivalTime=driver.find_element(By.XPATH,"//li[contains(text(),'11')]")
arrivalTime.click()

driver.find_element(By.XPATH,"//a[normalize-space()='Done']").click()

#DEPARTURE DATE AND TIME
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/div/div/div/div[2]/form/div[3]/div/div[2]/div/span").click()

departureDay=driver.find_element(By.XPATH,"//td[@aria-label='Thursday, June 30, 2022']")
departureDay.click()

departureTime=driver.find_element(By.XPATH,"//li[normalize-space()='11']")
departureTime.click()

driver.find_element(By.XPATH,"//a[normalize-space()='Done']").click()

driver.find_element(By.XPATH,"//button[normalize-space()='Show parking spaces']").click()

driver.save_screenshot("MonthlySaverModalDisplayed#1.png")

#MONTHLY SAVER MODAL
#driver.find_element(By.XPATH,"//span[normalize-space()='Use my current dates']").click()
driver.find_element(By.XPATH,"//span[normalize-space()='Switch to monthly parking']").click()

driver.save_screenshot("RollingMonthlySearchDisplayed#2.png")

expectedTitle= "London Parking | Guaranteed Spaces"
actualTitle= driver.title
if expectedTitle==actualTitle:
    print("Test Case for Rolling Monthly Saver is Successful")
else:
    print("Test Failed")

driver.close()