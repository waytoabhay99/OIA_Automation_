import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from ImmoAgent.ClientPortal_TestCases.test_logging_client import get_logger


def test_client_new_order_creation(login_client):
    log = get_logger()
    driver = login_client
    driver.implicitly_wait(30)

    order_create = driver.find_element(By.CSS_SELECTOR, 'span[class="pl-1"]')
    driver.execute_script("arguments[0].click();", order_create)
    log.info('Clicked on Create order')
    driver.implicitly_wait(10)

    std_rpt = driver.find_element(By.XPATH, '(//button[@class="btn blue-button text-center"])[1]')
    driver.execute_script("arguments[0].click();", std_rpt)
    log.info('Clicked on standard report')
    driver.implicitly_wait(10)

    answer1 = driver.find_element(By.ID, '9fd7d114-321c-4cd4-a89b-4ac55c46c495')
    answer1.send_keys('Office Space')
    log.info('Entered answer 1')

    visitor = driver.find_element(By.ID, 'Gebäude außen inkl. Umgebunga62b5c7f-98fc-41f9-8034-0c74b7488498')
    driver.execute_script("arguments[0].click();", visitor)
    log.info('Visitors selected')

    area = driver.find_element(By.ID, 'Jae49c07c7-429e-48b6-9301-24024a92813c')
    driver.execute_script("arguments[0].click();", area)
    log.info('Area selected')

    rpt_format = driver.find_element(By.ID, 'Datensatz (Excel) plus Fotosc5b70970-dbb7-49f1-9fbd-a975ec6cfab5')
    driver.execute_script("arguments[0].click();", rpt_format)
    log.info('Report format selected')

    purpose = driver.find_element(By.ID, 'Wertüberprüfungen, Monitoring des Bestands, schneller Ersteindruck über ein '
                                         'großes Portfolio oder ähnlich323f2237-e5e6-4f73-a7e0-959c626643b7')
    driver.execute_script("arguments[0].click();", purpose)
    log.info('Purpose selected')

    stock = driver.find_element(By.ID, 'Jae4488d50-4cce-4a14-8d16-2e9be82a4dd2')
    driver.execute_script("arguments[0].click();", stock)
    log.info('Micro/Macro report')

    date = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Monday, May 31, 2021"]')
    driver.execute_script("arguments[0].click();", date)
    log.info('Date picked')

    answer10 = driver.find_element(By.ID, '1f03475f-23dd-49f0-95bd-b0cfc5ac8843')
    answer10.send_keys('Airport distance')
    log.info('Answer 10 entered')

    ind_obj = driver.find_element(By.ID, 'Nein2263fd55-2810-430f-9fc6-071f2e5432c7')
    driver.execute_script("arguments[0].click();", ind_obj)
    log.info('Individual objects option selected')

    contine = driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary float-right mt-2"]')
    driver.execute_script("arguments[0].click();", contine)
    log.info('Clicked on continue after filling the form')
    time.sleep(3)

    asset_upload = driver.find_element(By.XPATH, '//input[@name="asset-upload-condition" and @value="manual-upload"]')
    asset_upload.click()
    log.info('Manual upload radio button clicked')
    time.sleep(5)

    asset_id = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="A567"]')
    asset_id.send_keys('A0012')
    log.info('Asset id entered')

    asset_no = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="FORTL_NR"]')
    asset_no.send_keys('B0012')
    log.info('Asset no entered')

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Sachsendamm"]').send_keys("Hamburg")

    add2 = driver.find_element(By.XPATH, '//input[@type="text" and @placeholder="Input Text"]')
    add2.send_keys('Street')
    log.info('Address 2 entered')
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Sachsendamm"]').click()
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Sachsendamm"]').send_keys(" 18")
    driver.find_element(By.XPATH, "//input[@placeholder = 'Sachsendamm']").send_keys(Keys.ARROW_DOWN, Keys.RETURN)
    # listElements = driver.find_elements(By.CSS_SELECTOR, "div.pac-container div span.pac-icon")
    # listElements[2].click()
    log.info('Entered Address 1')
    time.sleep(2)

    driver.find_element(By.XPATH, '//section//table//tr//td//select').click()
    asset_dropdown = driver.find_element(By.XPATH, '//section//table//tr//td//select')
    asset = Select(asset_dropdown)
    asset.select_by_value('office')
    log.info("Asset selected")

    cont_per = driver.find_element(By.XPATH, "//input[@placeholder = 'Max Mustermann']")
    cont_per.send_keys("Ramamoorthy")
    log.info('Contact person name entered')

    mobile = driver.find_element(By.XPATH, "//input[@placeholder ='+49891234567']")
    mobile.send_keys("+919729613751")
    log.info('Phone number entered')

    comment = driver.find_element(By.XPATH, "//input[@placeholder = 'Comment']")
    comment.send_keys("Space required for office")
    log.info('Comment entered')

    driver.find_element(By.XPATH, '//button[@type="button" and @class="btn primary-button mt-2 mb-2"]').click()
    log.info('Clicked on submit')
    time.sleep(3)

    row_header = driver.find_elements(By.CSS_SELECTOR, 'div[class="col-md-8 dark-text"]')
    if len(row_header) > 0:
        log.info('Order created, please continue for review')
    else:
        log.info('Order creation failed, please try again')

    contin2 = driver.find_element(By.XPATH, '//button[@type="button" and @class="btn primary-button mt-2 mb-2"]')
    driver.execute_script("arguments[0].click();", contin2)
    log.info('Clicked on continue')
    time.sleep(4)

    confirm_header = driver.find_elements(By.CSS_SELECTOR, 'div[class="confirm-head"]')
    if len(confirm_header) > 0:
        log.info('Thank you. Order created successfully')
    else:
        log.info('Order creation was not successful, please try again')
