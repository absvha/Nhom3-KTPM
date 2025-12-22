import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTC58:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)

        self.driver.get("http://hauiproj.somee.com/Dangnhap.aspx")
        self.driver.set_window_size(1212, 993)

        self.wait.until(EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtTaikhoan"))).send_keys("admin")
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtMatkhau").send_keys("1234")
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_btDangnhap").click()
        time.sleep(1)

        self.wait.until(EC.presence_of_element_located((By.ID, "HyperLink5")))

    def teardown_method(self, method):
        self.driver.quit()

    def test_tC58(self):
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        time.sleep(1)

        menu = self.wait.until(EC.presence_of_element_located((By.ID, "HyperLink5")))
        self.driver.execute_script("arguments[0].click();", menu)
        time.sleep(1)

        delete_btn = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".item-data:nth-child(7) .bt-style-chucnang:nth-child(2)")
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", delete_btn)
        self.driver.execute_script("arguments[0].click();", delete_btn)
        time.sleep(1)

        panel = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".khung-admin > .khung-phai2-admin")
            )
        )
        self.driver.execute_script("arguments[0].click();", panel)
        time.sleep(1)

        assert True