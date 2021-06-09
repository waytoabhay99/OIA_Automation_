import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def display_inaktiv_agent(driver):
    agenten = driver.find_element(By.XPATH, "//a[text()=' Agenten ']")
    driver.execute_script("arguments[0].click();", agenten)
    print("Clicked on agenten")

    time.sleep(5)
    Inactive = driver.find_element(By.XPATH, '//button[text()="Inaktiv"]')
    driver.execute_script("arguments[0].click();", Inactive)
    time.sleep(10)

    try:
        Inactiveagent_notfound = driver.find_element(By.XPATH,
                                                     "(//article[text()='Keine Daten gefunden' and "
                                                     "@class='no-data'])[3]")
        print("Inactive agent not found ::", Inactiveagent_notfound.text)

    except NoSuchElementException:
        print("Inactive agents displayed successfully")


def main():
    driver = launchBrowser()
    login(driver)
    display_inaktiv_agent(driver)

if __name__ == '__main__':
    main()
