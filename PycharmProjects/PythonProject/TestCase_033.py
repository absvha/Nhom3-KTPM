import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTC033():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        time.sleep(5)
        self.driver.quit()

    # Hàm gõ chậm để demo rõ cho giảng viên
    def slow_send_keys(self, element, text, delay=0.01):
        for char in text:
            element.send_keys(char)
            time.sleep(delay)

    def test_tC033(self):
        # 1. Truy cập trang web
        self.driver.get("http://hauiproj.somee.com/Default.aspx")
        self.driver.maximize_window()

        # 2. Vào trang Đăng ký
        self.driver.find_element(By.ID, "LinkDK").click()

        # 3. Nhập dữ liệu HỢP LỆ để KHÔNG che lỗi họ tên
        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtTaiKhoan"),
            f"HaiYen{int(time.time())}"  # tránh trùng tài khoản
        )

        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtMatKhau"),
            "Yen@12345"
        )

        # ❌ Họ tên chứa ký tự đặc biệt (DỮ LIỆU TEST)
        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtHoTen"),
            "Nguyễn Thị Hải Yến@#"
        )

        # Ngày sinh hợp lệ
        date_input = self.driver.find_element(By.ID, "ContentPlaceHolder1_txtNamSinh")
        self.driver.execute_script(
            "arguments[0].value = '2005-12-15';", date_input
        )
        time.sleep(1)

        # Giới tính
        dropdown = self.driver.find_element(By.ID, "ContentPlaceHolder1_dllGioiTinh")
        dropdown.find_element(By.XPATH, "//option[. = 'Nữ']").click()

        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtEmail"),
            "test033@gmail.com"
        )

        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtSdt"),
            "0873624421"
        )

        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtDiaChi"),
            "Bồng Lai"
        )

        # 4. Click Đăng ký
        btn_dangky = self.driver.find_element(By.ID, "ContentPlaceHolder1_btDangky")
        self.driver.execute_script("arguments[0].scrollIntoView();", btn_dangky)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", btn_dangky)

        # 5. ASSERT AN TOÀN – KHÔNG BỊ CRASH
        thong_bao_elements = self.driver.find_elements(
            By.ID, "ContentPlaceHolder1_lblThongBao"
        )

        # Nếu KHÔNG có thông báo → FAIL (phát hiện BUG)
        assert len(thong_bao_elements) > 0, (
            "FAIL: Hệ thống KHÔNG hiển thị thông báo lỗi khi họ tên chứa ký tự đặc biệt"
        )

        thong_bao = thong_bao_elements[0].text.lower().strip()
        print(f"\nThông báo nhận được: '{thong_bao}'")

        # Assert đúng NGHIỆP VỤ (linh hoạt)
        assert "họ tên" in thong_bao or "ký tự" in thong_bao, (
            "FAIL: Thông báo lỗi KHÔNG liên quan đến họ tên"
        )
