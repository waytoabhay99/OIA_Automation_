import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_display_stammagent(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(20)
    agenten = driver.find_element(By.XPATH, "//a[text()=' Agenten ']")
    driver.execute_script("arguments[0].click();", agenten)
    log.info("Clicked on agenten")

    time.sleep(5)
    Stammagent = driver.find_element(By.XPATH, '//button[text()="Stammagent"]')
    driver.execute_script("arguments[0].click();", Stammagent)
    time.sleep(10)

    try:
        Stammagent_notfound = driver.find_element(By.XPATH,
                                                  "(//article[text()='Keine Daten gefunden' and @class='no-data'])[3]")
        log.info("Stammagent agent not found: " + Stammagent_notfound.text)
    except NoSuchElementException:
        log.info("Stammagent displayed successfully")
