import time
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from ImmoAgent.Resuables.test_logging import get_logger


def test_job_submission(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(10)
    new_order = driver.find_element(By.CSS_SELECTOR, 'i[class="fa fa-plus"]')
    driver.execute_script("arguments[0].click();", new_order)
    log.info("Clicked on New order")

    time.sleep(5)
    driver.find_element(By.XPATH, '//input[@placeholder="Immobilienbesichtigungs GmbH"]').send_keys('Sopra')
    time.sleep(5)
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

    submit1 = driver.find_element(By.XPATH, '//button[text()="Weiter"]')
    driver.execute_script("arguments[0].click();", submit1)
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

    submit2=driver.find_element(By.XPATH, "//button[text()='Weiter']")
    driver.execute_script("arguments[0].click();", submit2)
    log.info("Details of form2 for order creation are Saved")

    # ##Job Submission section
    # #Screen 2
    # click on the blue icon for questions
    time.sleep(5)
    blue_icon = driver.find_element(By.XPATH, "//i[@class='far fa-file-alt blue']")
    driver.execute_script("arguments[0].click();", blue_icon)
    log.info("clicked on blue icon")
    time.sleep(10)

    # ##deletion of all the questions
    select_all = driver.find_element(By.XPATH,
                                     "//input[@type='checkbox' and @class='form-check-input cursor ng-untouched "
                                     "ng-pristine ng-valid']")
    driver.execute_script("arguments[0].click();", select_all)
    log.info("Clicked on clicked select all button")
    time.sleep(20)
    delete_all = driver.find_element(By.XPATH, "(//button[@type='button' and text()=' Aus dem Fragebögen löschen '])[1]")
    driver.execute_script("arguments[0].click();", delete_all)
    log.info("deleted all questions")

    time.sleep(25)

    # addition of questions

    # sonstiges1 = driver.find_element(By.XPATH, '(//div[@class="mb-2 form-check"]//input[@type="checkbox"])[3]')
    # driver.execute_script("arguments[0].click();", sonstiges1)
    # log.info("Selected Sonstiges1")


    Wettbewerb = driver.find_element(By.XPATH, '(//div[@class="mb-2 form-check"]//input[@type="checkbox"])[6]')
    driver.execute_script("arguments[0].click();", Wettbewerb)
    log.info("Selected Wettbewerb")

    time.sleep(15)
    submit3 = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Speichern']")
    driver.execute_script("arguments[0].click();", submit3)
    log.info("Details of form3 for order creation are Saved")

    time.sleep(10)
    check1 = driver.find_element(By.XPATH, "//input[@type='checkbox'and @name='trades']")
    driver.execute_script("arguments[0].click();", check1)
    log.info("Selected checkbox after deleting questions")
    time.sleep(10)

    # time.sleep(5)
    # InnenEinheit = driver.find_element(By.XPATH, "(//div[@class='deselected-state'])[1]")
    # driver.execute_script("arguments[0].click();",  InnenEinheit )
    # log.info(" Innen+Einheit service selected")

    save = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Speichern']")
    driver.execute_script("arguments[0].click();", save)
    log.info('Clicked on save')
    time.sleep(25)

    element = driver.find_element(By.XPATH, '//button[@type="button" and @class="no-shadow"]')
    driver.execute_script("arguments[0].click();", element)
    log.info("First Chevron selected for assigning the agent to the job created")

    time.sleep(5)
    edit = driver.find_element(By.XPATH, "//button[text()='Bearbeiten']")
    driver.execute_script("arguments[0].click();", edit)
    time.sleep(15)
    # screen to click and find agent for your created job
    driver.find_element(By.XPATH,"//button[@type='button' and text()=' neuen Agenten finden ']").click()
    # driver.execute_script("arguments[0].click();", click_findagent)
    log.info("list of agents displayed")
    time.sleep(10)

    # Search the agent in the search box
    driver.find_element(By.XPATH, "//input[@placeholder='Agenten suchen' and @name='searchTerm']").send_keys("Check1")
    time.sleep(5)
    select_agent = driver.find_element(By.XPATH, "(//input[@name='aId'])[1]")
    driver.execute_script("arguments[0].click();", select_agent)

    time.sleep(5)
    driver.find_element(By.XPATH, "//button[text()='Zuweisen']").click()

    time.sleep(5)
    ordernumber = driver.find_element(By.XPATH, "//label[text()='Auftragsnummer']/following-sibling::article")
    log.info(ordernumber.text)
    log.info("Order created: " + ordernumber.text)

    jobid = driver.find_elements(By.XPATH, "//tr[@class='content-data']//td[@scope='row']")

    for x in range(len(jobid)):
        log.info("Job Number:: " + (jobid[x].text))

    log.info("jobid[0]:" + jobid[0].text)
    search_job = jobid[0].text

    time.sleep(20)
    # option = Options()
    # option.add_argument("--disable-notifications")
    # option.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)

    driver.get("https://oiaagentqa.z6.web.core.windows.net/login")
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    log.info(driver.title)
    driver.find_element(By.XPATH, '//input[@placeholder ="max.mustermann@mail.com"]').send_keys(
        "revasharma0692+20@gmail.com")
    driver.find_element(By.XPATH, '//input[@formcontrolname="password"]').send_keys("Test@1234")
    driver.find_element(By.XPATH, '//button[@class="btn primary-button"]').click()

    # #Click on jobs
    driver.maximize_window()
    time.sleep(10)
    job = driver.find_element(By.XPATH, '//a[text()=" Jobs "]')
    driver.execute_script("arguments[0].click();", job)
    log.info("Clicked on Jobs")
    time.sleep(5)

    driver.find_element(By.NAME, 'searchTerm').send_keys(search_job)
    log.info("Job Searched Successfully")
    time.sleep(5)

    driver.find_element(By.XPATH, "//button[@type='button']//i[@class='fas fa-chevron-right']").click()
    log.info("Clicked on chevron :: Job displayed successfully")
    time.sleep(5)

    driver.find_element(By.XPATH,
                        "//button[@class='btn primary-button mx-auto pl-3 pr-3' and text()='Job annehmen']").click()
    log.info("Clicked on accept job")
    time.sleep(2)
    driver.find_element(By.XPATH,
                        "//button[@class='btn col-lg-12 primary-button' and text()='Ja, Job annehmen']").click()
    log.info("Clicked on yes,I accept job")

    if driver.find_element(By.XPATH,
                           '//div[@id="toast-container" and @class="toast-top-right toast-container"]').is_displayed():
        log.info(driver.find_element(By.XPATH,
                                     '//div[@id="toast-container" and @class="toast-top-right toast-container"]').text)
    else:
        log.info("Something went wrong")

    driver.find_element(By.XPATH,
                        "//button[@class='float-right btn primary-button col-lg-6 mt-4'and text()=' "
                        "Besichtigungsergebnisse prüfen ']").click()
    log.info("Clicked on Check inspection results")

    time.sleep(7)
    question1_chevron = driver.find_element(By.XPATH,
                                            "(//button[@type='button' and @class='no-shadow float-right mr-2'])[1]")
    driver.execute_script("arguments[0].click();", question1_chevron)
    log.info("Clicked on chevron1:: Question displayed successfully")

    time.sleep(5)

    first_option = driver.find_element(By.XPATH,"(//label[@for='inlineRadio'])[1]")
    driver.execute_script("arguments[0].click();",first_option)
    log.info("Selected Option Ja from the radio buttons avialable")

    submitanswer1 = driver.find_element(By.XPATH, "//button[@class='float-right cancel-button p-3 pr-4 pl-4']")
    driver.execute_script("arguments[0].click();", submitanswer1)
    log.info("Clicked on submit answer button for question 1 : Answer Submitted")
    time.sleep(2)

    second_option = driver.find_element(By.XPATH, " (// label[@ for ='inlineRadio'])[3]")
    driver.execute_script("arguments[0].click();", second_option)
    log.info("Selected Option Ja from the radio buttons avialable")

    submitanswer2 = driver.find_element(By.XPATH, "//button[@class='float-right cancel-button p-3 pr-4 pl-4']")
    driver.execute_script("arguments[0].click();", submitanswer2)
    log.info("Clicked on submit answer button for question 2 : Answer Submitted")

    option_first = driver.find_element(By.XPATH, "(//label[@for='inlineRadio'])[1]")
    driver.execute_script("arguments[0].click();", option_first)
    log.info("Selected Option Ja from the radio buttons avialable")

    submitanswer3 = driver.find_element(By.XPATH, "//button[@class='float-right cancel-button p-3 pr-4 pl-4']")
    driver.execute_script("arguments[0].click();", submitanswer3)
    log.info("Clicked on submit answer button for question 3 : Answer Submitted")
    time.sleep(2)




    driver.find_element(By.XPATH,
                        "//button[@class='float-right btn primary-button col-lg-6 mt-4' and text()=' Ergebnisse "
                        "übermitteln ']").click()
    log.info("Clicked on submit results")

    driver.find_element(By.XPATH, "//button[@class='float-right cancel-button p-3 pr-4 pl-4']").click()
    log.info("Clicked on Save/Speichern")

    time.sleep(5)
    driver.find_element(By.XPATH,
                        "//button[@class='float-right btn primary-button col-lg-6 mt-4' and text()=' Rechnung überprüfen und übermitteln ']").click()

    time.sleep(5)

    driver.find_element(By.XPATH,
                        "//button[@class='float-right btn primary-button pl-5 pr-5' and text()='Rechnung senden']").click()
    log.info("Bill sent successfully :: End of flow ")