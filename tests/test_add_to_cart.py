import pytest


@pytest.mark.smoke
def test_e2e_add_to_cart(home_page, product_page, category_page):
    home_page.open()
    home_page.open_jackets_submenu()
    category_page.open_first_product()
    assert product_page.add_to_cart_button_is_enabled(), '"Add to cart" button is not enabled'
