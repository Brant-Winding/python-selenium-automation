

class BasePage:

    def open(self):
        print('Opening base page')

    def click(self):
        print('Clicking')

    def verify_text(self):
        print('Verifying')

class LoginPage(BasePage):
    def login(self, username, password):
        print('Logging in')

#
# page = BasePage()
# page.click()
# page.verify_text


login_page = LoginPage()
# login_page.open()
# login_page.click()
# login_page.login('admin', 'admin')
login_page.verify_text()