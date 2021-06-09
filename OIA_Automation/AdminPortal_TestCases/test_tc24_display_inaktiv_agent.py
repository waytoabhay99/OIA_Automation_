import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_display_inaktiv_agent(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(10)
    agenten = driver.find_element(By.XPATH, "//a[text()=' Agenten ']")
    driver.execute_script("arguments[0].click();", agenten)
    log.info("Clicked on agenten")

    time.sleep(5)
    Inactive = driver.find_element(By.XPATH, '//button[text()="Inaktiv"]')
    driver.execute_script("arguments[0].click();", Inactive)
    time.sleep(10)

    try:
        Inactiveagent_notfound = driver.find_element(By.XPATH,
                                                     "(//article[text()='Keine Daten gefunden' and "
                                                     "@class='no-data'])[3]")
        log.info("Inactive agent not found ::" + Inactiveagent_notfound.text)

    except NoSuchElementException:
        log.info("Inactive agents displayed successfully")
