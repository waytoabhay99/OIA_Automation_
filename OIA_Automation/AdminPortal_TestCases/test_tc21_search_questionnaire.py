import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from ImmoAgent.Resuables.test_logging import get_logger


def test_search_questionnaire(login):
    log = get_logger()
    driver = login
    question = driver.find_element(By.XPATH, '//a[text()=" Fragebögen "]')
    driver.execute_script("arguments[0].click();", question)
    log.info("Clicked on Questionnaire")
    driver.implicitly_wait(10)

    sel_rubrik = driver.find_element(By.ID, 'rubrik')
    choose = Select(sel_rubrik)
    choose.select_by_value('fcaf23b5-86e1-469a-bfad-53c9117fb101')
    log.info('Selected rubrik')
    time.sleep(2)

    sel_clu = driver.find_element(By.ID, 'cluster')
    choose = Select(sel_clu)
    choose.select_by_index(1)
    log.info('Selected cluster')
    time.sleep(2)

    sel_assetClass = driver.find_element(By.ID, 'assetClass')
    choose = Select(sel_assetClass)
    choose.select_by_value('residential')
    log.info('Selected Asset class')
    time.sleep(2)

    search_que = driver.find_element(By.XPATH, '(//div[@class="input-group"]//input[@name="searchTerm"])[2]')
    search_que.click()
    search_que.send_keys('test')
    time.sleep(1)

    search_bar = driver.find_element(By.XPATH, '(//i[@class="fa fa-search"])[2]')
    search_bar.click()
    time.sleep(4)

    search_items = len(driver.find_elements(By.XPATH, '//td[@class="col-md-1 text-center pl-0 cursor"]'))
    if search_items > 0:
        log.info('No. of items found: ' + str(search_items))
    else:
        log.info('No items found')
