from selenium.webdriver.common.action_chains import ActionChains
import time

def test_tc60(driver):
    driver.get('http://hauiproj.somee.com/Default.aspx')
    driver.set_window_size(1138, 850)
    from conftest import wait_click
    wait_click(driver, 'css=#HyperLink2 > li')
    from conftest import wait_click
    wait_click(driver, 'id=ContentPlaceHolder1_DataList1_Image1_0')
    from conftest import wait_click
    wait_click(driver, 'id=ContentPlaceHolder1_Datalist1_btnThemVaoGio_0')
    from conftest import wait_click
    wait_click(driver, 'css=.tieude-phai')
