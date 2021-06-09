from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def search_order(driver):
    driver.implicitly_wait(5)
    Aufträge = driver.find_element(By.XPATH, "//a[text()=' Aufträge ']")
    driver.execute_script("arguments[0].click();", Aufträge)
    print("Clicked on Aufträge/orders")

    driver.find_element(By.NAME, 'searchTerm').send_keys("200")
    try:
        order_notfound = driver.find_element(By.XPATH,
                                             "(//article[text()='Keine Daten gefunden' and @class='no-data'])[3]")
        print("No order found", order_notfound.text)
    except NoSuchElementException:
        print("Order is searched successfully")


def main():
    driver = launchBrowser()
    login(driver)
    search_order(driver)


if __name__ == '__main__':
    main()
