from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from PageObjects.Homepage import Homepage
from PageObjects.checkoutpage import CheckOutpage
from PageObjects.confirmpage import ConfirmPage
from utilities.BaseClass import BaseClass
import time
import pytest

class TestOne(BaseClass):

    def test_e2e(self):
        log= self.getLogger()
        homepage= Homepage(self.driver) #actual driver
        checkoutpage=homepage.shopItems()
        #checkoutpage = CheckOutpage(self.driver)
        log.info('Getting all card titles')
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            card_text = card.text
            print(card_text)
            if card_text == 'Nokia Edge':
                checkoutpage.getCardFooter()[i].click()
        checkoutpage.getClickItem().click()
        confirmpage = checkoutpage.getclickCheckout()
        confirmpage.getDeliveryLocation().click()
        log.info('Entering country name as Ind')
        confirmpage.getDeliveryLocation().send_keys('ind')
        self.verifyLinkPresence("India")
        confirmpage.getClicklocation().click()
        confirmpage.getClickPurchase().click()
        gettext=confirmpage.getOrderConfirmText().text
        log.info('text received from application is '+ gettext)

