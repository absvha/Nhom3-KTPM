import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

URL = "http://hauiproj.somee.com/Default.aspx"

USER_1 = "abc"
PASS_1 = "abc"

USER_2 = "admin"
PASS_2 = "1234"


class TestLoginTwoTabsSplitScreen:

    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1600, 900)
        self.wait = WebDriverWait(self.driver, 5)

    def slow(self, seconds=1):
        time.sleep(seconds)

    def teardown_method(self):
        time.sleep(1)
        self.driver.quit()

    def open_login_form(self):
        self.driver.get(URL)
        self.slow(1)

        self.wait.until(
            EC.element_to_be_clickable((By.ID, "LinkDN"))
        ).click()
        self.slow(1)

    def login(self, username, password):
        user_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtTaikhoan"))
        )
        user_input.clear()
        user_input.send_keys(username)
        self.slow(1)

        pass_input = self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtMatkhau")
        pass_input.clear()
        pass_input.send_keys(password)
        self.slow(1)

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_btDangnhap"
        ).click()
        self.slow(1)

    def test_two_tabs_same_login_form(self):
        # TAB 1
        self.open_login_form()

        # TAB 2
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.open_login_form()

        # TAB 1 đăng nhập
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.login(USER_1, PASS_1)

        self.wait.until(
            EC.presence_of_element_located((By.ID, "LinkDX"))
        )
        self.slow(2)

        # TAB 2 đăng nhập
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.login(USER_2, PASS_2)

        # EXPECTED: PHẢI có thông báo lỗi
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, "ContentPlaceHolder1_txtThongbaoDN")
                )
            )
            # Nếu có thông báo → test PASS (nhưng thực tế KHÔNG có)
            assert True

        except TimeoutException:
            # KHÔNG có thông báo → FAIL 
            pytest.fail(
                "FAIL: Hệ thống dùng chung session cho nhiều tab, không tách phiên theo tab / request."
            )
