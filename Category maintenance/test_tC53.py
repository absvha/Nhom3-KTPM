import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTC53():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)

        # ===== AUTO LOGIN =====
        self.driver.get("http://hauiproj.somee.com/Dangnhap.aspx")
        self.driver.set_window_size(1212, 993)

        self.wait.until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtTaikhoan"))
        ).send_keys("admin")
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtMatkhau").send_keys("1234")
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_btDangnhap").click()
        time.sleep(2)  # chờ login xong

        self.wait.until(EC.presence_of_element_located((By.ID, "HyperLink5")))

    def teardown_method(self, method):
        time.sleep(2)  # pause trước khi tắt browser
        self.driver.quit()

    def test_tC53(self):
        # ===== TEST TC53: Sửa danh mục với tên trống =====
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        time.sleep(1)

        menu = self.wait.until(EC.presence_of_element_located((By.ID, "HyperLink5")))
        self.driver.execute_script("arguments[0].click();", menu)
        time.sleep(1)

        edit_btn = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".item-data:nth-child(8) .bt-style-chucnang:nth-child(1)")
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", edit_btn)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", edit_btn)
        time.sleep(1)

        name_input = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl08$ctl01")
            )
        )
        name_input.clear()
        time.sleep(0.5)
        name_input.send_keys(" ")  # tên trống
        time.sleep(1)

        update_btn = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl08$ctl02")
            )
        )
        self.driver.execute_script("arguments[0].click();", update_btn)
        time.sleep(1)

        # VERIFY: hệ thống không validate → BUG
        error_text = self.driver.find_element(By.ID, "ContentPlaceHolder1_lblTB").text
        assert error_text == ""
