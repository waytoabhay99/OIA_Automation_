import time
from selenium.webdriver.common.by import By
from ImmoAgent.AgentPortal_TestCases.test_logging import get_logger

def test_display_offen_bills(login):
    log = get_logger()
    driver = login
    # click_Rechnungen()
    rechnungen = driver.find_element(By.XPATH, '//a[text()=" Rechnungen "]')
    driver.execute_script("arguments[0].click();", rechnungen)
    log.info("Clicked on Rechnungen ")
    time.sleep(5)

    try:
        no_data = driver.find_element(By.XPATH, '// p[text() = "Keine Daten gefunden"]')
        log.info("Data not found::" + no_data.text)

    except:
        offen = driver.find_element(By.XPATH, '//button[text()="Offen"]')
        driver.execute_script("arguments[0].click();", offen)
        log.info("Clicked on offen -- Filtered the bills in offen status")

