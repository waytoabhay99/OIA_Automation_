import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.AgentPortal_TestCases.test_logging import get_logger

def test_display_angenommen_jobs(login):
    log = get_logger()
    driver = login
    job = driver.find_element(By.XPATH, '//a[text()=" Jobs "]')
    driver.execute_script("arguments[0].click();", job)
    log.info("Clicked on Jobs")
    time.sleep(3)

    angenommen = driver.find_element(By.XPATH, '//button[text()="Angenommen"]')
    driver.execute_script("arguments[0].click();", angenommen)
    log.info("Clicked on filter option : angenommen")
    time.sleep(5)
    try:
        angenommenjobs_notfound = driver.find_element(By.XPATH, '//div[@class ="text-center"]')
        log.info("Jobs in Angenommen status not found ::" + angenommenjobs_notfound.text)

    except NoSuchElementException:
        log.info("Clicked on Angenommen -- Filtered the jobs in angenommen status")

