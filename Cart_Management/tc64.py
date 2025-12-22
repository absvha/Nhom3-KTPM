# Auto-converted from Selenium IDE .side (quanlygiohang) on 2025-12-14
# Tests: TC59 - TC70
#
# Requirements:
#   pip install selenium
# Run:
#   python -m unittest -v tc59_tc70_selenium.py
#
# Notes:
# - Uses explicit waits to reduce "element not found" timing issues.
# - If you're on Selenium >= 4.6, Selenium Manager can auto-manage drivers.
#   Otherwise, install the browser driver (chromedriver/geckodriver) and ensure it's on PATH.

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def parse_locator(target: str):
    """Convert Selenium IDE locator string to (By, value)."""
    if target.startswith("css="):
        return By.CSS_SELECTOR, target[len("css="):]
    if target.startswith("id="):
        return By.ID, target[len("id="):]
    if target.startswith("xpath="):
        return By.XPATH, target[len("xpath="):]
    if target.startswith("name="):
        return By.NAME, target[len("name="):]
    if target.startswith("linkText="):
        return By.LINK_TEXT, target[len("linkText="):]
    # Fallback: treat as CSS if it looks like a CSS selector, else XPath
    if target.startswith("//") or target.startswith("(//"):
        return By.XPATH, target
    return By.CSS_SELECTOR, target


class BaseSeleniumIDETest(unittest.TestCase):
    WAIT_SECONDS = 10

    def setUp(self):
        # Change to webdriver.Firefox() if you prefer Firefox
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless=new")  # uncomment if you want headless
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, self.WAIT_SECONDS)

    def tearDown(self):
        self.driver.quit()

    # --- helpers ---
    def _open(self, url: str):
        self.driver.get(url)

    def _set_window_size(self, size: str):
        w, h = size.lower().split("x")
        self.driver.set_window_size(int(w), int(h))

    def _click(self, target: str):
        by, value = parse_locator(target)
        el = self.wait.until(EC.element_to_be_clickable((by, value)))
        el.click()

    def _type(self, target: str, value: str):
        by, loc = parse_locator(target)
        el = self.wait.until(EC.presence_of_element_located((by, loc)))
        # Wait clickable too (often needed for inputs)
        self.wait.until(EC.element_to_be_clickable((by, loc)))
        el.clear()
        el.send_keys(value)

class Test_TC64(BaseSeleniumIDETest):
    def test_TC64(self):
        self._open("http://hauiproj.somee.com/Default.aspx")
        self._set_window_size("1015x695")
        self._click("css=.menu-trai a:nth-child(2) > li")
        self._click("id=ContentPlaceHolder1_DataList1_Image1_3")
        self._click("id=ContentPlaceHolder1_Datalist1_txtSoLuong_0")
        self._type("id=ContentPlaceHolder1_Datalist1_txtSoLuong_0", "99999")
        self._click("id=ContentPlaceHolder1_Datalist1_btnThemVaoGio_0")


if __name__ == '__main__':
    import unittest
    unittest.main(verbosity=2)
