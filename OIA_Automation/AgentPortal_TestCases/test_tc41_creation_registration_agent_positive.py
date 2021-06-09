import time
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
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


def test_creation_agent():
    log = get_logger()

    # To click on register
    driver.implicitly_wait(10)
    register = driver.find_element(By.XPATH, '//button[@class="btn secondary-button mr-3 text-uppercase"]')
    driver.execute_script("arguments[0].click();", register)
    log.info("Clicked on Register 1")

    driver.find_element(By.XPATH, '//input[@placeholder ="max.mustermann@mail.com"]').send_keys(
        "revasharma0692+15@gmail.com")
    log.info("Entered email id")
    driver.find_element(By.XPATH, '//input[@formcontrolname="password"]').send_keys("Test@1234")
    log.info("Entered password in password field")
    driver.find_element(By.XPATH, '//input[@formcontrolname="confirmPassword"]').send_keys("Test@1234")
    log.info("Entered password in password again in confirm password field")
    driver.find_element(By.XPATH, '//button[@class="btn primary-button"]').click()
    log.info("Clicked on register")
    time.sleep(5)

    # #Registeration form
    # #Select gender
    gen = driver.find_element(By.ID, 'gender')
    drp = Select(gen)

    drp.select_by_value('female')
    log.info("Selected Gender")
    # #drp.select_by_value('male') working properly

    driver.find_element(By.ID, 'firstName').send_keys("Check1")
    log.info("Entered first name")
    driver.find_element(By.ID, 'lastName').send_keys("Check2")
    log.info("Entered second name")

    # #address selection
    try:
        driver.find_element(By.XPATH, "//input[@placeholder = 'Sachsendamm']").send_keys("458 ")
        time.sleep(2)
        listElements = driver.find_elements(By.CSS_SELECTOR, ".pac-container div span.pac-icon")
        listElements[2].click()

    except ElementNotInteractableException:
        log.info("Address not found :: Please try again")

    driver.find_element(By.XPATH, '//input[@formcontrolname="additionalAddress"]').send_keys("TestAddress")
    log.info("Added additional address")
    driver.find_element(By.ID, 'mobilePhone').send_keys("+491603338231")
    log.info("Added mobile number")
    driver.find_element(By.ID, 'phone').send_keys("+4972212700")
    log.info("Added phone number")
    driver.find_element(By.ID, 'jobStatus').send_keys("Test1")
    log.info("Added job status")
    element = driver.find_element(By.ID, 'experienced')
    driver.execute_script("arguments[0].click();", element)

    status = driver.find_element(By.ID, 'experienced').is_selected()
    log.info(status)

    radius_dropdown = driver.find_element(By.XPATH, '//select[@id="radius" and @formcontrolname="radius"]')
    radius = Select(radius_dropdown)

    radius.select_by_value('2: 15')
    log.info("Radius selected")

    driver.find_element(By.XPATH, '//button[@class="btn primary-button"]').click()
    log.info("Clicked on submit -- to save all the details provided by the user")

    if driver.find_element(By.XPATH,
                           '//div[@role="alertdialog" and @class="ng-tns-c14-0 toast-message ng-star-inserted"]').is_displayed():
        log.info(driver.find_element(By.XPATH,
                                     '//div[@role="alertdialog" and @class="ng-tns-c14-0 toast-message '
                                     'ng-star-inserted"]').text)

    elif driver.find_element(By.XPATH,
                             '//div[@id="toast-container" and @class="toast-top-right toast-container"]').is_displayed():
        log.info(driver.find_element(By.XPATH,
                                     '//div[@id="toast-container" and @class="toast-top-right toast-container"]').text)

    else:
        log.info("TRY AGAIN")
    driver.close()
