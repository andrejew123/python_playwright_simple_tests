class LoginPage:
    def __init__(self, page):
        self.page = page
        self.search_term_input = page.locator('[aria-label="Enter your search term"]')
        self.login_input = page.locator("#login_id")
        self.next_button = page.get_by_role("button", name="dalej")
        self.password_input = page.locator("#login_password")
        self.login_button = page.get_by_role("button", name="zaloguj się")
        self.user_name = page.locator("#user_name")
        self.error_message = page.locator('#error_login_id')

    def navigate(self):
        self.page.goto("https://demobank.jaktestowac.pl")

    def fill_login_input(self, text):
        self.login_input.fill(text)
        self.login_input.blur()

    def fill_password_input(self, text):
        self.password_input.click()
        self.password_input.fill(text)
        self.password_input.blur()
        self.login_button.click()

    def search(self, text):
        self.search_term_input.fill(text)
        self.search_term_input.press("Enter")