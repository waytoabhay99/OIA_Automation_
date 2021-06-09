import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def launchBrowser():  # this function is to launch the Chrome browser
    option = Options()
    option.add_argument("--disable-notifications")
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
    driver.implicitly_wait(5)
    driver.get("https://oiaqa.z6.web.core.windows.net/")
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    print(driver.title)
    return driver


def login(driver):  # this function is login to Admin portal
    driver.find_element(By.XPATH, '//input[@type="email"]').send_keys("a@b.com")
    driver.find_element(By.XPATH, '//input[@type="password"]').send_keys('test')
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    print("Login Successful")
    driver.implicitly_wait(10)


def logout(driver):
    driver.find_element(By.ID, 'dropdownBasic1').click()
    driver.find_element(By.XPATH, '//span[@class="buttonLabel" and text()="Abmelden"]').click()
    driver.find_element(By.XPATH, '// button[text() = "Abmelden"]').click()
    logout_success = driver.find_element(By.XPATH, '//input[@type="email"]')
    print(logout_success.is_displayed())
    print("Logout Successful")


def openDraft(driver):
    draft = driver.find_element(By.XPATH, '//button[text()="Draft"]')
    driver.execute_script("arguments[0].click();", draft)
    # draft.click()
    print("Clicked on Draft")


def chev1Open(driver):
    chev = driver.find_element(By.CLASS_NAME, 'fas fa-chevron-right')
    driver.execute_script("arguments[0].click();", chev)
    print("Clicked on 1st Chevron")

    """
    this function question_create is to create question which covers upto 
    Notice to agents/Hinweis für Agenten section
    """


def question_create(driver):
    question = driver.find_element(By.XPATH, '//a[text()=" Fragebögen "]')
    driver.execute_script("arguments[0].click();", question)
    print("Clicked on Questionnaire")

    driver.implicitly_wait(10)

    newQues = driver.find_element(By.XPATH, '//button[text()=" Neue Frage "]')
    driver.execute_script("arguments[0].click();", newQues)
    print("Clicked on New Question")

    time.sleep(2)
    category = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'rubrik')))
    choose = Select(category)
    choose.select_by_value('7e0c84d3-264e-4232-b1ce-bf43f3035985')
    print('Selected text from 1st Dropdown')

    time.sleep(1)
    cluster = driver.find_element(By.ID, 'cluster')
    choose = Select(cluster)
    choose.select_by_value('a7b55bac-18d4-455e-9c7e-2a520b11b5e1')
    print('Selected text from 2nd Dropdown')

    multiselect = driver.find_element(By.XPATH, '//label[text()="Asset-Klasse"]//ancestor::div//span[text()="Input '
                                                'Text"]')
    driver.execute_script("arguments[0].click();", multiselect)

    residential = driver.find_element(By.XPATH, '//input[@aria-label="Residential"]')
    driver.execute_script("arguments[0].click();", residential)
    # residential.click()
    print('Selected Residential from dropdown')

    office = driver.find_element(By.XPATH, '//input[@aria-label="Office"]')
    driver.execute_script("arguments[0].click();", office)
    # office.click()
    print('Selected Office from dropdown')

    keyword = driver.find_element(By.ID, 'keywording')
    keyword.send_keys('Office space')
    print("Enter keyword")

    ques = driver.find_element(By.ID, 'question')
    ques.send_keys('Office space question for Automation test')
    print("Entered question")

    notice = driver.find_element(By.ID, 'notice')
    notice.send_keys('This is a test notice')
    print("Notice to agents")


def delete_all(driver, question_list):
    if len(question_list) > 0:
        selectAll = driver.find_element(By.ID, 'selectAll')
        driver.execute_script("arguments[0].click();", selectAll)
        print('Selected all for delete')
        deleteAll = driver.find_element(By.XPATH, '//button[@class="btn toggle-button deleteQuestionsButton"]')
        driver.execute_script("arguments[0].click();", deleteAll)
        print('Deleted the selected')
        print(len(question_list))
        question_list = driver.find_elements(By.CSS_SELECTOR, 'label[class="form-check-label rubric-heading"]')
        delete_all(driver, question_list)
        time.sleep(2)
    else:
        quesPlanningCheckbox = driver.find_element(By.XPATH, '//label[text()="Leerstand "]')
        quesPlanningCheckbox.click()
        print('Selected Leerstand')


def randomize():
    return random.randint(0, 12)


def main():
    driver = launchBrowser()
    openDraft(driver)
    chev1Open(driver)
    driver.quit()


if __name__ == '__main__':
    main()
