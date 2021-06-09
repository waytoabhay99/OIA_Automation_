import random
import time
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login, logout


def custOrder(driver):
    cust = driver.find_element(By.CSS_SELECTOR, '[href="/customers"]')
    driver.execute_script("arguments[0].click();", cust)
    print("Clicked on Kunden")

    firstCust = driver.find_element(By.XPATH, '(//i[@class="fas fa-chevron-right"])[1]')
    firstCust.click()
    print('Open 1st customer details')
    time.sleep(3)

    history = driver.find_element(By.XPATH, '//section[@class="text-center text-uppercase deselected-tab mr-4 px-3 '
                                            'py-2 cursor"]')
    history.click()
    print('Clicked on history')
    time.sleep(2)
    custName = driver.find_element(By.XPATH, '//div[@class="heading"]')


    noDataFound = len(driver.find_elements(By.XPATH, '//td[@id="uid"]'))
    print(noDataFound)
    if noDataFound == 0:
        print('No order found for - ' + custName.text)
    else:
        print('Order history displayed for - ' + custName.text)
        orderCount = driver.find_elements(By.XPATH, '//td[@id="uid"]')
        for x in range(len(orderCount)):
            print(orderCount[x].text)
        print('Total number of orders found: ' + str(len(orderCount)))
    # dt = datetime.datetime.now()
    # print(dt)
    driver.get_screenshot_as_file('C:\\Users\\abhmishr\\PycharmProjects\\Selenium-Python\\ImmoAgent\\TestCases'
                                  '\\TestScreenshots\\TC026_' + str(random.randint(0, 999)) + '.png')



def main():
    driver = launchBrowser()
    login(driver)
    custOrder(driver)
    time.sleep(5)
    logout(driver)


if __name__ == '__main__':
    main()
