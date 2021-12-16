import pytest
from utilities import user
class TestUser():
    def setup_method(self):
        self.name = "safir"
        self.email = "afir@yahoo.com"
        self.password = "safir"
        self.user_data={
            "name":self.name,
            "email":self.email,
            "password":self.password
        }
    

    def test_registration_with_unique_email(self):
        unique = user.register(self.name,self.email,self.password)
        print(unique)
        assert unique == (1, "safir")


    def test_registration_with_non_unique_email(self):
        non_unique = user.register(self.name,self.email,self.password)
        assert non_unique is None


    def test_is_email_exists_with_unique_email(self):
        response = user.is_email_exists(self.email)
        print(response)
        assert response == (1,"safir")

    def test_is_email_exists_with_non_unique_email(self):
        response = user.is_email_exists(self.email)
        print(response)
        assert response is None
        
    def test_login_correct_email_correct_password(self):
        response = user.login(self.email,self.password)
        assert response == (1,"safir")

    
    def test_login_correct_email_incorrect_password(self):
        response = user.login(self.email,self.password)
        assert response is None

    
    def test_login_incorrect_email_correct_password(self):
        response = user.login(self.email,self.password)
        assert response is None


    def test_login_incorrect_email_incorrect_password(self):
        response = user.login(self.email,self.password)
        assert response is None
