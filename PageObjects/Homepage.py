from selenium.webdriver.common.by import By
from PageObjects.checkoutpage import CheckOutpage

class Homepage:
    # Initializing driver instance so that we can assign testcase driver to local driver

    def __init__(self,driver):
        self.driver=driver  #Local class driver

    shop = (By.XPATH ,'//a[contains(@href,"shop")]') #tuple
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*Homepage.shop).click()  # need to add * so this shop variable is considered as tuple
        checkoutpage = CheckOutpage(self.driver)
        return checkoutpage
    def getName(self):
       return self.driver.find_element(*Homepage.name)
    def getemail(self):
        return self.driver.find_element(*Homepage.email)

    def getCheckBox(self):
        return self.driver.find_element(*Homepage.check)

    def getGender(self):
        return self.driver.find_element(*Homepage.gender)

    def submitForm(self):
        return self.driver.find_element(*Homepage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*Homepage.successMessage)