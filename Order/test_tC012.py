import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTC012():

    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)

    def teardown_method(self, method):
        self.driver.quit()

    def test_tC012(self):
        # ===== TC-012: Thanh toán khi CHƯA đăng nhập =====

        # 1. Mở trang giỏ hàng
        self.driver.get("http://hauiproj.somee.com/Giohang.aspx")
        self.driver.set_window_size(1200, 650)
        time.sleep(1)

        # 2. Click menu Sản phẩm
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#HyperLink2 > li"))
        ).click()
        time.sleep(1)

        # 3. Click sản phẩm đầu tiên
        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "ContentPlaceHolder1_DataList1_Label1_0")
            )
        ).click()
        time.sleep(1)

        # 4. Thêm vào giỏ hàng (FIX lỗi click bị che)
        btn_add = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "ContentPlaceHolder1_Datalist1_btnThemVaoGio_0")
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", btn_add
        )
        time.sleep(1)

        self.driver.execute_script("arguments[0].click();", btn_add)
        time.sleep(1)

        # 5. Click Thanh toán
        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "ContentPlaceHolder1_btnThanhToan")
            )
        ).click()
        time.sleep(1)

        # 6. Kiểm tra thông báo yêu cầu đăng nhập
        thong_bao = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "ContentPlaceHolder1_lblThongBao2")
            )
        )

        assert thong_bao.text == "Vui lòng đăng ký hoặc đăng nhập để thực hiện thanh toán!"
        time.sleep(1)
