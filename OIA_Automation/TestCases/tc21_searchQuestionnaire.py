import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def searchQn(driver):
    question = driver.find_element(By.XPATH, '//a[text()=" Fragebögen "]')
    driver.execute_script("arguments[0].click();", question)
    print("Clicked on Questionnaire")
    driver.implicitly_wait(10)

    sel_rubrik = driver.find_element(By.ID, 'rubrik')
    choose = Select(sel_rubrik)
    selected = choose.select_by_visible_text('Conditional Questions ')
    print('Selected rubrik')
    time.sleep(1)

    sel_clu = driver.find_element(By.ID, 'cluster')
    choose = Select(sel_clu)
    selected = choose.select_by_index(1)
    print('Selected cluster')
    time.sleep(1)

    sel_assetClass = driver.find_element(By.ID, 'assetClass')
    choose = Select(sel_assetClass)
    selected = choose.select_by_value('residential')
    print('Selected Asset class')
    time.sleep(1)

    search_que = driver.find_element(By.NAME, 'searchTerm')
    search_que.send_keys('dfdfdftest')
    time.sleep(1)

    search_bar = driver.find_element(By.XPATH, '//i[@class="fa fa-search"]')
    search_bar.click()
    time.sleep(4)

    search_items = len(driver.find_elements(By.XPATH, '//td[@class="col-md-1 text-center pl-0 cursor"]'))
    if search_items > 0:
        print('No. of items found: '+str(search_items))
    else:
        print('No items found')

    driver.get_screenshot_as_file('C:\\Users\\abhmishr\\PycharmProjects\\Selenium-Python\\ImmoAgent\\TestCases\\TestScreenshots\\TC021_' + str(random.randint(0, 999)) + '.png')


def main():
    driver = launchBrowser()
    login(driver)
    searchQn(driver)
    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    main()
