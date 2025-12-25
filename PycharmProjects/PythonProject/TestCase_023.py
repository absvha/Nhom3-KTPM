import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTC023():
    def setup_method(self, method):
        # Khởi tạo trình duyệt Chrome
        self.driver = webdriver.Chrome()
        # Chờ tối đa 10 giây để tìm phần tử
        self.driver.implicitly_wait(10)
        self.vars = {}

    def teardown_method(self, method):
        # Dừng 5 giây để quan sát kết quả trước khi đóng trình duyệt
        time.sleep(5)
        self.driver.quit()

    # Hàm nhập dữ liệu chậm để mô phỏng người dùng thật khi demo cho giáo viên
    def slow_send_keys(self, element, text, delay=0.01):
        for char in text:
            element.send_keys(char)
            time.sleep(delay)

    def test_tC023(self):
        # Truy cập trang web
        self.driver.get("http://hauiproj.somee.com/Default.aspx")
        self.driver.maximize_window()

        # Click vào liên kết Đăng ký
        self.driver.find_element(By.ID, "LinkDK").click()

        # Nhập tên tài khoản (gõ chậm để dễ quan sát)
        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtTaiKhoan"),
<<<<<<< HEAD
            "#@"
=======
            "HaiYen15s21"
>>>>>>> a5fde3576beaadfa525b5e6fe751be89ccd969c7
        )

        # Nhập mật khẩu
        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtMatKhau"),
            "Yen@12345"
        )

        # Nhập họ tên
        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtHoTen"),
            "Nguyễn Thị Hải Yến"
        )

        # Nhập năm sinh
        # Chọn ngày sinh bằng JavaScript (input type=date)
        date_input = self.driver.find_element(By.ID, "ContentPlaceHolder1_txtNamSinh")
        self.driver.execute_script(
            "arguments[0].value = '2005-12-15';", date_input
        )
        time.sleep(1)  # dừng nhẹ để giáo viên nhìn thấy

        # Chọn giới tính Nữ
        dropdown = self.driver.find_element(By.ID, "ContentPlaceHolder1_dllGioiTinh")
        dropdown.find_element(By.XPATH, "//option[. = 'Nữ']").click()

        # Nhập email
        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtEmail"),
            "nguyenhaiyen321312@gmail.com"
        )

        # Nhập số điện thoại
        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtSdt"),
            "0869621094"
        )

        # Nhập địa chỉ
        self.slow_send_keys(
            self.driver.find_element(By.ID, "ContentPlaceHolder1_txtDiaChi"),
            "Bắc Ninh"
        )

        # Chờ 2 giây rồi click nút Đăng ký
        time.sleep(2)
        btn_dangky = self.driver.find_element(By.ID, "ContentPlaceHolder1_btDangky")
        self.driver.execute_script("arguments[0].click();", btn_dangky)
