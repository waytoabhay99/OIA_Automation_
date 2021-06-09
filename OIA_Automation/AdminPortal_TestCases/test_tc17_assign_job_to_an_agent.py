import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_assign_job_agent(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(5)

    Auftrage = driver.find_element(By.XPATH, "//a[text()=' Aufträge ']")
    driver.execute_script("arguments[0].click();", Auftrage)
    log.info("Clicked on Aufträge/orders")

    time.sleep(10)
    search = driver.find_element(By.XPATH,
                                 "//input[@name='searchTerm' and @placeholder='Aufträge durchsuchen']")
    search.send_keys("210201_0034")

    try:
        order_notfound = driver.find_element(By.XPATH,
                                             "(//article[text()='Keine Daten gefunden' and @class='no-data'])[3]")
        log.info("Invalid Order Number::" + order_notfound.text)

    except NoSuchElementException:
        log.info("Order is searched successfully")

    chevron1 = driver.find_element(By.XPATH, "(//i[@class='fas fa-chevron-right'])[1]")
    driver.execute_script("arguments[0].click();", chevron1)
    log.info("Clicked on chevron 1 --Navigated inside the order")

    time.sleep(10)

    chevron1_secondscreen = driver.find_element(By.XPATH,
                                                "(//button[@type='button' and @class='no-shadow']//i[@class='fas "
                                                "fa-chevron-right'])[1]")
    driver.execute_script("arguments[0].click();", chevron1_secondscreen)
    log.info("Clicked on chevron 2:: Selected first job in the order")
    time.sleep(7)

    edit = driver.find_element(By.XPATH, "//button[text()='Bearbeiten']")
    driver.execute_script("arguments[0].click();", edit)
    log.info('Clicked on edit job')
    time.sleep(7)

    # #screen to click and find agent for your created job
    click_findagent = driver.find_element(By.XPATH,
                                          "//button[@class='btn toggle-button' and text()=' neuen Agenten finden ']")
    driver.execute_script("arguments[0].click();", click_findagent)
    log.info("list of agents displayed")
    time.sleep(10)

    # #Search the agent in the search box
    driver.find_element(By.XPATH, "//input[@placeholder='Agenten suchen' and @name='searchTerm']").send_keys("K")
    log.info('Searching agent')
    time.sleep(5)

    select_agent = driver.find_element(By.XPATH, "(//input[@name='aId'])[1]")
    driver.execute_script("arguments[0].click();", select_agent)
    log.info("Selected required agent as per the input above")

    time.sleep(5)
    driver.find_element(By.XPATH, "//button[text()='Zuweisen']").click()
    log.info("Clicked on submit for assigning agent")
