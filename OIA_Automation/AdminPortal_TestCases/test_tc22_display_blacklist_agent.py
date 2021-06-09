import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_display_blacklist_agent(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(10)
    agenten = driver.find_element(By.XPATH, "//a[text()=' Agenten ']")
    driver.execute_script("arguments[0].click();", agenten)
    log.info("Clicked on agenten")

    time.sleep(5)
    aktiv = driver.find_element(By.XPATH, '//button[text()="Aktiv"]')

    if aktiv.is_enabled():
        log.info("Filter on active agent already selected")
        driver.execute_script("arguments[0].click();", aktiv)

    else:
        log.info("Aktive not selected")

    blacklist = driver.find_element(By.XPATH, '//button[text()="Blacklist"]')
    driver.execute_script("arguments[0].click();", blacklist)
    log.info('Clicked on blacklist')
    time.sleep(5)

    try:
        Blacklistagent_notfound = driver.find_element(By.XPATH,
                                                      "(//article[text()='Keine Daten gefunden' and "
                                                      "@class='no-data'])[3]")
        log.info("Blacklist agent not found: " + Blacklistagent_notfound.text)

    except NoSuchElementException:
        log.info("Blacklist agents displayed successfully")
