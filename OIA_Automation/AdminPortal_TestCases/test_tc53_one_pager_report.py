import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ImmoAgent.Resuables.test_logging import get_logger


def test_download_std_reports(login):
    log = get_logger()
    driver = login

    job_no = 210404
    searchbox = driver.find_element(By.XPATH, '//input[@name="searchTerm" and @placeholder="Aufträge durchsuchen"]')
    searchbox.send_keys(job_no)
    log.info('Entered Job Number ' + str(job_no) + ' in the Search box')
    driver.implicitly_wait(15)

    job_chev = driver.find_element(By.XPATH, '//a[@role="button"]//i[@class="fas fa-chevron-right"]')
    driver.execute_script("arguments[0].click();", job_chev)
    log.info('Clicked on the Job Chevron')
    driver.implicitly_wait(15)

    if driver.find_element(By.CSS_SELECTOR, 'i[class="zumReport fas fa-file-alt cursor"]').is_displayed():
        driver.find_element(By.CSS_SELECTOR, 'i[class="zumReport fas fa-file-alt cursor"]').click()

        time.sleep(8)

        allresults = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button['
                                                                                               '@type="submit" and '
                                                                                               '@class="btn '
                                                                                               'primary-button '
                                                                                               'mr-2"]')))
        driver.execute_script("arguments[0].click();", allresults)
        log.info('Clicked on All Results')
        time.sleep(8)
        allreports = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//button['
                                                                                               '@type="submit" and '
                                                                                               '@class="btn '
                                                                                               'primary-button"])['
                                                                                               '2]')))
        driver.execute_script("arguments[0].click();", allreports)
        log.info('Clicked on All Reports')
        time.sleep(8)

    else:
        log.info("No Reports Available")
