import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTC48:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)

        # ======================
        # LOGIN ADMIN
        # ======================
        self.driver.get("http://hauiproj.somee.com/Dangnhap.aspx")
        self.driver.set_window_size(1280, 987)

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

        # Đảm bảo login thành công
        self.wait.until(
            EC.presence_of_element_located((By.ID, "HyperLink5"))
        )

    def teardown_method(self, method):
        self.driver.quit()

    def test_tC48(self):
        # ======================
        # TC48: Thêm danh mục với tên vượt quá độ dài cho phép
        # ======================

        # Mở trang quản lý danh mục
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        time.sleep(1)

        # Nhập ID hợp lệ
        txt_id = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "ContentPlaceHolder1_txtID")
            )
        )
        txt_id.clear()
        txt_id.send_keys("24")
        time.sleep(1)

        # Nhập tên danh mục vượt quá số ký tự cho phép
        txt_name = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "ContentPlaceHolder1_txtTenDM")
            )
        )
        txt_name.clear()
        txt_name.send_keys(
            "Danh mục tổng hợp các bài viết hướng dẫn lập trình "
            "và phân tích dữ liệu nâng cao"
        )
        time.sleep(1)

        # Click nút thêm
        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_LinkButton1"
        ).click()
        time.sleep(1)

        # ======================
        # KIỂM TRA KẾT QUẢ
        # ======================
        expected_msg = "Số từ vượt quá ký tự"

        try:
            actual_msg = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.ID, "ContentPlaceHolder1_lblError")
                )
            ).text.strip()

            if expected_msg not in actual_msg:
                pytest.fail(
                    "TC48 FAIL - Thông báo không đúng mong đợi\n"
                    f"Expected: {expected_msg}\n"
                    f"Actual: {actual_msg}"
                )

            print("TC48 PASS - Hiển thị đúng thông báo vượt quá ký tự")

        except:
            pytest.fail(
                "TC48 FAIL - Hệ thống KHÔNG hiển thị thông báo lỗi "
                "khi tên danh mục vượt quá độ dài cho phép"
            )
