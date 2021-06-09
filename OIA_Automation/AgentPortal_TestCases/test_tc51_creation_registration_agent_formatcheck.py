import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

from ImmoAgent.AgentPortal_TestCases.test_logging import get_logger

option = Options()
option.add_argument("--disable-notifications")
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)

driver.get("https://oiaagentqa.z6.web.core.windows.net/login")
driver.maximize_window()


def test_creation_agent_Formatcheck():
    log = get_logger()

    # To click on register
    driver.implicitly_wait(10)
    Register = driver.find_element(By.XPATH, '//button[@class="btn secondary-button mr-3 text-uppercase"]')
    driver.execute_script("arguments[0].click();", Register)
    log.info("Clicked on Registration Link")

    driver.find_element(By.XPATH, '//input[@placeholder ="max.mustermann@mail.com"]').send_keys(
        "revasharma0692+13gmail.com")
    driver.find_element(By.XPATH, '//input[@formcontrolname="password"]').send_keys("Test@1234")
    driver.find_element(By.XPATH, '//input[@formcontrolname="confirmPassword"]').send_keys("Test@1234")

    driver.find_element(By.XPATH, '//button[@class="btn primary-button"]').click()
    log.info("Clicked on register")
    time.sleep(5)

    try:
        email_error = driver.find_element(By.XPATH, "//div[text()='Bitte gib ein gültiges E-Mail-Format ein.']")
        log.info("email is invalid:" + email_error.text)

    except NoSuchElementException:
        log.info("Format of the Email address provided is correct")

    gen = driver.find_element(By.ID, 'gender')
    drp = Select(gen)

    drp.select_by_value('female')
    log.info("Selected Gender")

    driver.find_element(By.ID, 'firstName').send_keys("Check1")
    log.info("Entered first name")
    driver.find_element(By.ID, 'lastName').send_keys("Check2")
    log.info("Entered second name")

    try:
        driver.find_element(By.XPATH, "//input[@placeholder = 'Sachsendamm']").send_keys("13347 Berlin")
        time.sleep(2)
        listElements = driver.find_elements(By.CSS_SELECTOR, ".pac-container div span.pac-icon")
        listElements[2].click()

    except ElementNotInteractableException:
        log.info("Address not found :: Please try again")

    driver.find_element(By.XPATH, '//input[@formcontrolname="additionalAddress"]').send_keys("TestAddress")
    log.info("Added additional address")
    driver.find_element(By.ID, 'mobilePhone').send_keys("000+491603338231")
    log.info("Added mobile number")
    driver.find_element(By.ID, 'phone').send_keys("+4972212700")
    log.info("Added phone number")
    driver.find_element(By.ID, 'jobStatus').send_keys("Test1")
    log.info("Added job status")
    element = driver.find_element(By.ID, 'experienced')
    driver.execute_script("arguments[0].click();", element)

    status = driver.find_element(By.ID, 'experienced').is_selected()
    log.info(status)

    r_dropdown = driver.find_element(By.ID, 'radius')
    radius = Select(r_dropdown)

    radius.select_by_visible_text('10 km ')
    log.info("Radius selected")
    driver.find_element(By.XPATH, '//button[@class="btn primary-button"]').click()
    time.sleep(5)

    try:
        mobile_error = driver.find_element(By.XPATH, '//div[text()="Bitte gib eine gültige Telefonnummer ein."]')
        log.info("Mobile number is invalid:" + mobile_error.text)

    except NoSuchElementException:
        log.info("Format of the given mobile number is correct")

    try:
        phone_error = driver.find_element(By.XPATH, '//div[text()="Bitte gib eine gültige Telefonnummer ein."]')
        log.info("Mobile number is invalid:" + phone_error.text)

    except NoSuchElementException:
        log.info("Format of the given phone number is correct")
