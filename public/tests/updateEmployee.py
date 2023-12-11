from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

class UpdateEmployeeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_update_employee(self):
        # Get an existing employee ID
        employee_id = 1  # Assuming an employee exists with this ID

        # Open the update page with the ID
        self.driver.get(f"http://localhost:8080/update.php?id={employee_id}")

        # Update employee details
        name_field = self.driver.find_element(By.NAME, "name")
        name_field.clear()
        name_field.send_keys("John Smith")

        address_field = self.driver.find_element(By.NAME, "address")
        address_field.clear()
        address_field.send_keys("456 Elm Street")

        salary_field = self.driver.find_element(By.NAME, "salary")
        salary_field.clear()
        salary_field.send_keys("60000")

        # Submit the form
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        submit_button.click()

        # Verify successful update message
        success_message = self.driver.find_element(By.CLASS_NAME, "alert-success")
        self.assertEqual(success_message.text, "Record updated successfully!")

        # Verify updated data on index page
        self.driver.get("http://localhost:8080/index.php")

        # Get the updated employee row
        updated_row = self.driver.find_element_by_xpath(f"//*[@id='employee_table']/tbody/tr[@data-id='{employee_id}']")

        # Verify updated details
        cells = updated_row.find_elements_by_tag_name("td")
        self.assertEqual(cells[0].text, "John Smith")
        self.assertEqual(cells[1].text, "456 Elm Street")
        self.assertEqual(cells[2].text, "$60,000")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
