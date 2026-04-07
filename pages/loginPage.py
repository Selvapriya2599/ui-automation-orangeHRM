from playwright.sync_api import Page, Locator, expect


class LoginPage:
    _title = "OrangeHRM"
    _logo = "img[alt='orangehrm-logo']"
    _forgot_password = "p.orangehrm-login-forgot-header"
    
    def __init__(self, page: Page):
        self.page = page
        self.loginButton = page.locator('button[type="submit"]')
        self.username_field = page.get_by_placeholder("Username")
        self.password_field = page.get_by_placeholder("Password")
        self.invalid_message = page.get_by_text("Invalid credentials")
        self.required_message = page.locator("span.oxd-input-field-error-message")
        self.logo = page.locator(self._logo).first
        self.forgot_password = page.locator(self._forgot_password)
        
    
    def enter_username(self,username:str):
        self.username_field.clear()
        self.username_field.fill(username)
        
    def enter_password(self,password:str):
        self.password_field.clear()
        self.password_field.fill(password)
        
    def login(self):
        self.loginButton.click()
    
    def assert_required_message(self):
        expect(self.required_message).to_have_text("Required")
        
    def assert_title(self):
        #expect(self.page).to_have_title(self.title)
        expect(self.page).to_have_title(self._title)
        
    def assert_logo(self):
        expect(self.logo).to_be_visible()
        expect(self.logo).to_have_attribute("src", "/web/images/ohrm_logo.png")
    