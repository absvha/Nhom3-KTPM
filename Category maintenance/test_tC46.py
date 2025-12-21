import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTC46:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)

        # LOGIN
        self.driver.get("http://hauiproj.somee.com/Dangnhap.aspx")
        self.driver.set_window_size(1200, 900)

        self.wait.until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtTaikhoan"))
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

        self.wait.until(
            EC.presence_of_element_located((By.ID, "HyperLink5"))
        )

    def teardown_method(self, method):
        self.driver.quit()

    def test_TC46(self):
        # Truy cập trực tiếp trang quản lý danh mục
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        time.sleep(1)

        # Nhập ID hợp lệ
        txt_id = self.wait.until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtID"))
        )
        txt_id.clear()
        txt_id.send_keys("22")
        time.sleep(1)

        # Nhập tên danh mục đã tồn tại
        txt_name = self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtTenDM"
        )
        txt_name.clear()
        txt_name.send_keys("Kính cận")
        time.sleep(1)

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_LinkButton1"
        ).click()
        time.sleep(1)

        msg = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "ContentPlaceHolder1_lblThongBao")
            )
        ).text.strip()

        assert msg == "Tên danh mục đã được sử dụng!"
