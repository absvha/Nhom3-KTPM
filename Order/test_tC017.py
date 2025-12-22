# FIXED – ASP.NET SAFE – EMPTY PHONE TEST
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DELAY = 2.5

class TestTC17:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def teardown_method(self, method):
        self.driver.quit()

    def test_tC17_empty_phone(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # ===== 1. MỞ TRANG =====
        driver.get("http://hauiproj.somee.com/Default.aspx")
        time.sleep(DELAY)

        # ===== 2. LOGIN =====
        wait.until(EC.element_to_be_clickable((By.ID, "LinkDN"))).click()
        time.sleep(DELAY)

        wait.until(EC.visibility_of_element_located(
            (By.ID, "ContentPlaceHolder1_txtTaikhoan"))
        ).send_keys("user")

        wait.until(EC.visibility_of_element_located(
            (By.ID, "ContentPlaceHolder1_txtMatkhau"))
        ).send_keys("1234")

        wait.until(EC.element_to_be_clickable(
            (By.ID, "ContentPlaceHolder1_btDangnhap"))
        ).click()

        time.sleep(DELAY)

        # ===== 3. CHỌN SẢN PHẨM =====
        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#HyperLink2 > li"))
        ).click()
        time.sleep(DELAY)

        wait.until(EC.element_to_be_clickable(
            (By.ID, "ContentPlaceHolder1_DataList1_Image1_0"))
        ).click()
        time.sleep(DELAY)

        wait.until(EC.element_to_be_clickable(
            (By.ID, "ContentPlaceHolder1_Datalist1_btnThemVaoGio_0"))
        ).click()
        time.sleep(DELAY)

        wait.until(EC.element_to_be_clickable(
            (By.ID, "ContentPlaceHolder1_btnThanhToan"))
        ).click()

        # ===== 4. ĐỢI FORM USER RENDER =====
        wait.until(lambda d: len(d.find_elements(
            By.XPATH,
            "//input[@type='text' and contains(@id,'txt')]"
        )) >= 2)

        time.sleep(1)

        # ===== 5. LẤY TEXTBOX USER =====
        textboxes = driver.find_elements(
            By.XPATH,
            "//input[@type='text' and contains(@id,'txt')]"
        )

        # DEBUG ID (nếu cần)
        for i, el in enumerate(textboxes):
            print(f"DEBUG textbox[{i}] id =", el.get_attribute("id"))

        ten = textboxes[0]      # Tên
        sdt = textboxes[1]      # SĐT (QUAN TRỌNG)

        # ===== 6. XÓA SĐT (JS – KHÔNG TRIGGER VALIDATE SỚM) =====
        driver.execute_script("arguments[0].value='';", sdt)

        # ===== 7. ĐIỀN GHI CHÚ =====
        ghi_chu = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//textarea")
        ))
        ghi_chu.clear()
        ghi_chu.send_keys("abc")

        time.sleep(DELAY)

        # ===== 8. SUBMIT =====
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[contains(@id,'ThanhToan')]"))
        ).click()

        # ===== 9. BẮT THÔNG BÁO LỖI =====
        error_element = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'SĐT')]")
        ))

        error_text = error_element.text.strip()
        print("DEBUG ERROR TEXT:", repr(error_text))

        assert error_text == "Nhập SĐT!", f"Sai thông báo lỗi: {error_text}"

        time.sleep(DELAY)
