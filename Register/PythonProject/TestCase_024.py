import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTC024():
    def setup_method(self, method):
        # Đổi sang Chrome để chạy ổn định hơn trên Windows
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Đợi tối đa 10s để tìm thấy phần tử
        self.vars = {}

    def teardown_method(self, method):
        # Giữ trình duyệt lại 3 giây để bạn xem kết quả trước khi đóng
        time.sleep(3)
        self.driver.quit()

    def test_tC024(self):
        self.driver.get("http://hauiproj.somee.com/Default.aspx")
        self.driver.maximize_window()  # Mở to để không bị các phần tử che khuất

        # Click Đăng ký
        self.driver.find_element(By.ID, "LinkDK").click()

        # Điền thông tin (Bỏ qua các bước .click() thừa của IDE để tránh lỗi)
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtMatKhau").send_keys("Yen@12345")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtHoTen").send_keys("Nguyễn Thị Hải Yến")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtNamSinh").send_keys("2025-12-15")

        # Chọn giới tính Nữ
        dropdown = self.driver.find_element(By.ID, "ContentPlaceHolder1_dllGioiTinh")
        dropdown.find_element(By.XPATH, "//option[. = 'Nữ']").click()

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtEmail").send_keys("nguyenhaiyen321312@gmail.com")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtSdt").send_keys("0869621094")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtDiaChi").send_keys("Bắc Ninh")

        # Cuộn trang xuống và click bằng JavaScript để tránh lỗi bị che (Intercepted)
        btn_dangky = self.driver.find_element(By.ID, "ContentPlaceHolder1_btDangky")
        self.driver.execute_script("arguments[0].scrollIntoView();", btn_dangky)
        self.driver.execute_script("arguments[0].click();", btn_dangky)

        # Kiểm tra thông báo lỗi (Assertion)
        thong_bao = self.driver.find_element(By.ID, "ContentPlaceHolder1_lblThongBao").text
        print(f"\nKết quả thông báo: {thong_bao}")
        assert "Nhập tài khoản" in thong_bao