import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTC023():
    def setup_method(self, method):
        # Khởi tạo trình duyệt Chrome
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        # Dừng 5 giây để quan sát kết quả
        time.sleep(5)
        self.driver.quit()

    # Hàm gõ chậm
    def slow_send_keys(self, element, text, delay=0.01):
        for char in text:
            element.send_keys(char)
            time.sleep(delay)

    def test_tC023(self):
        # 1. Truy cập trang web
        self.driver.get("http://hauiproj.somee.com/Default.aspx")
        self.driver.maximize_window()

        # 2. Click Đăng ký
        self.driver.find_element(By.ID, "LinkDK").click()

        # 3. Nhập tài khoản ĐÃ TỒN TẠI
        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtTaiKhoan"),
            "HaiYen15s"
        )

        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtMatKhau"),
            "Yen@12345"
        )

        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtHoTen"),
            "Nguyễn Thị Hải Yến"
        )

        # Chọn ngày sinh bằng JavaScript
        date_input = self.driver.find_element(By.ID, "ContentPlaceHolder1_txtNamSinh")
        self.driver.execute_script(
            "arguments[0].value = '2005-12-15';", date_input
        )
        time.sleep(1)

        # Chọn giới tính Nữ
        dropdown = self.driver.find_element(By.ID, "ContentPlaceHolder1_dllGioiTinh")
        dropdown.find_element(By.XPATH, "//option[. = 'Nữ']").click()

        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtEmail"),
            "nguyenhaiyen321312@gmail.com"
        )

        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtSdt"),
            "0869621094"
        )

        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtDiaChi"),
            "Bắc Ninh"
        )

        # 4. Click Đăng ký
        time.sleep(2)
        btn_dangky = self.driver.find_element(By.ID, "ContentPlaceHolder1_btDangky")
        self.driver.execute_script("arguments[0].click();", btn_dangky)

        # 5. ASSERT – kiểm tra thông báo tài khoản đã tồn tại
        thong_bao = self.driver.find_element(
            By.ID, "ContentPlaceHolder1_lblThongBao"
        ).text.strip()

        print("Thông báo hệ thống:", thong_bao)

        # ASSERT LINH HOẠT – chỉ cần đúng ý
        assert "tài khoản" in thong_bao.lower() and "đã" in thong_bao.lower()
