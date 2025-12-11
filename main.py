from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

##Getting driver connection
def get_driver():
  #Using scromeoptions to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("diable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_argument("disable-blink-features=AutomationControlled")
  options.add_experimental_option("excludeSwitches",["enable-automation"])

  driver = webdriver.Chrome(options=options)
  #Establishing connection
  driver.get("https://automated.pythonanywhere.com/login")
  return driver

def main():
  driver = get_driver()
  time.sleep(2)
  #logging in
  driver.find_element(by="id",value="id_username").send_keys("automated")
  driver.find_element(by ="id",value = "id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(2)
  #submitting
  driver.find_element(by="xpath",value = "/html/body/nav/div/a").click()
  time.sleep(2)

  homeUrl = driver.current_url
  print(homeUrl)
  
  #Extratcing content from home page 
  element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[2]")
  output = float(element.text.split(": ")[1])
  print(output)
  print("end**************")

  
main()