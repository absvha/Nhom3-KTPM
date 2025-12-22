import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTC026():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        time.sleep(5)
        self.driver.quit()

    # Hàm gõ chậm – GIỮ ĐÚNG FORM BẠN ĐANG DÙNG
    def slow_send_keys(self, element, text, delay=0.01):
        for char in text:
            element.send_keys(char)
            time.sleep(delay)

    def test_tC026(self):
        # 1. Truy cập trang
        self.driver.get("http://hauiproj.somee.com/Default.aspx")
        self.driver.maximize_window()

        # 2. Vào trang Đăng ký
        self.driver.find_element(By.ID, "LinkDK").click()

        # 3. Nhập tài khoản
        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtTaiKhoan"),
            "HaiYen123412"
        )

        # 4. Nhập mật khẩu
        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtMatKhau"),
            "Yen@12345"
        )

        # ❌ KHÔNG nhập HỌ TÊN (ĐÚNG TC026)

        # 5. Chọn ngày sinh bằng JavaScript
        date_input = self.driver.find_element(By.ID, "ContentPlaceHolder1_txtNamSinh")
        self.driver.execute_script(
            "arguments[0].value = '2005-12-15';", date_input
        )
        time.sleep(1)

        # 6. Chọn giới tính Nữ
        dropdown = self.driver.find_element(By.ID, "ContentPlaceHolder1_dllGioiTinh")
        dropdown.find_element(By.XPATH, "//option[. = 'Nữ']").click()

        # 7. Nhập email
        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtEmail"),
            "nguyen@gmail.com"
        )

        # 8. Nhập số điện thoại
        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtSdt"),
            "0982736222"
        )

        # 9. Nhập địa chỉ
        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtDiaChi"),
            "Bắc Giang"
        )

        # 10. Click Đăng ký
        time.sleep(2)
        btn_dangky = self.driver.find_element(By.ID, "ContentPlaceHolder1_btDangky")
        self.driver.execute_script("arguments[0].click();", btn_dangky)

        # 11. ASSERT – LINH HOẠT (KHÔNG FAIL VẶT)
        thong_bao = self.driver.find_element(
            By.ID, "ContentPlaceHolder1_lblThongBao"
        ).text.strip()

        print("Thông báo hệ thống:", thong_bao)

        assert "họ tên" in thong_bao.lower()
