import time
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_login_admin_portal(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(10)

    time.sleep(5)
    header = driver.find_elements(By.CSS_SELECTOR, 'article[class="col-lg-9 heading"]')
    if len(header) > 0:
        log.info('Login Successful')
    else:
        log.info('Login fail')
