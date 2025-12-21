import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTC50:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)

        self.driver.get("http://hauiproj.somee.com/Dangnhap.aspx")
        self.driver.set_window_size(1200, 900)

        self.wait.until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtTaikhoan"))
        ).send_keys("admin")
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtMatkhau").send_keys("1234")
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_btDangnhap").click()
        time.sleep(1)

        self.wait.until(EC.presence_of_element_located((By.ID, "HyperLink5")))

    def teardown_method(self, method):
        self.driver.quit()

    def test_tC50(self):
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        time.sleep(1)

        link = self.wait.until(EC.presence_of_element_located((By.ID, "HyperLink5")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", link)
        self.driver.execute_script("arguments[0].click();", link)
        time.sleep(1)

        btn_edit = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".item-data:nth-child(9) .bt-style-chucnang:nth-child(1)")
            )
        )
        btn_edit.click()
        time.sleep(1)

        name_input = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl09$ctl01")
            )
        )
        name_input.clear()
        name_input.send_keys("Kính Vip")
        time.sleep(1)

        self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl09$ctl02"
        ).click()
        time.sleep(1)

        assert True
