from page_object_example.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class DeleteCustomerPage(BasePage):

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
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, './/a[@href="DeleteCustomerInput.php"]' )))
        self.driver.find_element_by_xpath('.//a[@href="DeleteCustomerInput.php"]').click()

    def delete_customer(self, id, click_submit=True, click_reset=False):
        self.customer_id_text_field.send_keys(id)

        if click_submit:
            self.submit_button.click()
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            self.driver.switch_to_alert().accept()
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            info_alert = self.driver.switch_to_alert()
            alert_text = info_alert.text
            info_alert.accept()
            return alert_text

        elif click_reset:
            self.reset_button.click()
