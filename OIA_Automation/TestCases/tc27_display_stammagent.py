import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def display_stammagent(driver):
    driver.implicitly_wait(20)
    agenten = driver.find_element(By.XPATH, "//a[text()=' Agenten ']")
    driver.execute_script("arguments[0].click();", agenten)
    print("Clicked on agenten")

    time.sleep(5)
    Stammagent = driver.find_element(By.XPATH, '//button[text()="Stammagent"]')
    driver.execute_script("arguments[0].click();", Stammagent)
    time.sleep(10)

    try:
        Stammagent_notfound = driver.find_element(By.XPATH,
                                                  "(//article[text()='Keine Daten gefunden' and @class='no-data'])[3]")
        print("Inactive agent not found: ", Stammagent_notfound.text)
    except NoSuchElementException:
        print("Stammagent displayed successfully")


def main():
    driver = launchBrowser()
    login(driver)
    display_stammagent(driver)

if __name__ == '__main__':
    main()
