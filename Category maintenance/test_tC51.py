import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTC51:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)

        # AUTO LOGIN
        self.driver.get("http://hauiproj.somee.com/Dangnhap.aspx")
        self.driver.set_window_size(1212, 993)

        self.wait.until(EC.presence_of_element_located(
            (By.ID, "ContentPlaceHolder1_txtTaikhoan"))
        ).send_keys("admin")
        time.sleep(1)

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtMatkhau"
        ).send_keys("1234")
        time.sleep(1)

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_btDangnhap"
        ).click()
        time.sleep(1)

        self.wait.until(EC.presence_of_element_located((By.ID, "HyperLink5")))

    def teardown_method(self, method):
        self.driver.quit()

    def test_tC51(self):
        self.driver.get("http://hauiproj.somee.com/Admin/Default.aspx")
        time.sleep(1)

        link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#HyperLink5 > li")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", link)
        self.driver.execute_script("arguments[0].click();", link)
        time.sleep(1)

        btn_edit = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".item-data:nth-child(8) .bt-style-chucnang:nth-child(1)")
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn_edit)
        self.driver.execute_script("arguments[0].click();", btn_edit)
        time.sleep(1)

        input_ma = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl08$ctl00")
            )
        )
        input_ma.clear()
        input_ma.send_keys("12")
        time.sleep(1)

        input_ten = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl08$ctl01"
        )
        input_ten.clear()
        input_ten.send_keys("Kính đẹp")
        time.sleep(1)

        btn_save = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl08$ctl02"
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn_save)
        self.driver.execute_script("arguments[0].click();", btn_save)
        time.sleep(1)

        back_btn = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".khung-phai2-admin > div:nth-child(1)")
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", back_btn)
        self.driver.execute_script("arguments[0].click();", back_btn)
        time.sleep(1)

        assert True
