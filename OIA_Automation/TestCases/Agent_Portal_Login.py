from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

option = Options()
option.add_argument("--disable-notifications")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
driver.get("https://oiaagentqa.z6.web.core.windows.net/login")
driver.maximize_window()
# To click on register
driver.implicitly_wait(10)
Register = driver.find_element(By.XPATH, '//button[@class="btn secondary-button mr-3 text-uppercase"]')
driver.execute_script("arguments[0].click();", Register)
print("Clicked on Register")

driver.find_element(By.XPATH, '//input[@placeholder ="max.mustermann@mail.com"]').send_keys(
    "revasharma0692+3@gmail.com")
driver.find_element(By.XPATH, '//input[@formcontrolname="password"]').send_keys("Test@1234")
driver.find_element(By.XPATH, '//input[@formcontrolname="confirmPassword"]').send_keys("Test@1234")
print('Entered id and passowrd')
driver.quit()
