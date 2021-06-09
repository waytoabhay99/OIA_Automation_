import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.AgentPortal_TestCases.test_logging import get_logger

def test_display_abgeschlossen_jobs(login):
    log = get_logger()
    driver = login
    time.sleep(5)
    job = driver.find_element(By.XPATH, '//a[text()=" Jobs "]')
    driver.execute_script("arguments[0].click();", job)
    log.info("Clicked on Jobs")

    time.sleep(3)
    abgeschlossen = driver.find_element(By.XPATH, '//button[text()="Abgeschlossen"]')
    driver.execute_script("arguments[0].click();", abgeschlossen)
    log.info("Clicked on filter option : abgeschlossen")
    time.sleep(5)

    try:
        abgeschlossenjobs_notfound = driver.find_element(By.XPATH,
                                                         "//div[@class ='text-center']//p[text()='Keine Daten gefunden']")
        log.info("Jobs in Abgeschlossen status not found ::" + abgeschlossenjobs_notfound.text)

    except NoSuchElementException:
        log.info("Clicked on abgeschlossen -- Filtered the jobs in abgeschlossen status")

