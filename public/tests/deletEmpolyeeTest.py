from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

class DeleteEmployeeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_delete_employee(self):
        # Get an existing employee ID
        employee_id = 1  # Assuming an employee exists with this ID

        # Open the delete confirmation page with the ID
        self.driver.get(f"http://localhost/delete.php?id={employee_id}")

        # Confirm delete action
        yes_button = self.driver.find_element(By.CLASS_NAME, "btn-danger")
        yes_button.click()

        # Verify successful deletion message
        success_message = self.driver.find_element(By.CLASS_NAME, "alert-success")
        self.assertEqual(success_message.text, "Record deleted successfully!")

        # Verify employee absence on index page
        self.driver.get("http://localhost:8080/index.php")

        # Check if the employee row is present
        employee_rows = self.driver.find_elements_by_css_selector("tr.employee_row")
        found = False
        for row in employee_rows:
            cells = row.find_elements_by_tag_name("td")
            if cells[0].text == f"Employee {employee_id}":
                found = True
                break

        self.assertFalse(found)  # Employee should not be present

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
