import time
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_search_order_history(login):
    log = get_logger()
    driver = login
    cust = driver.find_element(By.CSS_SELECTOR, '[href="/customers"]')
    driver.execute_script("arguments[0].click();", cust)
    log.info("Clicked on Kunden")

    firstCust = driver.find_element(By.XPATH, '(//i[@class="fas fa-chevron-right"])[3]')
    firstCust.click()
    log.info('Open 1st customer details')
    time.sleep(3)

    history = driver.find_element(By.CSS_SELECTOR, "section[class='text-center text-uppercase deselected-tab mr-4 "
                                                   "px-3 py-2 cursor']")
    driver.execute_script("arguments[0].click();", history)
    log.info('Clicked on history')
    time.sleep(2)
    custName = driver.find_element(By.CSS_SELECTOR, 'div[class="heading"]')
    noDataFound = len(driver.find_elements(By.ID, "uname"))
    if noDataFound == 0:
        log.info('No order found for - ' + custName.text)
    else:
        log.info('Order history displayed for - ' + custName.text)
        orderCount = driver.find_elements(By.ID, "uname")
        for x in range(len(orderCount)):
            log.info(orderCount[x].text)
        log.info('Total number of orders found: ' + str(len(orderCount)))
