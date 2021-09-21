import unittest
from time import sleep
from appium import webdriver


class MyFirstTest(unittest.TestCase):
    """docstring for """

    def setUp(self):
        desiredCaps = {"deviceName": "emulator-5554", "platformName": "android", "appPackage": "com.ATG.World",
                       "appWaitDuration": "5000", "appExecTimeout": "50000", "uiautomator2ServerLaunchTimeout": "50000",
                       "uiautomator2ServerInstallTimeout": "50000",
                       "appActivity": "com.atg.world.activity.SplashActivity"}
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desiredCaps)

    def tearDown(self):
        self.driver.quit()

    def test_LoginWithRightCredential(self):
        self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
        sleep(1)
        self.driver.find_element_by_id("com.ATG.World:id/getStartedTv").click()
        sleep(1)
        self.driver.find_element_by_id("com.ATG.World:id/login_email").click()
        sleep(1)
        email = self.driver.find_element_by_id("com.ATG.World:id/email")
        email.send_keys("wiz_saurabh@rediffmail.com")
        password = self.driver.find_element_by_id("com.ATG.World:id/password")
        password.send_keys("Pass@123")
        signin = self.driver.find_element_by_id("com.ATG.World:id/email_sign_in_button")
        signin.click()
        sleep(1)
        print("test_LoginWithRightCredential passed")
        sleep(1)
        self.assertTrue(True)

    def test_PostingImageAfterLogin(self):
        self.test_LoginWithRightCredential()
        self.driver.find_element_by_id("com.ATG.World:id/btnGotit").click()
        sleep(1)
        self.driver.find_element_by_id("com.ATG.World:id/btnGotit").click()
        sleep(1)
        self.driver.find_element_by_id("com.ATG.World:id/fab").click()
        sleep(1)
        self.driver.find_element_by_id("com.ATG.World:id/image_fab_clicked").click()
        sleep(1)
        self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
        sleep(1)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]").click()
        sleep(1)
        self.driver.find_element_by_id("com.google.android.apps.photos:id/image").click()
        sleep(1)
        self.driver.find_element_by_accessibility_id("Photo taken on Sep 20, 2021 11:51:03 PM").click()
        sleep(1)
        self.driver.find_element_by_id("com.ATG.World:id/postCaption").send_keys("Testing123")
        sleep(1)
        self.driver.find_element_by_id("com.ATG.World:id/toolbar_post_action").click()
        sleep(1)
        print("test_PostingImageAfterLogin passed")
        sleep(1)
        self.assertTrue(True)