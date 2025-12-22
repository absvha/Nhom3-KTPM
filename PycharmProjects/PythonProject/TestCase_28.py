import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTC028():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        time.sleep(5)
        self.driver.quit()

    def test_tC028(self):
        # 1. Truy cập trang
        self.driver.get("http://hauiproj.somee.com/Default.aspx")
        self.driver.maximize_window()

        # 2. Vào trang Đăng ký
        self.driver.find_element(By.ID, "LinkDK").click()

        # ❌ 3. KHÔNG nhập bất kỳ trường nào (đúng TC028)

        # 4. Click Đăng ký
        time.sleep(2)
        btn_dangky = self.driver.find_element(By.ID, "ContentPlaceHolder1_btDangky")
        self.driver.execute_script("arguments[0].click();", btn_dangky)

        # 5. ASSERT – kiểm tra thông báo lỗi (LINH HOẠT)
        thong_bao = self.driver.find_element(
            By.ID, "ContentPlaceHolder1_lblThongBao"
        ).text.strip()

        print("Thông báo hệ thống:", thong_bao)

        # Chỉ cần hệ thống báo lỗi liên quan đến tài khoản (trường bắt buộc đầu tiên)
        assert "tài khoản" in thong_bao.lower()
