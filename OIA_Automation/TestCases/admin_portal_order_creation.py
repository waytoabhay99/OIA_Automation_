import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def create_order(driver):
    time.sleep(3)
    # new_order = driver.find_element((By.XPATH, '//button[@class="btn primary-button"]')))
    # driver.execute_script("arguments[0].click();", new_order)
    new_order = driver.find_element(By.CSS_SELECTOR, 'i[class="fa fa-plus"]')
    driver.execute_script("arguments[0].click();", new_order)
    print("Clicked on New order")

    time.sleep(5)
    driver.find_element(By.XPATH, '//input[@placeholder="Immobilienbesichtigungs GmbH"]').send_keys('Sopra')
    listElements = driver.find_element(By.XPATH, '//span[text()="Rv RS"]')
    driver.execute_script("arguments[0].click();", listElements)
    print("Selected customer")

    driver.find_element_by_xpath('//*[@id="orderName"]').send_keys("test")

    driver.find_element(By.XPATH, '(//i[@class="far fa-calendar-alt"])[1]').click()
    c1 = driver.find_element(By.XPATH, '//div[@aria-label="Tuesday, March 30, 2021"]')
    driver.execute_script("arguments[0].click();", c1)
    print("selected 1st date")
    time.sleep(5)

    c2 = driver.find_element(By.XPATH, '//div[@aria-label="Friday, April 16, 2021"]')
    driver.execute_script("arguments[0].click();", c2)
    print("selected 2nd date")
    time.sleep(5)

    driver.find_element(By.XPATH, '(//i[@class="far fa-calendar-alt"])[3]').click()
    c3 = driver.find_element(By.XPATH, '(//div[@aria-label="Thursday, March 25, 2021"])[1]')
    driver.execute_script("arguments[0].click();", c3)
    print("selected 3rd date")
    time.sleep(5)

    driver.find_element(By.XPATH, '(//i[@class="far fa-calendar-alt"])[4]').click()
    c4 = driver.find_element(By.XPATH, '//div[@aria-label="Wednesday, March 31, 2021"]')
    driver.execute_script("arguments[0].click();", c4)
    print("selected 4th date")

    continue1 = driver.find_element(By.XPATH, '//button[text()="Weiter"]')
    driver.execute_script("arguments[0].click();", continue1)
    print("Details of form1 for order creation are Saved")

    time.sleep(3)
    manual_upload = driver.find_element(By.XPATH, '//input[@value="manual-upload"]')
    driver.execute_script("arguments[0].click();", manual_upload)
    print("Clicked on manual entry")

    driver.find_element(By.XPATH, '//input[@placeholder="FORTL_NR"]').send_keys("A001")

    driver.find_element(By.XPATH, "//input[@placeholder = 'Sachsendamm']").send_keys("Fra")
    driver.find_element(By.XPATH, "//input[@placeholder='Input Text']").send_keys("add1")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder = 'Sachsendamm']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder = 'Sachsendamm']").send_keys("nk")
    driver.find_element(By.XPATH, "//input[@placeholder = 'Sachsendamm']").send_keys(Keys.ARROW_DOWN, Keys.RETURN)
    time.sleep(2)

    driver.find_element(By.XPATH, '//section//table//tr//td//select').click()
    asset_dropdown = driver.find_element(By.XPATH, '//section//table//tr//td//select')
    asset = Select(asset_dropdown)
    asset.select_by_visible_text('Office ')
    print("Asset selected")

    driver.find_element(By.XPATH, "//input[@placeholder = 'Max Mustermann']").send_keys("John")
    driver.find_element(By.XPATH, "//input[@placeholder ='+49891234567']").send_keys("+919729613751")
    driver.find_element(By.XPATH, "//input[@placeholder = 'Comment']").send_keys("Space required for office")
    driver.find_element(By.XPATH, "//button[text()='Weiter']").click()

    check1 = driver.find_element(By.XPATH, "//input[@type='checkbox'and @name='trades']")
    driver.execute_script("arguments[0].click();", check1)

    Innen = driver.find_element(By.XPATH, "(//div[@class='deselected-state'])[1]")
    driver.execute_script("arguments[0].click();", Innen)
    print("Innen service selected")

    save = driver.find_element(By.XPATH, "//button[text()='Speichern']")
    driver.execute_script("arguments[0].click();", save)
    print('Clicked on save')

    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "(//i[@class='fas fa-chevron-right'])[1]")))
    driver.execute_script("arguments[0].click();", element)
    print("First Chevron selected")

    time.sleep(5)
    edit = driver.find_element(By.XPATH, "//button[text()='Bearbeiten']")
    driver.execute_script("arguments[0].click();", edit)

# screen to click and find agent for your created job
    click_findagent = driver.find_element(By.XPATH,
                                          "//button[@class='btn toggle-button' and text()=' neuen Agenten finden ']")
    driver.execute_script("arguments[0].click();", click_findagent)
    print("list of agents displayed")
    time.sleep(10)

# Search the agent in the search box
    driver.find_element(By.XPATH, "//input[@placeholder='Agenten suchen' and @name='searchTerm']").send_keys("Rev")
    time.sleep(5)
    select_agent = driver.find_element(By.XPATH, "(//input[@name='aId'])[1]")
    driver.execute_script("arguments[0].click();", select_agent)

    time.sleep(5)
    driver.find_element(By.XPATH, "//button[text()='Zuweisen']").click()

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "(//article[@class='col-lg-3']//article)[1]")))
    ordernummer = driver.find_element(By.XPATH, '(//article[@class="col-lg-3"]//article)[1]')
    print("Order created: "+ordernummer.text)


def main():
    driver = launchBrowser()
    login(driver)
    create_order(driver)


if __name__ == '__main__':
    main()
