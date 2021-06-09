import time
from selenium.webdriver.common.by import By
from ImmoAgent.ClientPortal_TestCases.test_logging_client import get_logger


def test_client_login(login_client):
    log = get_logger()
    driver = login_client
    driver.implicitly_wait(15)
    header = driver.find_elements(By.CSS_SELECTOR, 'section[class="row header"]')
    if len(header) > 0:
        log.info('Login Successful')
    else:
        log.info('Login fail')
