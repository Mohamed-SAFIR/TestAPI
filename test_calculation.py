import pytest
from utilities import user
from utilities import calculation
class TestCalculation():
    def setup_method(self):
        self.name = "safir mohamed"
        self.email = "safir.mohamed@gmail.com"
        self.password = "safirmohamed"
        self.user_data={
            "name":self.name,
            "email":self.email,
            "password":self.password
        }

    def test_get_user_history_empty_state(self):
        unique = user.register(self.name,self.email,self.password)
        assert unique == (2, "safir mohamed")
        login = user.login(self.email,self.password)
        assert login == (2, "safir mohamed")
        history = calculation.get_user_history(2)
        print(history)
        #assert history == []

    def test_get_user_history_non_empty_state(self):
        unique = user.register(self.name,self.email,self.password)
        assert unique == (2, "safir mohamed")
        login = user.login(self.email,self.password)
        assert login == (2, "safir mohamed")
        addCalculation = calculation.add_calculation(2,10,10)
        assert addCalculation == 1
        history = calculation.get_user_history(2)
        print(history)
        assert history != []

    def test_get_user_history_non_empty_state_bad_id(self):
        history = calculation.get_user_history(5)
        print(history)
        assert history == []

    def test_add_calculation(self):
        addCalculation = calculation.add_calculation(2,15,15)
        print(addCalculation)
        assert addCalculation == 1
