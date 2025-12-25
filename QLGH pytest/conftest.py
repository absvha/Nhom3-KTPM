import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

DEFAULT_TIMEOUT = float(os.getenv("SELENIUM_TIMEOUT", "15"))

def locator_from_side_target(target: str):
    # Selenium IDE (.side) target formats commonly look like:
    #   "css=...", "id=...", "xpath=...", "linkText=...", "name=..."
    # Sometimes target may already be a raw CSS selector; treat it as CSS in that case.
    if target.startswith("css="):
        return (By.CSS_SELECTOR, target[len("css="):])
    if target.startswith("id="):
        return (By.ID, target[len("id="):])
    if target.startswith("xpath="):
        return (By.XPATH, target[len("xpath="):])
    if target.startswith("linkText="):
        return (By.LINK_TEXT, target[len("linkText="):])
    if target.startswith("name="):
        return (By.NAME, target[len("name="):])
    # Fallback: treat as CSS selector
    return (By.CSS_SELECTOR, target)

def wait_find(driver, target: str):
    by, sel = locator_from_side_target(target)
    return WebDriverWait(driver, DEFAULT_TIMEOUT).until(EC.presence_of_element_located((by, sel)))

def wait_click(driver, target: str):
    by, sel = locator_from_side_target(target)
    el = WebDriverWait(driver, DEFAULT_TIMEOUT).until(EC.element_to_be_clickable((by, sel)))
    el.click()
    return el

@pytest.fixture
def driver():
    # You can switch to headed mode by removing the --headless=new option below.
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    options.add_argument("--window-size=1200,900")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    drv = webdriver.Chrome(options=options)
    try:
        yield drv
    finally:
        drv.quit()
