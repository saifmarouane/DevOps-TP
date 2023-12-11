from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

class ReadEmployeeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_read_employee(self):
        # Get an existing employee ID
        employee_id = 1  # Assuming an employee exists with this ID

        # Open the read page with the ID
        self.driver.get(f"http://localhost:8080/read.php?id={employee_id}")

        # Verify employee details are displayed
        name_field = self.driver.find_element(By.CSS_SELECTOR, "p.form-control-static:nth-child(2)")
        address_field = self.driver.find_element(By.CSS_SELECTOR, "p.form-control-static:nth-child(4)")
        salary_field = self.driver.find_element(By.CSS_SELECTOR, "p.form-control-static:nth-child(6)")

        # Use assertions to verify expected data
        self.assertEqual(name_field.text, "John Doe")  # assuming John Doe is the employee with given ID
        self.assertEqual(address_field.text, "123 Main Street")
        self.assertEqual(salary_field.text, "$50,000")

        # Verify back button functionality
        back_button = self.driver.find_element(By.CSS_SELECTOR, "a.btn-primary")
        back_button.click()

        # Verify redirection to index page
        self.assertEqual(self.driver.current_url, "http://localhost:8080/index.php")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
