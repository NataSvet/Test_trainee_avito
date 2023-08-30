from selenium.webdriver.common.by import By

class CardOfProductLocators():
    BTN_ADD_FAVORITES = (By.CSS_SELECTOR, "div[class ='style-header-add-favorite-M7nA2'] button")
    BTN_ADDED_FAVORITES = (By.XPATH, "//button/span[contains(text(), 'В избранном')]")
    NOTIFICATION_LINK_IN_FAVORITES = (By.CSS_SELECTOR, "div[class ='desktop-1rs0evq'] a")
    NOTIFICATION_ADD_FAVORITES_TEXT = (By.CSS_SELECTOR, "div[class ='desktop-1rs0evq'] p")
    LINK_FAVORITE_HEADER = (By.CSS_SELECTOR, "a[title='Избранное']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "span[class='title-info-title-text']")
    PRODUCT_ADRESS = (By.CSS_SELECTOR, "span[class='style-item-address__string-wt61A']")
    PRODUCT_TIME_PUBLICATION = (By.CSS_SELECTOR, "span[data-marker='item-view/item-date']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "span[class ='styles-module-size_xxxl-A2qfi']:nth-child(1)")
    PRODUCT_CATEGORY = (By.CSS_SELECTOR, "span[class ='breadcrumbs-linkWrapper-jZP0j']:nth-child(3)")
    
    
class FavoritesLocators():
    PRODUCT_CARD = "//div/div/div[1]/div[contains(@class, 'styles-module-theme-scFBJ')]"
    PRODUCT_ADRESS = (By.XPATH, PRODUCT_CARD+"//span[@class='location-addressLine-igcGe']")
    PRODUCT_NAME = (By.XPATH, PRODUCT_CARD+"//div[@class='item-snippet-column-2-md2mY']/a/p/strong")
    PRODUCT_LINK = (By.XPATH, PRODUCT_CARD+"//div[@class='item-snippet-column-2-md2mY']/a")
    PRODUCT_PRICE = (By.XPATH, PRODUCT_CARD+"//div[@class='item-snippet-column-2-md2mY']//div[@class='price-line-root-NiZHp']")
    PRODUCT_TIME_PUBLICATION = (By.XPATH, PRODUCT_CARD+"//div[@class='item-snippet-column-2-md2mY']/p")
    PRODUCT_CATEGORY = (By.CSS_SELECTOR, "li:nth-child(2) button div[class ='category-content-content-biVWE'] span:nth-child(1)")



    

    

    
