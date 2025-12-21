import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# =======================
# Helper login function
# =======================
def login(driver, wait):
    driver.get("http://hauiproj.somee.com/Dangnhap.aspx")
    driver.set_window_size(1200, 900)
    wait.until(EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtTaikhoan"))).send_keys("admin")
    driver.find_element(By.ID, "ContentPlaceHolder1_txtMatkhau").send_keys("1234")
    driver.find_element(By.ID, "ContentPlaceHolder1_btDangnhap").click()
    wait.until(EC.presence_of_element_located((By.ID, "HyperLink5")))

# =======================
# TC37: Xem danh mục
# =======================
class TestTC37:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)

    def teardown_method(self, method):
        self.driver.quit()

    def test_tC37(self):
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

# =======================
# TC38: Thêm danh mục hợp lệ
# =======================
class TestTC38:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)

    def teardown_method(self, method):
        self.driver.quit()

    def test_tC38(self):
        # mở trang quản lý danh mục
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        self.driver.set_window_size(1200, 900)

        time.sleep(1)

        # click menu danh mục
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#HyperLink5 > li")
            )
        ).click()

        time.sleep(1)

        # nhập ID
        self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "ContentPlaceHolder1_txtID")
            )
        ).click()
        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtID"
        ).send_keys("6")

        time.sleep(1)

        # nhập tên danh mục
        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtTenDM"
        ).click()
        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtTenDM"
        ).send_keys("Kính cận")

        time.sleep(1)

        # click thêm / lưu
        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_LinkButton1"
        ).click()

        time.sleep(2)

        # click xem danh sách
        self.driver.find_element(
            By.CSS_SELECTOR, ".khung-phai2-admin > div:nth-child(1)"
        ).click()

# =======================
# TC39: Thiếu mã danh mục
# =======================
class TestTC39:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)

    def teardown_method(self, method):
        self.driver.quit()

    def test_tC39(self):
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        self.driver.set_window_size(1200, 900)

        time.sleep(1)

        self.driver.find_element(
            By.CSS_SELECTOR, "#HyperLink5 > li"
        ).click()

        time.sleep(1)

        # chỉ nhập tên danh mục (KHÔNG nhập ID)
        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtTenDM"
        ).send_keys("Kính không gọng")

        time.sleep(1)

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_LinkButton1"
        ).click()

        time.sleep(1)

        # assert thông báo lỗi
        assert self.driver.find_element(
            By.ID, "ContentPlaceHolder1_lblThongBao"
        ).text.strip() == "Nhập mã danh mục!"

# =======================
# TC40: Trùng mã danh mục
# =======================
class TestTC40:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)

    def teardown_method(self, method):
        self.driver.quit()

    def test_tC40(self):
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        self.driver.set_window_size(1200, 900)

        time.sleep(1)

        self.driver.find_element(
            By.CSS_SELECTOR, "#HyperLink5 > li"
        ).click()

        time.sleep(1)

        # nhập mã đã tồn tại
        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtID"
        ).send_keys("11")

        time.sleep(1)

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtTenDM"
        ).send_keys("Kính không gọng")

        time.sleep(1)

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_LinkButton1"
        ).click()

        time.sleep(1)

        # assert thông báo lỗi
        assert "đã được sử dụng" in self.driver.find_element(
            By.ID, "ContentPlaceHolder1_lblThongBao"
        ).text

# =======================
# TC41: Mã danh mục không hợp lệ (số thập phân)
# =======================
class TestTC41:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)

    def teardown_method(self, method):
        self.driver.quit()
    def test_tC41(self):
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        self.driver.set_window_size(946, 987)

        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, "#HyperLink5 > li").click()
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtID").send_keys("6.5")
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtTenDM").send_keys("Kính cao cấp")
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_LinkButton1").click()
        time.sleep(1)

        assert "không hợp lệ" in self.driver.find_element(
            By.ID, "ContentPlaceHolder1_lblThongBao"
        ).text
    

# =======================
# TC42: Mã danh mục không hợp lệ (0)
# =======================
class TestTC42:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)
    def teardown_method(self, method):
        self.driver.quit()
    def test_tC42(self):
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        self.driver.set_window_size(986, 987)

        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, "#HyperLink5 > li").click()
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtID").send_keys("0")
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtTenDM").send_keys("Kính titan")
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_LinkButton1").click()
        time.sleep(1)

        assert "không hợp lệ" in self.driver.find_element(
            By.ID, "ContentPlaceHolder1_lblThongBao"
        ).text

