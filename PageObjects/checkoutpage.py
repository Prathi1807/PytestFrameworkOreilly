from selenium.webdriver.common.by import By
from PageObjects.confirmpage import ConfirmPage
class CheckOutpage:
    # Initializing driver instance so that we can assign testcase driver to local driver

    def __init__(self,driver):
        self.driver = driver
   #self.driver.find_elements(By.XPATH,"//h4[@class='card-title")
    cardTitles = (By.XPATH,"//h4[@class='card-title']")
    #self.driver.find_elements(By.XPATH, '//i[@class="zmdi zmdi-shopping-cart"]')[i].click()
    card_footer = (By.XPATH, '//i[@class="zmdi zmdi-shopping-cart"]')
    #self.driver.find_element(By.CSS_SELECTOR, 'a[class*="btn-primary"]').click()
    clickItem = (By.CSS_SELECTOR, 'a[class*="btn-primary"]')
    #self.driver.find_element(By.XPATH, '//button[@class="btn btn-success"]')
    clickCheckout = (By.XPATH, '//button[@class="btn btn-success"]')

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutpage.cardTitles)
    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutpage.card_footer)
    def getClickItem(self):
        return self.driver.find_element(*CheckOutpage.clickItem)
    def getclickCheckout(self):
        self.driver.find_element(*CheckOutpage.clickCheckout).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage




