from selenium.webdriver.common.by import By


# Initializing driver instance so that we can assign testcase driver to local driver

class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    #self.driver.find_element(By.XPATH, '//input[@id="country"]')

    deliveryLocation = (By.XPATH, '//input[@id="country"]')
    #self.driver.find_element(By.LINK_TEXT,"India"]').click()

    clickLocation = (By.LINK_TEXT,"India")

    #self.driver.find_element(By.XPATH, '//input[@value="Purchase"]')

    clickPurchase = (By.XPATH, '//input[@value="Purchase"]')

    orderConfirmedText = (By.XPATH,"//strong[text()='Success!']")

    def getDeliveryLocation(self):
        return self.driver.find_element(*ConfirmPage.deliveryLocation)

    def getClicklocation(self):
        return self.driver.find_element(*ConfirmPage.clickLocation)

    def getClickPurchase(self):

        return self.driver.find_element(*ConfirmPage.clickPurchase)

    def getOrderConfirmText(self):
        return self.driver.find_element(*ConfirmPage.orderConfirmedText)

