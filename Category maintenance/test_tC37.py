import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTC37():

    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)

        # ======================
        # AUTO LOGIN
        # ======================
        self.driver.get("http://hauiproj.somee.com/Dangnhap.aspx")
        self.driver.set_window_size(1200, 900)

        # Nhập tài khoản
        username_input = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "ContentPlaceHolder1_txtTaikhoan")
            )
        )
        username_input.send_keys("admin")

        # Nhập mật khẩu
        password_input = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "ContentPlaceHolder1_txtMatkhau")
            )
        )
        password_input.send_keys("1234")

        # Click đăng nhập
        login_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "ContentPlaceHolder1_btDangnhap")
            )
        )
        login_button.click()

        # ĐỢI MENU ADMIN XUẤT HIỆN (login thành công)
        self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "HyperLink5")
            )
        )

    def teardown_method(self, method):
        self.driver.quit()

    def test_tC37(self):
        # ======================
        # TEST: Xem danh mục
        # ======================

        # Click menu Danh mục
        danh_muc_menu = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#HyperLink5 > li")
            )
        )
        danh_muc_menu.click()

        # Click nội dung danh mục
        noi_dung_danh_muc = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".khung-phai2-admin > div:nth-child(1)")
            )
        )
        noi_dung_danh_muc.click()
