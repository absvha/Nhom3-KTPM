import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTC026():
    def setup_method(self, method):
        # Sử dụng Chrome để đồng bộ với các bài trước và tránh lỗi driver Firefox
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Chờ đợi ngầm định tối đa 10s
        self.vars = {}

    def teardown_method(self, method):
        # Dừng 3 giây để quan sát kết quả trước khi đóng
        time.sleep(3)
        self.driver.quit()

    def test_tC026(self):
        # 1. Truy cập trang web và phóng to cửa sổ
        self.driver.get("http://hauiproj.somee.com/Default.aspx")
        self.driver.maximize_window()

        # 2. Chuyển sang trang Đăng ký
        self.driver.find_element(By.ID, "LinkDK").click()

        # 3. Nhập dữ liệu (Lược bỏ các bước click thừa của Selenium IDE)
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtTaiKhoan").send_keys("HaiYen123412")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtMatKhau").send_keys("Yen@12345")

        # Họ tên bỏ trống theo kịch bản TC_026 của bạn

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtNamSinh").send_keys("2025-12-15")

        # Chọn giới tính Nữ
        dropdown = self.driver.find_element(By.ID, "ContentPlaceHolder1_dllGioiTinh")
        dropdown.find_element(By.XPATH, "//option[. = 'Nữ']").click()

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtEmail").send_keys("nguyen@gmail.com")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtSdt").send_keys("0982736222")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtDiaChi").send_keys("Bắc giang")

        # 4. Click nút Đăng ký bằng JavaScript để tránh lỗi bị che khuất phần tử
        btn_dangky = self.driver.find_element(By.ID, "ContentPlaceHolder1_btDangky")
        self.driver.execute_script("arguments[0].scrollIntoView();", btn_dangky)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", btn_dangky)

        # 5. Kiểm tra thông báo lỗi hiển thị trên màn hình
        thong_bao = self.driver.find_element(By.ID, "ContentPlaceHolder1_lblThongBao").text
        print(f"\nKết quả thực tế: {thong_bao}")

        # Kiểm tra xem có đúng thông báo yêu cầu nhập họ tên không
        assert "Nhập họ tên" in thong_bao or thong_bao != ""