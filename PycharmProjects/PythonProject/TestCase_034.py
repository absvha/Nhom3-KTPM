import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTC034():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        time.sleep(3)
        self.driver.quit()

    def test_tC034(self):
        # 1. Truy cập trang web
        self.driver.get("http://hauiproj.somee.com/Default.aspx")
        self.driver.maximize_window()

        # 2. Vào trang Đăng ký
        self.driver.find_element(By.ID, "LinkDK").click()

        # 3. Nhập dữ liệu HỢP LỆ (tránh che lỗi ngày sinh)
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtTaiKhoan").send_keys(
            f"HaiYen{int(time.time())}"
        )
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtMatKhau").send_keys("Yen@12345")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtHoTen").send_keys(
            "Nguyễn Thị Hải Yến"
        )

        # Ngày sinh KHÔNG TỒN TẠI
        date_input = self.driver.find_element(By.ID, "ContentPlaceHolder1_txtNamSinh")
        self.driver.execute_script(
            "arguments[0].value = '1111-12-15';", date_input
        )
        time.sleep(1)

        # Giới tính
        dropdown = self.driver.find_element(By.ID, "ContentPlaceHolder1_dllGioiTinh")
        dropdown.find_element(By.XPATH, "//option[. = 'Nữ']").click()

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtEmail").send_keys(
            "test034@gmail.com"
        )
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtSdt").send_keys("0873624421")
        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtDiaChi").send_keys("Bồng Lai")

        # 4. Click Đăng ký
        btn_dangky = self.driver.find_element(By.ID, "ContentPlaceHolder1_btDangky")
        self.driver.execute_script("arguments[0].scrollIntoView();", btn_dangky)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", btn_dangky)

        # 5. ASSERT AN TOÀN – KHÔNG BỊ CRASH
        thong_bao_elements = self.driver.find_elements(
            By.ID, "ContentPlaceHolder1_lblThongBao"
        )

        # 👉 Nếu KHÔNG có thông báo → FAIL (phát hiện bug)
        assert len(thong_bao_elements) > 0, (
            "FAIL: Hệ thống KHÔNG hiển thị thông báo lỗi khi nhập ngày sinh không tồn tại"
        )

        thong_bao = thong_bao_elements[0].text.strip()
        print(f"\nThông báo nhận được: '{thong_bao}'")

        # Nếu có thông báo thì kiểm tra nội dung
        assert "ngày sinh" in thong_bao.lower()
