import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def search_cust(driver):
    cust = driver.find_element(By.XPATH, "//a[text()=' Kunden ']")
    driver.execute_script("arguments[0].click();", cust)
    print("Clicked on customer")
    time.sleep(10)
    driver.find_element(By.NAME, 'searchTerm').send_keys("Mike Davidson")
    time.sleep(10)

    try:
        agent_notfound = driver.find_element(By.XPATH,
                                             "(//article[text()='Keine Daten gefunden' and @class='no-data'])[3]")
        print("Customer not found::", agent_notfound.text)

    except NoSuchElementException:
        print("Customer search result displayed")


def main():
    driver = launchBrowser()
    login(driver)
    search_cust(driver)


if __name__ == '__main__':
    main()
