import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def display_agenten_rechnungen(driver):
    driver.implicitly_wait(10)
    bills = driver.find_element(By.XPATH, "//a[text()=' Rechnungen ']")
    driver.execute_script("arguments[0].click();", bills)
    print("Clicked on bills")
    time.sleep(10)

    # #Click on filter icons of bills:

    offen = driver.find_element(By.XPATH, '//button[text()="Offen"]')
    driver.execute_script("arguments[0].click();", offen)
    time.sleep(5)

    try:
        no_datafound = driver.find_element(By.XPATH,
                                           "//article[text()='Keine Daten gefunden' and @class='text-center']")
        print("No bills available::", no_datafound.text)

    except NoSuchElementException:
        first = driver.find_elements(By.XPATH, "//label[text()='Rechnungsnumber']//following-sibling::article")
        print("list of bills in Status - OFFEN")
        for x in range(len(first)):
            print("Bill Number:: " + first[x].text)

    time.sleep(10)

    fehlt = driver.find_element(By.XPATH, '//button[text()="Fehlt"]')
    driver.execute_script("arguments[0].click();", fehlt)
    time.sleep(5)

    try:
        no_datafound = driver.find_element(By.XPATH,
                                           "//article[text()='Keine Daten gefunden' and @class='text-center']")
        print("No bills available in status Fehlt:: " + no_datafound.text)

    except NoSuchElementException:
        second = driver.find_elements(By.XPATH, "//label[text()='Rechnungsnumber']//following-sibling::article")
        print("list of bills in Status - Fehlt ")
        for x in range(len(second)):
            print("Bill Number:: " + second[x].text)
    time.sleep(10)

    Freigegeben = driver.find_element(By.XPATH, '//button[text()="Freigegeben"]')
    driver.execute_script("arguments[0].click();", Freigegeben)
    time.sleep(5)

    try:
        no_datafound = driver.find_element(By.XPATH,
                                           "//article[text()='Keine Daten gefunden' and @class='text-center']")
        print("No bills available in status Freigegeben::", no_datafound.text)

    except NoSuchElementException:
        third = driver.find_elements(By.XPATH, "//label[text()='Rechnungsnumber']//following-sibling::article")
        print("list of bills in Status - Freigegeben ")
        for x in range(len(third)):
            print("Bill Number:: " + third[x].text)
    time.sleep(10)

    Bezahlt = driver.find_element(By.XPATH, '//button[text()="Bezahlt"]')
    driver.execute_script("arguments[0].click();", Bezahlt)
    time.sleep(15)

    try:
        no_datafound = driver.find_element(By.XPATH,
                                           "//article[text()='Keine Daten gefunden' and @class='text-center']")
        print("No bills available in status Bezahlt::", no_datafound.text)

    except NoSuchElementException:
        fourth = driver.find_elements(By.XPATH, "//label[text()='Rechnungsnumber']//following-sibling::article")
        print("list of bills in Status - Bezahlt ")
        for x in range(len(fourth)):
            print("Bill Number:: " + fourth[x].text)


def main():
    driver = launchBrowser()
    login(driver)
    display_agenten_rechnungen(driver)


if __name__ == '__main__':
    main()
