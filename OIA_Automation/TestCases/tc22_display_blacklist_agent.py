import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def display_blacklist_agent(driver):
    agenten = driver.find_element(By.XPATH, "//a[text()=' Agenten ']")
    driver.execute_script("arguments[0].click();", agenten)
    print("Clicked on agenten")

    time.sleep(5)
    blacklist = driver.find_element(By.XPATH, '//button[text()="Blacklist"]')
    driver.execute_script("arguments[0].click();", blacklist)

    try:
        Blacklistagent_notfound = WebDriverWait(driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, "(//article[text()='Keine Daten gefunden' and @class='no-data'])[3]")))
        print("Blacklist agent not found :", Blacklistagent_notfound.text)

    except NoSuchElementException:
        print("Blacklist agents displayed successfully")


def main():
    driver = launchBrowser()
    login(driver)
    display_blacklist_agent(driver)

if __name__ == '__main__':
    main()
