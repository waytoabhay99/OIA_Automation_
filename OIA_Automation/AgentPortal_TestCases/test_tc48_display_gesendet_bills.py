import time
from selenium.webdriver.common.by import By
from ImmoAgent.AgentPortal_TestCases.test_logging import get_logger

def test_display_gesendet_bills(login):
    log = get_logger()
    driver = login
    time.sleep(10)
    # click_Rechnungen()
    rechnungen = driver.find_element(By.XPATH, '//a[text()=" Rechnungen "]')
    driver.execute_script("arguments[0].click();", rechnungen)
    log.info("Clicked on Rechnungen ")
    time.sleep(5)

    try:
        no_data = driver.find_element(By.XPATH, '// p[text() = "Keine Daten gefunden"]')
        log.info("Data not found::" + no_data.text)

    except:
        gesendet = driver.find_element(By.XPATH, '//button[text()="Gesendet"]')
        driver.execute_script("arguments[0].click();", gesendet)
        log.info("Clicked on Gesendet -- Filtered the bills in Gesendet status")
        time.sleep(3)
