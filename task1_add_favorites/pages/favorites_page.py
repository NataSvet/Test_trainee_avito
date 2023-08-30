from .base_page import BasePage
from .locators import FavoritesLocators

class FavoritesPage(BasePage):

    locators = FavoritesLocators()
    def get_info_favorites(self):
        info_favorites = {
            'name': self.presence_of_element_located(self.locators.PRODUCT_NAME).text,
            'adress': self.presence_of_element_located(self.locators.PRODUCT_ADRESS).text,
            'time_publication': self.presence_of_element_located(self.locators.PRODUCT_TIME_PUBLICATION).text,
            'product_category': self.presence_of_element_located(self.locators.PRODUCT_CATEGORY).text,
            'price': (self.presence_of_element_located(self.locators.PRODUCT_PRICE).text).replace(' ₽', '')
        }

        return info_favorites
        