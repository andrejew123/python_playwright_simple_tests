from playwright.sync_api import Page, expect

from pages.loginPage import LoginPage


def test_demobank_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()

    login_page.fill_login_input("12345678")
    login_page.next_button.click()
    login_page.fill_password_input("12345678")

    expect(login_page.user_name).to_have_text("Jan Demobankowy")


def test_demobank_login_id_too_short(page):
    login_page = LoginPage(page)
    login_page.navigate()

    login_page.fill_login_input("123")

    expect(login_page.error_message).to_have_text("identyfikator ma min. 8 znaków")
