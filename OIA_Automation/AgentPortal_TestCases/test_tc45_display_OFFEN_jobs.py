import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.AgentPortal_TestCases.test_logging import get_logger

def test_display_offen_jobs(login):
    log = get_logger()
    driver = login
    job = driver.find_element(By.XPATH, '//a[text()=" Jobs "]')
    driver.execute_script("arguments[0].click();", job)
    log.info("Clicked on Jobs")
    time.sleep(3)

    offen = driver.find_element(By.XPATH, '//button[text()="Offen"]')
    driver.execute_script("arguments[0].click();", offen)
    log.info("Clicked on filter option : offen")
    time.sleep(5)

    try:
        offenjobs_notfound = driver.find_element(By.XPATH,
                                                 '//div[@class ="text-center"]//p[text()="Keine Daten gefunden"]]')
        log.info("Jobs in Offen status not found ::", +offenjobs_notfound.text)

    except NoSuchElementException:
        log.info("Clicked on Offen -- Filtered the jobs in offen status")

