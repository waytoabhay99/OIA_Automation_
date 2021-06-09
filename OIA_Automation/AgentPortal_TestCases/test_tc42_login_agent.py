import time
from selenium.webdriver.common.by import By
from ImmoAgent.AgentPortal_TestCases.test_logging import get_logger


def test_user_login(login):
    log = get_logger()
    driver = login
    time.sleep(5)
    welcome = driver.find_elements(By.XPATH, "//div[@class='header-inner']")

    if len(welcome) > 0:
        log.info("User successfully logged In")

    else:
        log.info("Something went wrong -- User unable to login")
