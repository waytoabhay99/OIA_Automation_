import random
import time
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from ImmoAgent.ClientPortal_TestCases.test_logging_client import get_logger


def test_customer_registration(launch_browser):
    log = get_logger()
    driver = launch_browser
    driver.get("https://oiaclientqa.z6.web.core.windows.net/login")
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    Register = driver.find_element(By.XPATH, '(//button[@type="submit"])[2]')
    driver.execute_script("arguments[0].click();", Register)
    log.info("Clicked on Register")
    time.sleep(5)

    driver.find_element(By.XPATH, '//input[@placeholder="Z.B. max@mustermann.de"]').send_keys(
        "revasharma0692+" + str(random.randint(2, 999)) + "@gmail.com")

    driver.find_element(By.XPATH, '//input[@formcontrolname="password"]').send_keys("Test@1234")
    driver.find_element(By.XPATH, '//input[@formcontrolname="confirmPassword"]').send_keys("Test@1234")
    time.sleep(5)
    submit1 = driver.find_element(By.XPATH, '//button[text()="Weiter"]')
    driver.execute_script("arguments[0].click();", submit1)
    time.sleep(2)
    try:
        email_error1 = driver.find_element(By.XPATH, "//div[text()='Die E-Mail-Adresse existiert bereits.']")
        log.info("Email Id already exists:" + email_error1.text)

    except NoSuchElementException:
        log.info("Unique email Id entered")

    try:
        email_error2 = driver.find_element(By.XPATH, "//div[text()='Bitte geben Sie ein gÃ¼ltiges E-Mail-Format ein.']")
        log.info("Format of the email id provided is incorrect:" + email_error2.text)

    except NoSuchElementException:
        log.info("Format of the emailId provided is correct")

    gen = driver.find_element(By.ID, 'salutation')
    drp = Select(gen)

    drp.select_by_value('female')
    log.info("Selected Gender")
    # drp.select_by_value('male')

    driver.find_element(By.ID, 'phone').send_keys("+4972212700")
    log.info("Added phone number")

    driver.find_element(By.ID, 'firstName').send_keys("Check11")
    log.info("Entered first name")

    driver.find_element(By.ID, "lastName").send_keys("Check2")
    log.info("Entered second name")

    time.sleep(2)
    # address selection
    driver.find_element(By.XPATH, "//input[@placeholder = 'Sachsendamm']").send_keys("133")
    time.sleep(2)

    driver.find_element(By.XPATH, '//input[@formcontrolname="additionalAddress"]').send_keys("Address 2")
    log.info("Added additional address")

    try:
        driver.find_element(By.XPATH, "//input[@placeholder = 'Sachsendamm']").click()
        driver.find_element(By.XPATH, "//input[@placeholder = 'Sachsendamm']").send_keys("4")
        driver.find_element(By.XPATH, "//input[@placeholder = 'Sachsendamm']").send_keys(Keys.ARROW_DOWN, Keys.RETURN)
        log.info('Location entered')
        time.sleep(2)

    except ElementNotInteractableException:
        log.info("Address not found :: Please try again")

    time.sleep(3)
    submit2 = driver.find_element(By.XPATH, '//button[text()=" Weiter "]')
    driver.execute_script("arguments[0].click();", submit2)
    log.info("Clicked on Weiter::Details of form2 submitted ")

    driver.find_element(By.ID, 'companyName').send_keys("Sopra1")
    log.info("Company name added")

    driver.find_element(By.ID, 'invoiceEmail').send_keys("revasharma+100@gmail.com")
    log.info("Email for invoices added")

    driver.find_element(By.ID, 'vatin').send_keys("1111")
    log.info("USt-Id-Nr added")

    time.sleep(2)
    submit3 = driver.find_element(By.XPATH, '//button[text()=" Weiter "]')
    driver.execute_script("arguments[0].click();", submit3)
    log.info("Clicked on Weiter::Details of form 3 submitted ")

# radio button to select second option
    radiobutton2 = driver.find_element(By.ID, 'rd_2')
    driver.execute_script("arguments[0].click();", radiobutton2)
    log.info("Selected second radio button : eigene Rechnungsadresse")

    driver.find_element(By.ID, 'billingvatin').send_keys("1234")
    log.info("Entered VAT identification number")

    driver.find_element(By.ID, 'billingInvoiceEmail').send_keys("revasharama0692+100@gmail.com")
    log.info("Entered billing invoice email")

    submit4 = driver.find_element(By.XPATH, '//button[text()=" Weiter "]')
    driver.execute_script("arguments[0].click();", submit4)
    log.info("Clicked on Weiter : Details of form 4 submitted ")

    time.sleep(5)

    if driver.find_element(By.XPATH, "//div[@class='overlay-container']").is_displayed():
        log.info(driver.find_element(By.XPATH, "//div[@class='overlay-container']").text)

    else:
        log.info("TRY AGAIN")
