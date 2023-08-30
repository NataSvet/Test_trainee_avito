from .base_page import BasePage
from .locators import CardOfProductLocators

class CardOfProduct(BasePage):
    locators_card_of_product_page = CardOfProductLocators()

    def get_info_card_of_product(self):
        info_card_of_product = {
        'name': self.presence_of_element_located(self.locators_card_of_product_page.PRODUCT_NAME).text,
        'adress': self.presence_of_element_located(self.locators_card_of_product_page.PRODUCT_ADRESS).text,
        'time_publication': (self.presence_of_element_located(self.locators_card_of_product_page.PRODUCT_TIME_PUBLICATION).text[2:]).replace(' в', ','),
        'product_category': self.presence_of_element_located(self.locators_card_of_product_page.PRODUCT_CATEGORY).text,
        'price': self.presence_of_element_located(self.locators_card_of_product_page.PRODUCT_PRICE).text
        }
        return info_card_of_product

    def add_favorites(self):
        self.element_is_clickable(self.locators_card_of_product_page.BTN_ADD_FAVORITES).click()

    def go_to_section_favorites(self):
        self.element_is_clickable(self.locators_card_of_product_page.LINK_FAVORITE_HEADER).click()
 
    def get_text_notification(self):
        return self.visibility_of_element_located(self.locators_card_of_product_page.NOTIFICATION_ADD_FAVORITES_TEXT).text
 
    def check_change_text_added_favorites_button(self):
        self.visibility_of_element_located(self.locators_card_of_product_page.BTN_ADDED_FAVORITES)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              


