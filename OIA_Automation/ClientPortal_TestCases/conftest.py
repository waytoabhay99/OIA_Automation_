from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = None


@pytest.fixture()
def launch_browser():
    global driver
    option = Options()
    option.add_argument("--disable-notifications")
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
    yield driver
    driver.close()


@pytest.fixture()
def login_client(launch_browser):
    driver = launch_browser
    driver.get("https://oiaclientqa.z6.web.core.windows.net/login")
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    driver.find_element(By.XPATH, '//input[@type="email"]').send_keys("a@b.com")
    driver.find_element(By.XPATH, '//input[@type="password"]').send_keys('test')
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    driver.implicitly_wait(10)
    yield driver
    '''
    driver.find_element(By.ID, 'dropdownBasic1').click()
    driver.find_element(By.XPATH, '//span[@class="buttonLabel" and text()="Abmelden"]').click()
    driver.find_element(By.XPATH, '// button[text() = "Abmelden"]').click()
    '''


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
     Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
