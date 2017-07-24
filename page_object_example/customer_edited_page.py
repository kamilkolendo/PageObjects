from page_object_example.base_page import BasePage


class CustomerEditedSucessfullyPage(BasePage):

    @property
    def header_field(self):
        return self.driver.find_element_by_class_name('heading3')

    @property
    def customer_city_field(self):
        return self.driver.find_element_by_xpath('//*[@id="customer"]/tbody/tr[9]/td[2]')

    def get_header_text(self):
        return self.header_field.text

    def get_customer_city(self):
        return self.customer_city_field.text