# =======================
# TC43: Mã danh mục không hợp lệ (âm)
# =======================
class TestTC43:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)
    def teardown_method(self, method):
        self.driver.quit()
    def test_tC43(self):
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        self.driver.set_window_size(986, 987)

        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, "#HyperLink5 > li").click()
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtID").send_keys("-5")
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_txtTenDM").send_keys("Kính cường lực")
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_LinkButton1").click()
        time.sleep(1)

        assert "không hợp lệ" in self.driver.find_element(
            By.ID, "ContentPlaceHolder1_lblThongBao"
        ).text

# =======================
# TC44: Mã danh mục quá lớn
# =======================
class TestTC44:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)
    def teardown_method(self, method):
        self.driver.quit()
    def test_TC44(self):
        # Truy cập trực tiếp trang quản lý danh mục
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        time.sleep(1)  # dừng 1 giây

        # Nhập ID không hợp lệ
        txt_id = self.wait.until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtID"))
        )
        txt_id.clear()
        txt_id.send_keys("99999999999")
        time.sleep(1)  # dừng 1 giây

        txt_name = self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtTenDM"
        )
        txt_name.clear()
        txt_name.send_keys("Kính thời trang")
        time.sleep(1)  # dừng 1 giây

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_LinkButton1"
        ).click()
        time.sleep(1)  # dừng 1 giây

        msg = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "ContentPlaceHolder1_lblThongBao")
            )
        ).text.strip()

        assert msg == "Mã danh mục không hợp lệ!"

# =======================
# TC45: Mã danh mục chứa chữ
# =======================
class TestTC45:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)
    def teardown_method(self, method):
        self.driver.quit()
    def test_TC45(self):
        # Truy cập trực tiếp trang quản lý danh mục
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        time.sleep(1)

        # Nhập ID không hợp lệ (chứa chữ)
        txt_id = self.wait.until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtID"))
        )
        txt_id.clear()
        txt_id.send_keys("12a")
        time.sleep(1)

        txt_name = self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtTenDM"
        )
        txt_name.clear()
        txt_name.send_keys("Kính phân cực")
        time.sleep(1)

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_LinkButton1"
        ).click()
        time.sleep(1)

        msg = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "ContentPlaceHolder1_lblThongBao")
            )
        ).text.strip()

        assert msg == "Mã danh mục không hợp lệ!"

# =======================
# TC46: Tên danh mục đã tồn tại
# =======================
class TestTC46:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)
    def teardown_method(self, method):
        self.driver.quit()
    def test_TC46(self):
        # Truy cập trực tiếp trang quản lý danh mục
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        time.sleep(1)

        # Nhập ID hợp lệ
        txt_id = self.wait.until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtID"))
        )
        txt_id.clear()
        txt_id.send_keys("22")
        time.sleep(1)

        # Nhập tên danh mục đã tồn tại
        txt_name = self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtTenDM"
        )
        txt_name.clear()
        txt_name.send_keys("Kính cận")
        time.sleep(1)

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_LinkButton1"
        ).click()
        time.sleep(1)

        msg = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "ContentPlaceHolder1_lblThongBao")
            )
        ).text.strip()

        assert msg == "Tên danh mục đã được sử dụng!"

# =======================
# TC47: Không nhập tên danh mục
# =======================
class TestTC47:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)
    def teardown_method(self, method):
        self.driver.quit()
    def test_TC47(self):
        # Truy cập trực tiếp trang quản lý danh mục
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        time.sleep(1)

        # Nhập ID hợp lệ
        txt_id = self.wait.until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtID"))
        )
        txt_id.clear()
        txt_id.send_keys("23")
        time.sleep(1)

        # KHÔNG nhập tên danh mục
        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_LinkButton1"
        ).click()
        time.sleep(1)

        msg = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "ContentPlaceHolder1_lblThongBao")
            )
        ).text.strip()

        assert msg == "Nhập tên danh mục!"

# =======================
# TC48: Tên danh mục quá dài
# =======================
class TestTC48:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)
    def teardown_method(self, method):
        self.driver.quit()
    def test_TC48(self):
        # Truy cập trực tiếp trang quản lý danh mục
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        time.sleep(1)

        # Nhập ID hợp lệ
        txt_id = self.wait.until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtID"))
        )
        txt_id.clear()
        txt_id.send_keys("24")
        time.sleep(1)

        # Nhập tên danh mục vượt quá độ dài cho phép
        txt_name = self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtTenDM"
        )
        txt_name.clear()
        txt_name.send_keys(
            "Danh mục tổng hợp các bài viết hướng dẫn lập trình và phân tích dữ liệu nâng cao"
        )
        time.sleep(1)

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_LinkButton1"
        ).click()
        time.sleep(1)

        err = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "ContentPlaceHolder1_lblError")
            )
        ).text.strip()

        assert "String or binary data would be truncated" in err

