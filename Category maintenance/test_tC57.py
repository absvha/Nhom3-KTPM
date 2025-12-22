import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTC57:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)

        # ======================
        # LOGIN
        # ======================
        self.driver.get("http://hauiproj.somee.com/Dangnhap.aspx")
        self.driver.set_window_size(1212, 993)

        self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "ContentPlaceHolder1_txtTaikhoan")
            )
        ).send_keys("admin")
        time.sleep(1)

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtMatkhau"
        ).send_keys("1234")
        time.sleep(1)

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_btDangnhap"
        ).click()
        time.sleep(1)

        # Đảm bảo đăng nhập thành công
        self.wait.until(
            EC.presence_of_element_located((By.ID, "HyperLink5"))
        )

    def teardown_method(self, method):
        self.driver.quit()

    def test_tC57(self):
        # ======================
        # TC57: Cập nhật danh mục trùng tên
        # ======================

        # Mở trang quản lý danh mục
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        time.sleep(1)

        # Click nút sửa của 1 danh mục (ví dụ dòng 10)
        edit_btn = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    ".item-data:nth-child(10) .bt-style-chucnang:nth-child(1)"
                )
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", edit_btn
        )
        edit_btn.click()
        time.sleep(1)

        # Nhập tên danh mục bị trùng
        txt_name = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl10$ctl01")
            )
        )
        txt_name.clear()
        txt_name.send_keys("Kính râm")
        time.sleep(1)

        # Click cập nhật
        update_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl10$ctl02")
            )
        )
        update_btn.click()
        time.sleep(1)

        # ======================
        # KIỂM TRA KẾT QUẢ
        # ======================
        expected_msg = "Tên danh mục đã được sử dụng"

        try:
            actual_msg = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.ID, "ContentPlaceHolder1_lblTB")
                )
            ).text.strip()

            if expected_msg not in actual_msg:
                pytest.fail(
                    "TC57 FAIL - Thông báo không đúng mong đợi\n"
                    f"Expected: {expected_msg}\n"
                    f"Actual: {actual_msg}"
                )

            print("TC57 PASS - Hiển thị đúng thông báo trùng danh mục")

        except:
            pytest.fail(
                "TC57 FAIL - Hệ thống KHÔNG hiển thị thông báo lỗi "
                "khi cập nhật danh mục trùng tên"
            )
