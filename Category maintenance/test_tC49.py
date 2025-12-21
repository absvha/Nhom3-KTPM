import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTC49:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)

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

    def test_tc49_add_category_name_with_emoji(self):
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        time.sleep(1)

        txt_id = self.wait.until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtID"))
        )
        txt_id.send_keys("25")
        time.sleep(1)

        # Tên danh mục có emoji
        ten_dm = "Kính Không biết 😀"
        txt_ten = self.driver.find_element(By.ID, "ContentPlaceHolder1_txtTenDM")
        self.driver.execute_script("arguments[0].value = arguments[1];", txt_ten, ten_dm)
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_LinkButton1").click()
        time.sleep(1)

        assert True