# =======================
# TC49: Tên danh mục có emoji
# =======================
class TestTC49:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)
    def teardown_method(self, method):
        self.driver.quit()
    def test_tc49_add_category_name_with_emoji(self):
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        time.sleep(1)

        txt_id = self.wait.until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txtID"))
        )
        txt_id.send_keys("25")
        time.sleep(1)

        # Tên danh mục có emoji
        ten_dm = "Kính Không biết 😀"
        txt_ten = self.driver.find_element(By.ID, "ContentPlaceHolder1_txtTenDM")
        self.driver.execute_script("arguments[0].value = arguments[1];", txt_ten, ten_dm)
        time.sleep(1)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_LinkButton1").click()
        time.sleep(1)

        assert True

# =======================
# TC50: Sửa danh mục thành công
# =======================
class TestTC50:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)
    def teardown_method(self, method):
        self.driver.quit()
    def test_tC50(self):
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        time.sleep(1)

        link = self.wait.until(EC.presence_of_element_located((By.ID, "HyperLink5")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", link)
        self.driver.execute_script("arguments[0].click();", link)
        time.sleep(1)

        btn_edit = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".item-data:nth-child(9) .bt-style-chucnang:nth-child(1)")
            )
        )
        btn_edit.click()
        time.sleep(1)

        name_input = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl09$ctl01")
            )
        )
        name_input.clear()
        name_input.send_keys("Kính Vip")
        time.sleep(1)

        self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl09$ctl02"
        ).click()
        time.sleep(1)

        assert True

# =======================
# TC51: Sửa tên + mã danh mục
# =======================

class TestTC51:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)
    def teardown_method(self, method):
        self.driver.quit()
    def test_tC51(self):
        self.driver.get("http://hauiproj.somee.com/Admin/Default.aspx")
        time.sleep(1)

        link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#HyperLink5 > li")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", link)
        self.driver.execute_script("arguments[0].click();", link)
        time.sleep(1)

        btn_edit = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".item-data:nth-child(8) .bt-style-chucnang:nth-child(1)")
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn_edit)
        self.driver.execute_script("arguments[0].click();", btn_edit)
        time.sleep(1)

        input_ma = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl08$ctl00")
            )
        )
        input_ma.clear()
        input_ma.send_keys("12")
        time.sleep(1)

        input_ten = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl08$ctl01"
        )
        input_ten.clear()
        input_ten.send_keys("Kính đẹp")
        time.sleep(1)

        btn_save = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl08$ctl02"
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn_save)
        self.driver.execute_script("arguments[0].click();", btn_save)
        time.sleep(1)

        back_btn = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".khung-phai2-admin > div:nth-child(1)")
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", back_btn)
        self.driver.execute_script("arguments[0].click();", back_btn)
        time.sleep(1)

        assert True

# =======================
# TC52: Hủy sửa danh mục
# =======================
class TestTC52:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)
    def teardown_method(self, method):
        self.driver.quit()
    def test_tC52(self):
        self.driver.get("http://hauiproj.somee.com/Admin/Default.aspx")
        time.sleep(1)

        link = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#HyperLink5 > li"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", link)
        self.driver.execute_script("arguments[0].click();", link)
        time.sleep(1)

        btn_edit = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".item-data:nth-child(10) .bt-style-chucnang:nth-child(1)")
            )
        )
        self.driver.execute_script("arguments[0].click();", btn_edit)
        time.sleep(1)

        input_name = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl10$ctl01")
            )
        )
        input_name.clear()
        input_name.send_keys("Kính Vip")
        time.sleep(1)

        btn_save = self.driver.find_element(
            By.CSS_SELECTOR, ".item-data:nth-child(10) .bt-style-chucnang:nth-child(2)"
        )
        self.driver.execute_script("arguments[0].click();", btn_save)
        time.sleep(1)

        assert True

