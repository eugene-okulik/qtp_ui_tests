import pytest


@pytest.mark.extended
def test_sale_title(sale_page):
    sale_page.open()
    assert sale_page.page_title_text == 'Sale'
