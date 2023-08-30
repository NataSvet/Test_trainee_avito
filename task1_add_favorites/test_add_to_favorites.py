from .pages.card_of_product_page import CardOfProduct
from .pages.favorites_page import FavoritesPage


def test_add_to_favorites(browser):
    page = CardOfProduct(browser)
    link = 'https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363'
    page.open(link)
    page.add_favorites()
    page.check_change_text_added_favorites_button()
    assert page.get_text_notification() == "Добавлено в избранное", f'Уведомление об добавлении в избранное имеет другой текст{page.get_text_notification()}'
    card_of_product = page.get_info_card_of_product()

    page.go_to_section_favorites()
    page = FavoritesPage(browser)
    favorites_product_add =page.get_info_favorites()
    # Проверяем, объявление с таким названием добавлено в избранное
    assert card_of_product['name'] == favorites_product_add['name'], f'Название продукта не совпадает. Объявление - {card_of_product["name"]} - в избранном{favorites_product_add["name"]}'
    # Проверяем что объявление добавлено с верными данными
    assert card_of_product['adress'] == favorites_product_add['adress'], f'Адрес не совпадает. Объявление - {card_of_product["adress"]} - в избранном{favorites_product_add["adress"]}'
    assert card_of_product['time_publication'] == favorites_product_add['time_publication'], f'Время публикациии не совпадает. Объявление - {card_of_product["time_publication"]} - в избранном {favorites_product_add["time_publication"]}'
    assert card_of_product['product_category'] == favorites_product_add['product_category'], f'Указана неправильная категория. Объявление - {card_of_product["product_category"]} - в избранном {favorites_product_add["product_category"]}'
    assert card_of_product['price'] == favorites_product_add['price'], f'Указана неправильная стоимость. Объявление - {card_of_product["price"]} - в избранном {favorites_product_add["price"]}'
