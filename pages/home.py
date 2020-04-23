import time, os, base64
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction

class Android_ATP_WTA(unittest.TestCase):
    
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['automationName'] = 'UiAutomator1'
        desired_caps['deviceName'] = '9d22273f'
        desired_caps['appPackage'] = 'com.android.chrome'
        desired_caps['appActivity'] = 'org.chromium.chrome.browser.document.ChromeLauncherActivity'
        desired_caps['useNewWDA'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
    
    def test_atp_wta(self):
        self.driver.start_recording_screen()
        accept_continue = self.driver.find_element_by_xpath("//*[contains(@resource-id,'com.android.chrome:id/terms_accept') and @text='Accept & continue']")
        accept_continue.click()
        next_button = self.driver.find_element_by_xpath("//*[contains(@resource-id,'com.android.chrome:id/next_button') and @text='Next']")
        next_button.click()
        positive_button = self.driver.find_element_by_xpath("//*[contains(@resource-id,'com.android.chrome:id/positive_button')]")
        positive_button.click()
        wait = WebDriverWait(self.driver, 30)
        search_url=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[contains(@resource-id,'com.android.chrome:id/search_box_text') and @text='Search or type web address']")))
        search_url.send_keys("https://sonataservices.com")
        show_link = wait.until(EC.element_to_be_clickable((By.XPATH,"//android.widget.TextView[@text='https://sonataservices.com']")))
        show_link.click()
        self.driver.implicitly_wait(5)
        accept_cookies = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='ACCEPT']")))
        accept_cookies.click()
        self.driver.implicitly_wait(5)
        action = TouchAction(self.driver)   
        action.press(x=0, y=1832).move_to(x=0, y=534).release().perform()
        self.driver.implicitly_wait(5) 
        el1 = self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[1]")
        el1.click()
        video_recording = self.driver.stop_recording_screen()
        video_file = self.driver.current_activity + time.strftime("%Y_%m_%d%H%M%S")
        filepath = os.path.join("/repository/python/appium",video_file+".mp4")
        with open(filepath,"wb") as vd:
            vd.write(base64.b64decode(video_recording))

#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_ATP_WTA)
    unittest.TextTestRunner(verbosity=2).run(suite)

