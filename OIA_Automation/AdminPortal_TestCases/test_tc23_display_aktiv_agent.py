import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_display_aktiv_agent(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(20)
    agenten = driver.find_element(By.XPATH, "//a[text()=' Agenten ']")
    driver.execute_script("arguments[0].click();", agenten)
    log.info("Clicked on agenten")

    time.sleep(12)
    Active = driver.find_element(By.XPATH, '//button[text()="Aktiv"]')

    if Active.is_enabled():
        log.info("Filter on active agent already selected")

    else:
        driver.execute_script("arguments[0].click();", Active)
        log.info("Filter on active agent selected now")

    try:
        Activeagent_notfound = driver.find_element(By.XPATH,
                                                   "(//article[text()='Keine Daten gefunden' and @class='no-data'])[3]")
        log.info("Active agent not found ::"+ Activeagent_notfound.text)

    except NoSuchElementException:
        log.info("Active agents displayed successfully")
