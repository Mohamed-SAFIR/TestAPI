import pytest
from werkzeug.wrappers import response
from app import app
def test_register_page_returns_correct_html():
    tester = app.test_client()
    response = tester.get('/register')
    assert response.status_code == 200
    assert b'Register User' in response.data  


def test_register_user_success():
    tester = app.test_client()
    response = tester.post('/register', data={"name":"mohamed","email":"tester@gmail.com","password":"mohamed"}, follow_redirects=True)
    assert response.status_code == 200
    

def test_register_user_bad_input():
    tester = app.test_client()
    response = tester.post('/login', follow_redirects=True)
    assert response.status_code == 400


def test_register_user_success():
    tester = app.test_client()
    response = tester.post('/register', data={"name":"mohamed","email":"tester@gmail.com","password":"mohamed"}, follow_redirects=True)
    assert response.status_code == 403
    

def test_login_user_success():
    tester = app.test_client()
    response = tester.post('/login',data={"email":"tester@gmail.com","password":"mohamed"},follow_redirects=True)
    assert response.status_code == 200
    assert b'Conversion Page' in response.data
    assert b'<form ' in response.data


def test_login_user_invalid_credentials():
    tester = app.test_client()
    response = tester.post('/login', data={"email":"tester@gmail.c","password":"moham"},follow_redirects=True)
    assert response.status_code == 403
    assert b'Invalid email or password' in response.data


def test_login_user_bad_data():
    tester = app.test_client()
    response = tester.post('/login', data={})
    assert response.status_code == 400
    assert b'Login User' in response.data
    assert b'<form ' in response.data


def test_home_without_login():
    tester = app.test_client()
    response = tester.get('/',follow_redirects=True)
    assert response.status_code == 200
    data = response.data.decode()
    assert data.find("Login User") != -1


def test_calculation_hex():
    tester = app.test_client()
    response = tester.post('/login',data={"email":"tester@gmail.com","password":"mohamed"},follow_redirects=True)
    response = tester.get('/')
    data = response.data.decode()
    assert data.find("Conversion Page") != -1
    response = tester.post('/',data={"base":"16","input":"A"})
    assert response.status_code == 200
    data = response.data.decode()
    assert data.find("Result") != -1


def test_calculation_dec():
    tester = app.test_client()
    response = tester.post('/login',data={"email":"tester@gmail.com","password":"mohamed"},follow_redirects=True)
    response = tester.get('/')
    data = response.data.decode()
    assert data.find("Conversion Page") != -1
    response = tester.post('/',data={"base":"10","input":"10"})
    assert response.status_code == 200
    data = response.data.decode()
    assert data.find("Result") != -1


def test_calculation_bin():
    tester = app.test_client()
    response = tester.post('/login',data={"email":"tester@gmail.com","password":"mohamed"},follow_redirects=True)
    response = tester.get('/')
    data = response.data.decode()
    assert data.find("Conversion Page") != -1
    response = tester.post('/',data={"base":"2","input":"1010"})
    assert response.status_code == 200
    data = response.data.decode()
    assert data.find("Result") != -1


def test_calculation_bad_data():
    tester = app.test_client()
    response = tester.post('/login',data={"email":"tester@gmail.com","password":"mohamed"},follow_redirects=True)
    response = tester.get('/')
    data = response.data.decode()
    assert data.find("Conversion Page") != -1
    response = tester.post('/',data={"base":"10","input":"10A"})
    assert response.status_code == 400

def test_history():
    tester = app.test_client()
    response = tester.post('/login',data={"email":"tester@gmail.com","password":"mohamed"},follow_redirects=True)
    response = tester.get('/')
    data = response.data.decode()
    assert data.find("Conversion Page") != -1
    response = tester.post('/',data={"base":"2","input":"1010"})
    response = tester.post('/',data={"base":"10","input":"10"})
    response = tester.post('/',data={"base":"16","input":"A"})
    assert response.status_code == 200
    response = tester.get('/dashboard')
    assert response.status_code == 200
    data = response.data.decode()
    assert data.find("A") != -1

