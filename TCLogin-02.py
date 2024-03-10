from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/")

# Wait for the username field to be visible
username_field = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.ID, "txtUsername"))
)

# Find password and login button elements
password_field = driver.find_element(By.ID, "txtPassword")
login_button = driver.find_element(By.ID, "btnLogin")

# Enter username and invalid password
username_field.send_keys("Admin")
password_field.send_keys("Invalid password")

# Click login button
login_button.click()

# Wait for the error message to be displayed
error_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "spanMessage"))
)

# Verify if the error message is displayed correctly
expected_error_message = "Invalid credentials"
assert expected_error_message in error_message.text, f"Expected: '{expected_error_message}', Actual: '{error_message.text}'"

# Print success message if assertion passes
print("The error message for invalid credentials is displayed correctly.")

# Close the WebDriver
driver.quit()