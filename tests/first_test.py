from page_object_example.login_page import LoginPage
from page_object_example.main_page import MainPage
from page_object_example.new_customer_page import NewCustomerPage
from page_object_example.delete_customer_page import DeleteCustomerPage
from page_object_example.edit_customer_page import EditCustomerPage
from page_object_example.customer_edited_page import CustomerEditedSucessfullyPage
from page_object_example.customer_editing_page import CustomerEditingPage
from page_object_example.customer_registered_page import CustomerRegisteredSucessfullyPage
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Ie
import random, string

driver = None
# to be filled in
manager_username = 'mngr88946'
manager_password = 'zurujAz'
new_customer_id = ' '


def setup_module(module):
    global driver
    caps = DesiredCapabilities.INTERNETEXPLORER
    caps['nativeEvents'] = False
    driver = Ie(capabilities=caps)
    driver.get('demo.guru99.com/V4/')


def test_login():
    login_page = LoginPage(driver)
    login_page.login_user(username=manager_username, password=manager_password)
    main_page = MainPage(driver)
    assert manager_username in main_page.manager_id_label.text


def test_new_customer():
    random_mail = ''.join(random.choice(string.ascii_lowercase) for i in range(5));
    mail = random_mail + '@java.com'

    data = {'customer_name': 'Krystian',
            'date_of_birth': '23/07/1993',
            'adress': 'Heheszki 247',
            'city': 'Gdansk',
            'state': 'Peaceful',
            'pin': '420420',
            'telephone': '420420420',
            'email': mail,
            'password': 'Kartofelek1',
            'gender': 'male'}

    new_customer_page = NewCustomerPage(driver)
    new_customer_page.open()
    new_customer_page.add_new_customer(data)

    customer_registered_page = CustomerRegisteredSucessfullyPage(driver)

    assert customer_registered_page.get_header_text() == "Customer Registered Successfully!!!"

    global new_customer_id
    new_customer_id = customer_registered_page.get_customer_id()

def test_edit_customer():
    data = {'city': 'Olsztyn'}

    edit_customer_page = EditCustomerPage(driver)
    edit_customer_page.open()
    edit_customer_page.edit_customer(new_customer_id)

    customer_editing_page = CustomerEditingPage(driver)
    customer_editing_page.edit_city(data)

    customer_edited_page = CustomerEditedSucessfullyPage(driver)

    assert customer_edited_page.get_customer_city() == data['city']

    assert customer_edited_page.get_header_text() == "Customer details updated Successfully!!!"

def test_delete_customer():
    delete_customer_page = DeleteCustomerPage(driver)

    delete_customer_page.open()
    delete_customer_page.delete_customer(new_customer_id)

    delete_customer_page.open()
    alert_msg = delete_customer_page.delete_customer(new_customer_id)

    assert alert_msg == "Customer does not exist!!"

def teardown_module(module):
    global driver
    # driver.quit()
    driver = None
