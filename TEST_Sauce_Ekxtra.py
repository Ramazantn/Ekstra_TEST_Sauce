
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
import openpyxl
from selenium.webdriver.support.select import Select



##### Sauce Demo Stesinde Filtreleme Görüntüleri İle Ürün İsim ve iyatlarının Test Edilmesi####   
#Not: Pytest kullanılmadan yazılmıstır...



driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.CLASS_NAME, "product_sort_container")
sleep(3)
#Yapılacak Secim İsleminin Opsiyonlarının Gösterilmesi
dropdown=driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/span/select")
urun=Select(dropdown)
urun_sort=urun.options
for tip in urun_sort:
    print(tip.text)
    sleep(5)

print("----------------------------------------------------------------------------------------")
# Sitede A>Z Seklinde Yapılan Filtreleme Listesinin Görüntüsü ve Listenin İlk Ürünün İsmi ve Fiyatının Cıktısı
price_A_to_Z=driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select/option[1]")
price_A_to_Z.click()
driver.save_screenshot("./1.png")
List_Of_One=driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div")
Name=List_Of_One.text
List_Of_One=driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div")
Preis=List_Of_One.text
print(f"*{Name}*  :  {Preis}") 


# Sitede Z>A Seklinde Yapılan Filtreleme Listesinin Görüntüsü ve Listenin İlk Ürünün İsmi ve Fiyatının Cıktısı
price_Z_to_A=driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/span/select/option[2]")
price_Z_to_A.click()
sleep(3)
driver.save_screenshot("./2.png")
driver.find_element(By.CLASS_NAME, "product_sort_container")
List_Of_Two=driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div")
Name2=List_Of_Two.text
List_Of_Two=driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div")
Preis2=List_Of_Two.text
print(f" *{Name2}* : {Preis2}  ") 


# Sitede low_to_high Seklinde Yapılan Filtreleme Listesinin Görüntüsü ve Listenin İlk Ürünün İsmi ve Fiyatının Cıktısı
price_low_to_high=driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select/option[3]")
price_low_to_high.click()
sleep(3)
driver.save_screenshot("./3.png")
List_Of_Three=driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div")
Name3=List_Of_Three.text
List_Of_Three=driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div")
Preis3=List_Of_Three.text
print(f" *{Name3}* : {Preis3}  ") 

# Sitede high_to_low Seklinde Yapılan Filtreleme Listesinin Görüntüsü ve Listenin İlk Ürünün İsmi ve Fiyatının Cıktısı
price_high_to_low=driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/span/select/option[4]")
price_high_to_low.click()
driver.save_screenshot("./4.png")
sleep(3)
List_Of_Four=driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div")
Name4=List_Of_Four.text
List_Of_Four=driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div")
Preis4=List_Of_Four.text
print(f" *{Name4}* : {Preis4}  ") 

