import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def admin_job_sub(driver):
    driver.implicitly_wait(10)
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
    print("selected 1stdate")

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

    time.sleep(5)
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

    blue_icon = driver.find_element(By.XPATH, "//i[@class='far fa-file-alt blue']")
    driver.execute_script("arguments[0].click();", blue_icon)
    time.sleep(5)

    # ##deletion of all the questions
    select_all = driver.find_element(By.XPATH,
                                     "//input[@type='checkbox' and @class='form-check-input cursor ng-untouched "
                                     "ng-pristine ng-valid']")
    driver.execute_script("arguments[0].click();", select_all)
    delete_all = driver.find_element(By.CSS_SELECTOR, 'i[class="far fa-trash-alt mr-2"]')
    driver.execute_script("arguments[0].click();", delete_all)
    print("deleted all questions")
    time.sleep(8)

    # addition of questions

    Sonstiges1 = driver.find_element(By.XPATH,'(//div[@class="mb-2 form-check"]//input[@type="checkbox"])[3]')
    driver.execute_script("arguments[0].click();", Sonstiges1)
    print("Selected Sonstiges1")


def main():
    driver = launchBrowser()
    login(driver)
    admin_job_sub(driver)


if __name__ == '__main__':
    main()
