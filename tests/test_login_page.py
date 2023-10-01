import pytest


@pytest.mark.regression
def test_incorrect_pass(login_page):
    login_page.open()
    login_page.fill_login_form(login='user@mail.com', passw='qwqwqwqw')
    assert login_page.error_text == (
        'The account sign-in was incorrect or your account is disabled temporarily. '
        'Please wait and try again later.'
    )
