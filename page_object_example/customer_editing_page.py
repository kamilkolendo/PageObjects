from page_object_example.base_page import BasePage


class CustomerEditingPage(BasePage):

    @property
    def customer_name_text_field(self):
        return self.driver.find_element_by_name('name')

    @property
    def male_gender_radio(self):
        return self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]')

    @property
    def female_gender_radio(self):
        return self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]')

    @property
    def date_of_birth_text_field(self):
        return self.driver.find_element_by_name('dob')

    @property
    def address_text_field(self):
        return self.driver.find_element_by_name('addr')

    @property
    def city_text_field(self):
        return self.driver.find_element_by_name('city')

    @property
    def state_text_field(self):
        return self.driver.find_element_by_name('state')

    @property
    def pin_text_field(self):
        return self.driver.find_element_by_name('pinno')

    @property
    def telephone_text_field(self):
        return self.driver.find_element_by_name('telephoneno')

    @property
    def email_text_field(self):
        return self.driver.find_element_by_name('emailid')

    @property
    def password_text_field(self):
        return self.driver.find_element_by_name('password')

    @property
    def submit_button(self):
        return self.driver.find_element_by_name('sub')

    @property
    def reset_button(self):
        return self.driver.find_element_by_name('reset')

    def open(self):
        self.driver.find_element_by_xpath('.//a[@href="addcustomerpage.php"]').click()

    def edit_city(self, data, click_submit=True, click_reset=False):
        if 'city' in data.keys():
            self.city_text_field.clear()
            self.city_text_field.send_keys(data['city'])

        if click_submit:
            self.submit_button.click()
        elif click_reset:
            self.reset_button.click()
