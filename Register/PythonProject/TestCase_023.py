import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTC023():
    def setup_method(self, method):
        # Đổi thành Chrome nếu bạn không dùng Firefox
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Chờ tối đa 10s nếu không tìm thấy phần tử
        self.vars = {}

    def teardown_method(self, method):
        time.sleep(5)  # Dừng 5s để bạn kịp nhìn kết quả trước khi đóng
        self.driver.quit()

    def test_tC023(self):
        self.driver.get("http://hauiproj.somee.com/Default.aspx")
        self.driver.maximize_window()  # Mở to màn hình để tránh bị che

        self.driver.find_element(By.ID, "LinkDK").click()
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtTaiKhoan").send_keys("HaiYen1235623343")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtMatKhau").send_keys("Yen@12345")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtHoTen").send_keys("Nguyễn Thị hải Yến")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtNamSinh").send_keys("2025-12-15")

        # Chọn giới tính
        dropdown = self.driver.find_element(By.ID, "ContentPlaceHolder1_dllGioiTinh")
        dropdown.find_element(By.XPATH, "//option[. = 'Nữ']").click()

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtEmail").send_keys("nguyenhaiyen321312@gmail.com")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtSdt").send_keys("0869621094")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtDiaChi").send_keys("Bắc Ninh")

        # Dùng JavaScript để click nút Đăng ký nhằm tránh lỗi bị che (Intercepted)
        time.sleep(2)  # Đợi một chút cho chắc chắn
        btn_dangky = self.driver.find_element(By.ID, "ContentPlaceHolder1_btDangky")
        self.driver.execute_script("arguments[0].click();", btn_dangky)