from selenium.webdriver.common.by import By
def get_captcha(driver, element, path):
    captcha_p = driver.find_element(By.ID,element)
    captcha_p.screenshot(path)  
