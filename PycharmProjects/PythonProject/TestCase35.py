import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTC035:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        time.sleep(3)
        self.driver.quit()

    def test_tC035_sdt_sai(self):
        driver = self.driver

        # 1. Truy cập trang web
        driver.get("http://hauiproj.somee.com/Default.aspx")
        driver.maximize_window()

        # 2. Vào trang Đăng ký
        driver.find_element(By.ID, "LinkDK").click()

        # 3. Nhập dữ liệu hợp lệ để không che lỗi khác
        driver.find_element(By.ID, "ContentPlaceHolder1_txtTaiKhoan").send_keys(
            f"HaiYen{int(time.time())}"
        )
        driver.find_element(By.ID, "ContentPlaceHolder1_txtMatKhau").send_keys(
            "Yen@12345"
        )
        driver.find_element(By.ID, "ContentPlaceHolder1_txtHoTen").send_keys(
            "Nguyễn Thị Hải Yến"
        )
        driver.find_element(By.ID, "ContentPlaceHolder1_txtNamSinh").send_keys(
            "2005-12-15"
        )

        # Giới tính
        dropdown = driver.find_element(By.ID, "ContentPlaceHolder1_dllGioiTinh")
        dropdown.find_element(By.XPATH, "//option[. = 'Nữ']").click()

        # Email hợp lệ
        driver.find_element(By.ID, "ContentPlaceHolder1_txtEmail").send_keys(
            "nguyenhaiyen321@gmail.com"
        )

        # ❌ Số điện thoại sai định dạng (ví dụ nhập chữ)
        driver.find_element(By.ID, "ContentPlaceHolder1_txtSdt").send_keys(
            "08736abc421"
        )

        # Địa chỉ hợp lệ
        driver.find_element(By.ID, "ContentPlaceHolder1_txtDiaChi").send_keys(
            "Bồng Lai"
        )

        # 4. Click Đăng ký
        btn_dangky = driver.find_element(By.ID, "ContentPlaceHolder1_btDangky")
        driver.execute_script("arguments[0].scrollIntoView();", btn_dangky)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", btn_dangky)

        # 5. ASSERT AN TOÀN – KHÔNG CRASH
        thong_bao_elements = driver.find_elements(
            By.ID, "ContentPlaceHolder1_lblThongBao"
        )
        assert len(thong_bao_elements) > 0, (
            "FAIL: Hệ thống KHÔNG hiển thị thông báo lỗi khi số điện thoại sai định dạng"
        )

        thong_bao = thong_bao_elements[0].text.lower().strip()
        print(f"\nThông báo nhận được: '{thong_bao}'")

        # Assert đúng nghiệp vụ – thông báo liên quan số điện thoại
        assert "số điện thoại" in thong_bao or "điện thoại" in thong_bao, (
            "FAIL: Thông báo lỗi KHÔNG đúng cho số điện thoại sai định dạng"
        )
