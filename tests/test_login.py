
from config import BASE_URL,username,password
from pages.loginPage import LoginPage
from playwright.sync_api import expect
        
class TestLoginPageUI:
    def test_title_visible(self,loginPage:LoginPage):
        loginPage.assert_title()
        
    def test_logo_visible(self,loginPage:LoginPage):
        loginPage.assert_logo()
        
    def test_username_field_visible(self,loginPage:LoginPage):
        expect(loginPage.username_field).to_be_visible()
    
    def test_passowrd_field_visible(self,loginPage:LoginPage):
        expect(loginPage.password_field).to_be_visible()
        
    def test_forgot_password_link_visible(self,loginPage:LoginPage):
        expect(loginPage.forgot_password).to_be_visible()
        
class TestLoginFucntionality:
    def test_success_login(self,loginPage:LoginPage):
        loginPage.enter_username(username)
        loginPage.enter_password(password)
        loginPage.login()
        
    def test_login_with_wrong_credentials(self,loginPage:LoginPage,wrong_credentials):
        loginPage.enter_username(wrong_credentials["username"])
        loginPage.enter_password(wrong_credentials["password"])
        loginPage.login()
        loginPage.invalid_message.wait_for(state="visible")
        
    def test_login_without_username(self,loginPage:LoginPage,wrong_credentials):
        loginPage.enter_password(wrong_credentials["password"])
        loginPage.login()
        loginPage.assert_required_message()
        
    def test_login_without_password(self,loginPage:LoginPage,wrong_credentials):
        loginPage.enter_username(wrong_credentials["username"])
        loginPage.login()
        loginPage.assert_required_message()
        
    def test_login_with_wrong_username(self,loginPage:LoginPage,wrong_credentials):
        loginPage.enter_username(wrong_credentials["username"])
        loginPage.enter_password(password)
        loginPage.login()
        loginPage.invalid_message.wait_for(state="visible")
        
    def test_login_with_wrong_password(self,loginPage:LoginPage,wrong_credentials):
        loginPage.enter_username(username)
        loginPage.enter_password(wrong_credentials["password"])
        loginPage.login()
        loginPage.invalid_message.wait_for(state="visible")

    