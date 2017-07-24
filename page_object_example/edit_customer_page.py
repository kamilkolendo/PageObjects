from page_object_example.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class EditCustomerPage(BasePage):

    @property
    def customer_id_text_field(self):
        return self.driver.find_element_by_name('cusid')

    @property
    def submit_button(self):
        return self.driver.find_element_by_name('AccSubmit')

    @property
    def reset_button(self):
        return self.driver.find_element_by_name('res')

    def open(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, './/a[@href="EditCustomer.php"]' )))
        self.driver.find_element_by_xpath('.//a[@href="EditCustomer.php"]').click()

    def edit_customer(self, id, click_submit=True, click_reset=False):
        self.customer_id_text_field.send_keys(id)

        if click_submit:
            self.submit_button.click()

        elif click_reset:
            self.reset_button.click()
