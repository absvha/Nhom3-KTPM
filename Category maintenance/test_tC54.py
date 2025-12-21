import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTC54:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)

        self.driver.get("http://hauiproj.somee.com/Dangnhap.aspx")
        self.driver.set_window_size(1212, 993)

        self.wait.until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtTaikhoan"))
        ).send_keys("admin")
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtMatkhau").send_keys("1234")
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_btDangnhap").click()
        time.sleep(1)

        self.wait.until(EC.presence_of_element_located((By.ID, "HyperLink5")))

    def teardown_method(self, method):
        self.driver.quit()

    def test_tC54(self):
        self.driver.get("http://hauiproj.somee.com/Admin/Default.aspx")
        time.sleep(1)

        link = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#HyperLink5 > li"))
        )
        self.driver.execute_script("arguments[0].click();", link)
        time.sleep(1)

        edit_btn = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".item-data:nth-child(7) .bt-style-chucnang:nth-child(1)")
            )
        )
        self.driver.execute_script("arguments[0].click();", edit_btn)
        time.sleep(1)

        input_desc = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl07$ctl01")
            )
        )
        input_desc.send_keys(
            "Danh mục tổng hợp các bài viết hướng dẫn lập trình và phân tích dữ liệu nâng cao"
        )
        time.sleep(1)

        self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl07$ctl02"
        ).click()
        time.sleep(1)

        error = self.wait.until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_lblTB"))
        ).text

        assert "String or binary data would be truncated" in error
