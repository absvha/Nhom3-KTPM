import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class TestTC036:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        time.sleep(3)
        self.driver.quit()

    # Hàm gõ chậm
    def slow_send_keys(self, element, text, delay=0.01):
        for char in text:
            element.send_keys(char)
            time.sleep(delay)

    def test_tC036_email_sai(self):
        driver = self.driver
        driver.get("http://hauiproj.somee.com/Default.aspx")
        driver.maximize_window()

        # Click Đăng ký
        driver.find_element(By.ID, "LinkDK").click()

        # Nhập tài khoản
        self.slow_send_keys(
            driver.find_element(By.ID, "ContentPlaceHolder1_txtTaiKhoan"),
            f"HaiYen{int(time.time())}"
        )

        # Nhập mật khẩu
        self.slow_send_keys(
            driver.find_element(By.ID, "ContentPlaceHolder1_txtMatKhau"),
            "Yen@12345"
        )

        # Họ tên hợp lệ
        self.slow_send_keys(
            driver.find_element(By.ID, "ContentPlaceHolder1_txtHoTen"),
            "Nguyễn Thị Hải Yến"
        )

        # Ngày sinh
        date_input = driver.find_element(By.ID, "ContentPlaceHolder1_txtNamSinh")
        driver.execute_script("arguments[0].value = '2005-12-15';", date_input)
        time.sleep(0.5)

        # Giới tính
        select_gender = Select(driver.find_element(By.ID, "ContentPlaceHolder1_dllGioiTinh"))
        select_gender.select_by_visible_text("Nữ")

        # **Email sai định dạng**
        self.slow_send_keys(
            driver.find_element(By.ID, "ContentPlaceHolder1_txtEmail"),
            "test036gmail.com"  # thiếu @ → invalid
        )

        # Số điện thoại
        self.slow_send_keys(
            driver.find_element(By.ID, "ContentPlaceHolder1_txtSdt"),
            "0873624421"
        )

        # Địa chỉ
        self.slow_send_keys(
            driver.find_element(By.ID, "ContentPlaceHolder1_txtDiaChi"),
            "Bồng Lai"
        )

        # Click Đăng ký
        btn_dangky = driver.find_element(By.ID, "ContentPlaceHolder1_btDangky")
        driver.execute_script("arguments[0].scrollIntoView();", btn_dangky)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", btn_dangky)

        # Wait thông báo
        lbl = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "ContentPlaceHolder1_lblThongBao"))
        )

        thong_bao = lbl.text.lower().strip()
        print(f"\nThông báo nhận được: '{thong_bao}'")

        # Assert thông báo liên quan email
        assert "email" in thong_bao, (
            "FAIL: Thông báo lỗi KHÔNG liên quan đến email"
        )
