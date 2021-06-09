import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_search_agent(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(5)
    agenten = driver.find_element(By.XPATH, "//a[text()=' Agenten ']")
    driver.execute_script("arguments[0].click();", agenten)
    log.info("Clicked on agenten")

    driver.implicitly_wait(20)
    driver.find_element(By.XPATH, '(//input[@name="searchTerm"])[2]').send_keys("A000003")
    time.sleep(3)

    order_notfound = len(driver.find_elements(By.XPATH,
                                             "(//article[text()='Keine Daten gefunden' and @class='no-data'])[3]"))
    log.info(order_notfound)
    if order_notfound == 0:
        log.info("No Data Displayed")
    else:
        log.info("Search results are displayed")
