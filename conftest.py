import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--headless")  # disable headless
    options.add_argument("--no-sandbox")  # develop
    # options.add_argument("--disable-gpu")
    # options.add_argument('--start-maximized')  # fullscreen
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--window-size=1920x1080")  # size of the browser
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)  # driver Chrome
    request.cls.driver = driver
    yield driver
    driver.quit()
