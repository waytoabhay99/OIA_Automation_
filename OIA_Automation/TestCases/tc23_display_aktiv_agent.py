import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def display_aktiv_agent(driver):
    driver.implicitly_wait(20)
    agenten = driver.find_element(By.XPATH, "//a[text()=' Agenten ']")
    driver.execute_script("arguments[0].click();", agenten)
    print("Clicked on agenten")

    time.sleep(5)
    Active = driver.find_element(By.XPATH, '//button[text()="Aktiv"]')
    driver.execute_script("arguments[0].click();", Active)
    time.sleep(10)

    try:
        Activeagent_notfound = driver.find_element(By.XPATH,
                                                   "(//article[text()='Keine Daten gefunden' and @class='no-data'])[3]")
        print("Active agent not found ::", Activeagent_notfound.text)

    except NoSuchElementException:
        print("Active agents displayed successfully")


def main():
    driver = launchBrowser()
    login(driver)
    display_aktiv_agent(driver)

if __name__ == '__main__':
    main()
