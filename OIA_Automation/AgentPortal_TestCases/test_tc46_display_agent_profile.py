import time
from selenium.webdriver.common.by import By
from ImmoAgent.AgentPortal_TestCases.test_logging import get_logger

def test_display_agent_profile(login):
    log = get_logger()
    driver = login
    time.sleep(5)

    profile = driver.find_element(By.XPATH, '//a[text()=" Profil "]')
    driver.execute_script("arguments[0].click();", profile)

    profile1= driver.find_elements(By.XPATH,"//div[@class='welcome-header float-left mt-n5 ml-4']")

    if len(profile1) > 0:
        log.info("Clicked on profile ::--Profile of the agent is displayed")

    else:
        log.info("Something went wrong : Please try again")