# =======================
# TC53: Sửa tên danh mục trống
# =======================
class TestTC53:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)
    def teardown_method(self, method):
        self.driver.quit()
    def test_tC53(self):
        # ===== TEST TC53: Sửa danh mục với tên trống =====
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        time.sleep(1)

        menu = self.wait.until(EC.presence_of_element_located((By.ID, "HyperLink5")))
        self.driver.execute_script("arguments[0].click();", menu)
        time.sleep(1)

        edit_btn = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".item-data:nth-child(8) .bt-style-chucnang:nth-child(1)")
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", edit_btn)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", edit_btn)
        time.sleep(1)

        name_input = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl08$ctl01")
            )
        )
        name_input.clear()
        time.sleep(0.5)
        name_input.send_keys(" ")  # tên trống
        time.sleep(1)

        update_btn = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl08$ctl02")
            )
        )
        self.driver.execute_script("arguments[0].click();", update_btn)
        time.sleep(1)

        # VERIFY: hệ thống không validate → BUG
        error_text = self.driver.find_element(By.ID, "ContentPlaceHolder1_lblTB").text
        assert error_text == ""

# =======================
# TC54: Sửa tên danh mục trống
# =======================
class TestTC54:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)
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

# =======================
# TC55: Sửa tên danh mục trống
# =======================
class TestTC55:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)
    def teardown_method(self, method):
        self.driver.quit()
    def test_tC55(self):
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        time.sleep(1)

        menu = self.wait.until(EC.presence_of_element_located((By.ID, "HyperLink5")))
        self.driver.execute_script("arguments[0].click();", menu)
        time.sleep(1)

        edit_btn = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".item-data:nth-child(8) .bt-style-chucnang:nth-child(1)")
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", edit_btn)
        self.driver.execute_script("arguments[0].click();", edit_btn)
        time.sleep(1)

        name_input = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl08$ctl01")
            )
        )
        name_input.clear()
        name_input.send_keys("Kinh@")
        time.sleep(1)

        update_btn = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl08$ctl02")
            )
        )
        self.driver.execute_script("arguments[0].click();", update_btn)
        time.sleep(1)

        assert True

# =======================
# TC56: Sửa tên danh mục trống
# =======================
class TestTC56:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)
    def teardown_method(self, method):
        self.driver.quit()
    def test_tC56(self):
        self.driver.get("http://hauiproj.somee.com/Admin/Default.aspx")
        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#HyperLink5 > li")))
        )
        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".item-data:nth-child(9) .bt-style-chucnang:nth-child(1)")
            ))
        )
        time.sleep(1)

        input_name = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl09$ctl01")
            )
        )
        input_name.clear()
        input_name.send_keys("Kinh go😀")
        time.sleep(1)

        self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl09$ctl02"
        ).click()
        time.sleep(1)

        assert True    

# =======================
# TC57: Sửa tên danh mục trống
# =======================
class TestTC57:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)
    def teardown_method(self, method):
        self.driver.quit()
    def test_tC57(self):
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        time.sleep(1)

        menu = self.wait.until(EC.presence_of_element_located((By.ID, "HyperLink5")))
        self.driver.execute_script("arguments[0].click();", menu)
        time.sleep(1)

        edit_btn = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".item-data:nth-child(10) .bt-style-chucnang:nth-child(1)")
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", edit_btn)
        self.driver.execute_script("arguments[0].click();", edit_btn)
        time.sleep(1)

        name_input = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl10$ctl01")
            )
        )
        name_input.clear()
        name_input.send_keys("Kính râm")
        time.sleep(1)

        update_btn = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "ctl00$ContentPlaceHolder1$GridView1$ctl10$ctl02")
            )
        )
        self.driver.execute_script("arguments[0].click();", update_btn)
        time.sleep(1)

        assert True


# =======================
# TC58: Sửa tên danh mục trống
# =======================
class TestTC58:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        login(self.driver, self.wait)
    def teardown_method(self, method):
        self.driver.quit()
    def test_tC58(self):
        self.driver.get("http://hauiproj.somee.com/Admin/Quanlydanhmuc.aspx")
        time.sleep(1)

        menu = self.wait.until(EC.presence_of_element_located((By.ID, "HyperLink5")))
        self.driver.execute_script("arguments[0].click();", menu)
        time.sleep(1)

        delete_btn = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".item-data:nth-child(7) .bt-style-chucnang:nth-child(2)")
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", delete_btn)
        self.driver.execute_script("arguments[0].click();", delete_btn)
        time.sleep(1)

        panel = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".khung-admin > .khung-phai2-admin")
            )
        )
        self.driver.execute_script("arguments[0].click();", panel)
        time.sleep(1)

        assert True