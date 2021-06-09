import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from ImmoAgent.Resuables.test_logging import get_logger


def test_download_reports(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(5)

    Aufträge = driver.find_element(By.XPATH, "//a[text()=' Aufträge ']")
    driver.execute_script("arguments[0].click();", Aufträge)
    log.info("Clicked on Aufträge/orders")

    time.sleep(10)
    search = driver.find_element(By.XPATH,
                                 "//input[@name='searchTerm' and @placeholder='Aufträge durchsuchen']")
    search.send_keys("210246_0003")

    try:
        order_notfound = driver.find_element(By.XPATH,
                                             "(//article[text()='Keine Daten gefunden' and @class='no-data'])[3]")
        log.info("Invalid Order Number::" + order_notfound.text)

    except NoSuchElementException:
        log.info("Order is searched successfully")

    chevron1 = driver.find_element(By.XPATH, "(//i[@class='fas fa-chevron-right'])[1]")
    driver.execute_script("arguments[0].click();", chevron1)
    log.info("Clicked on chevron1 --Navigated inside the order")

    time.sleep(20)

    status_dropdown = driver.find_element(By.XPATH, "//label[@class='form-label-header']/following-sibling::select")
    status = Select(status_dropdown)

    status.select_by_value('abgeschlossen')
    log.info("Status changed successfully")

    status1 = len(driver.find_elements(By.ID, 'toast-container'))

    if status1 > 0:
        log.info(driver.find_element(By.ID, 'toast-container').text)

    else:
        log.info("Something went wrong ::Unable to change the status")

    time.sleep(4)
    # driver.find_element(By.XPATH, "//span[text()=' Alle Ergebnisse herunterladen ']").click()
    # # driver.find_element(By.XPATH,"//button[text()='Ergebnisse herunterladen']").click()
    # print("Report downloaded successfully")

    driver.find_element(By.XPATH, "//button[text()='Download Auftragsinformationen']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//span[text()=' Alle Ergebnisse herunterladen ']").click()
    time.sleep(10)
    log.info("Report downloaded successfully")
