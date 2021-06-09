import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from ImmoAgent.Resuables.test_logging import get_logger


def test_create_new_order(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(10)
    new_order = driver.find_element(By.CSS_SELECTOR, 'i[class="fa fa-plus"]')
    driver.execute_script("arguments[0].click();", new_order)
    log.info("Clicked on New order")

    time.sleep(10)
    driver.find_element(By.XPATH, '//input[@placeholder="Immobilienbesichtigungs GmbH"]').send_keys('Sopra')
    listElements = driver.find_element(By.XPATH, '//span[text()="Rv RS"]')
    driver.execute_script("arguments[0].click();", listElements)
    log.info("Selected customer")

    driver.find_element_by_xpath('//*[@id="orderName"]').send_keys("test")

    driver.find_element(By.XPATH, '(//i[@class="far fa-calendar-alt"])[1]').click()
    c1 = driver.find_element(By.XPATH, '//div[@aria-label="Friday, June 25, 2021"]')
    driver.execute_script("arguments[0].click();", c1)
    log.info("selected 1st date")
    time.sleep(5)

    c2 = driver.find_element(By.XPATH, '//div[@aria-label="Wednesday, June 30, 2021"]')
    driver.execute_script("arguments[0].click();", c2)
    log.info("selected 2nddate")
    time.sleep(5)

    driver.find_element(By.XPATH, '(//i[@class="far fa-calendar-alt"])[3]').click()
    c3 = driver.find_element(By.XPATH, '(//div[@aria-label="Monday, May 31, 2021"])[1]')
    driver.execute_script("arguments[0].click();", c3)
    log.info("selected 3rd date")
    time.sleep(5)

    driver.find_element(By.XPATH, '(//i[@class="far fa-calendar-alt"])[4]').click()
    c4 = driver.find_element(By.XPATH, '//div[@aria-label="Monday, May 31, 2021"]')
    driver.execute_script("arguments[0].click();", c4)
    log.info("selected 4th date")

    continue1 = driver.find_element(By.XPATH, '//button[text()="Weiter"]')
    driver.execute_script("arguments[0].click();", continue1)
    log.info("Details of form1 for order creation are Saved")

    time.sleep(3)
    manual_upload = driver.find_element(By.XPATH, '//input[@value="manual-upload"]')
    driver.execute_script("arguments[0].click();", manual_upload)
    log.info("Clicked on manual entry")

    driver.find_element(By.XPATH, '//input[@placeholder="FORTL_NR"]').send_keys("A001")
    log.info('Asset id entered')

    driver.find_element(By.XPATH, "//input[@placeholder = 'Sachsendamm']").send_keys("Fra")
    driver.find_element(By.XPATH, "//input[@placeholder='Input Text']").send_keys("add1")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder = 'Sachsendamm']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder = 'Sachsendamm']").send_keys("nk 13")
    driver.find_element(By.XPATH, "//input[@placeholder = 'Sachsendamm']").send_keys(Keys.ARROW_DOWN, Keys.RETURN)
    time.sleep(2)
    log.info('Entered Address 1')

    driver.find_element(By.XPATH, '//section//table//tr//td//select').click()
    asset_dropdown = driver.find_element(By.XPATH, '//section//table//tr//td//select')
    asset = Select(asset_dropdown)
    asset.select_by_value('office')
    log.info("Asset selected")

    driver.find_element(By.XPATH, "//input[@placeholder = 'Max Mustermann']").send_keys("John")
    log.info('Contact person name entered')

    driver.find_element(By.XPATH, "//input[@placeholder ='+49891234567']").send_keys("+919729613751")
    log.info('Phone number entered')

    driver.find_element(By.XPATH, "//input[@placeholder = 'Comment']").send_keys("Space required for office")
    log.info('Comment entered')

    driver.find_element(By.XPATH, "//button[text()='Weiter']").click()
    log.info('Clicked on continue')

    check1 = driver.find_element(By.XPATH, "//input[@type='checkbox'and @name='trades']")
    driver.execute_script("arguments[0].click();", check1)

    Innen = driver.find_element(By.XPATH, "(//div[@class='deselected-state'])[1]")
    driver.execute_script("arguments[0].click();", Innen)
    log.info("Innen service selected")

    save = driver.find_element(By.XPATH, "//button[text()='Speichern']")
    driver.execute_script("arguments[0].click();", save)
    log.info('Clicked on save')

    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "(//i[@class='fas fa-chevron-right'])[1]")))
    driver.execute_script("arguments[0].click();", element)
    log.info("First Chevron selected")

    time.sleep(5)
    edit = driver.find_element(By.XPATH, "//button[text()='Bearbeiten']")
    driver.execute_script("arguments[0].click();", edit)

    # screen to click and find agent for your created job
    click_findagent = driver.find_element(By.XPATH,
                                          "//button[@class='btn toggle-button' and text()=' neuen Agenten finden ']")
    driver.execute_script("arguments[0].click();", click_findagent)
    log.info("list of agents displayed")
    time.sleep(5)

    # Search the agent in the search box
    driver.find_element(By.XPATH, "//input[@placeholder='Agenten suchen' and @name='searchTerm']").send_keys("Test")
    time.sleep(5)
    select_agent = driver.find_element(By.XPATH, "(//input[@name='aId'])[1]")
    driver.execute_script("arguments[0].click();", select_agent)
    log.info('Agent selected')

    time.sleep(5)
    driver.find_element(By.XPATH, "//button[text()='Zuweisen']").click()
    log.info('Clicked on submit')
    time.sleep(8)

    ordernumber = driver.find_element(By.XPATH, "//label[text()='Auftragsnummer']/following-sibling::article")
    log.info(ordernumber.text)
    log.info("Order created: "+ ordernumber.text)
