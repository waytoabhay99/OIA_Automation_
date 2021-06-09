import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def search_agent(driver):
    driver.implicitly_wait(5)
    agenten = driver.find_element(By.XPATH, "//a[text()=' Agenten ']")
    driver.execute_script("arguments[0].click();", agenten)
    print("Clicked on agenten")
    driver.implicitly_wait(20)
    driver.find_element(By.NAME, 'searchTerm').send_keys("A000003")
    time.sleep(10)
    try:
        order_notfound = driver.find_element(By.XPATH,
                                             "(//article[text()='Keine Daten gefunden' and @class='no-data'])[3]")
        print("Invalid Order Number::", order_notfound.text)

    except NoSuchElementException:
        print("Search results are displayed")


def main():
    driver = launchBrowser()
    login(driver)
    search_agent(driver)


if __name__ == '__main__':
    main()
