from pages.fun_9999_page import FunPage


def test_entering_russian_text_in_the_search_bar(fun_9999_page: FunPage):
    fun_9999_page.open_page()
    fun_9999_page.enter_cyrillic_text_in_the_search_bar()
    fun_9999_page.checking_the_input_result_in_cyrillic('No results')


def test_adding_a_negative_quantity_of_items_to_the_cart(fun_9999_page: FunPage):
    fun_9999_page.open_page()
    fun_9999_page.entering_a_negative_quantity()
    fun_9999_page.check_for_negative_item_quantities_in_the_cart('Your cart is empty!')


def test_adding_an_excessively_large_number_of_items_to_the_cart(fun_9999_page: FunPage):
    fun_9999_page.open_page()
    fun_9999_page.input_of_an_extremely_large_quantity()
    fun_9999_page.checking_for_an_excessively_large_quantity_in_the_cart()
