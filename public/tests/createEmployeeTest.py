from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

class CreateEmployeeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_create_employee(self):
        # Open the create page
        self.driver.get("http://localhost:8080/index.php")

        # Enter employee details
        name_field = self.driver.find_element_by_id("name")
        name_field.send_keys("John Doe")

        address_field = self.driver.find_element_by_name("address")
        address_field.send_keys("123 Main Street")

        salary_field = self.driver.find_element_by_name("salary")
        salary_field.send_keys("50000")

        # Submit the form
        submit_button = self.driver.find_element_by_css_selector("input[type='submit']")
        submit_button.click()

        # Verify success message
        success_message = self.driver.find_element_by_class_name("success_message")
        self.assertEqual(success_message.text, "Employee added successfully!")

        # Verify employee data in index page
        self.driver.get("http://localhost:8080/index.php")

        # Get all employee rows
        rows = self.driver.find_elements_by_css_selector("tr.employee_row")

        # Find the row containing the new employee
        found = False
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            if cells[0].text == "John Doe":
                # Verify employee details
                self.assertEqual(cells[1].text, "123 Main Street")
                self.assertEqual(cells[2].text, "$50,000")
                found = True
                break

        self.assertTrue(found)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
