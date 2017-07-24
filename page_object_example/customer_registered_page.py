from page_object_example.base_page import BasePage


class CustomerRegisteredSucessfullyPage(BasePage):

    @property
    def header_field(self):
        return self.driver.find_element_by_class_name('heading3')

    @property
    def customer_id_field(self):
        return self.driver.find_element_by_xpath('//*[@id="customer"]/tbody/tr[4]/td[2]')

    def get_header_text(self):
        return self.header_field.text

    def get_customer_id(self):
        return self.customer_id_field.text

