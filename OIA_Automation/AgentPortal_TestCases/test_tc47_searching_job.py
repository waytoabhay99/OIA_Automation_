import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.AgentPortal_TestCases.test_logging import get_logger

def test_search_job(login):
    log = get_logger()
    driver = login
    time.sleep(10)

    # #Click on jobs
    driver.maximize_window()
    driver.implicitly_wait(5)
    job = driver.find_element(By.XPATH, '//a[text()=" Jobs "]')
    driver.execute_script("arguments[0].click();", job)
    log.info("Clicked on Jobs")
    time.sleep(5)

    try:
        no_data = driver.find_element(By.XPATH, '// p[text() = "Keine Daten gefunden"]')
        log.info("Data not found::" + no_data.text)

    except NoSuchElementException:
        driver.find_element(By.NAME, 'searchTerm').send_keys("209984_000")
        log.info("Job Searched Successfully")
        time.sleep(5)

        chevron1 = driver.find_element(By.XPATH, "//i[@class='fas fa-chevron-right']")
        driver.execute_script("arguments[0].click();", chevron1)
        log.info("Clicked on chevron1 ::- Details of the job searched is displayed")
        time.sleep(3)
