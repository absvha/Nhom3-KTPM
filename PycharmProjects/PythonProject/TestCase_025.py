import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTC025():
    def setup_method(self, method):
        # Đổi sang Chrome để chạy ổn định trên Windows
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Chờ tối đa 10s để tìm thấy phần tử
        self.vars = {}

    def teardown_method(self, method):
        # Tạm dừng 3 giây để bạn xem thông báo trước khi đóng
        time.sleep(3)
        self.driver.quit()

    def test_tC025(self):
        # 1. Truy cập trang web
        self.driver.get("http://hauiproj.somee.com/Default.aspx")
        self.driver.maximize_window()

        # 2. Click vào link Đăng ký
        self.driver.find_element(By.ID, "LinkDK").click()

        # 3. Điền các thông tin (Bỏ qua các bước .click() thừa của IDE)
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtTaiKhoan").send_keys("HaiYen123412")

        # Lưu ý: TC này bỏ trống Mật khẩu để kiểm tra thông báo lỗi

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtHoTen").send_keys("Nguyễn Thị Hải Yến")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtNamSinh").send_keys("2025-12-15")

        # Chọn giới tính Nữ
        dropdown = self.driver.find_element(By.ID, "ContentPlaceHolder1_dllGioiTinh")
        dropdown.find_element(By.XPATH, "//option[. = 'Nữ']").click()

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtEmail").send_keys("nguyen@gmail.com")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtSdt").send_keys("0982736222")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtDiaChi").send_keys("Bắc giang")

        # 4. Click nút Đăng ký bằng JavaScript để tránh lỗi ElementClickIntercepted
        btn_dangky = self.driver.find_element(By.ID, "ContentPlaceHolder1_btDangky")
        self.driver.execute_script("arguments[0].scrollIntoView();", btn_dangky)  # Cuộn xuống nút
        time.sleep(1)  # Chờ 1 giây cho trang ổn định
        self.driver.execute_script("arguments[0].click();", btn_dangky)

        # 5. Kiểm tra thông báo lỗi có đúng là "Nhập mật khẩu" không
        thong_bao = self.driver.find_element(By.ID, "ContentPlaceHolder1_lblThongBao").text
        print(f"\nThông báo nhận được: {thong_bao}")
        assert "Nhập mật khẩu" in thong_bao