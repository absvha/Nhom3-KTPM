from selenium.webdriver.common.action_chains import ActionChains
import time

def test_tc59(driver):
    driver.get('http://hauiproj.somee.com/Default.aspx')
    driver.set_window_size(1138, 850)
    from conftest import wait_click
    wait_click(driver, 'css=#HyperLink4 > li')
    from conftest import wait_find
    el = wait_find(driver, 'id=ContentPlaceHolder1_gvGioHang_Label1')
    assert el.text.strip() == 'Không có mặt hàng nào trong giỏ hàng!'
