from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/")

# Wait for the username field to be visible and enter credentials
username_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "txtUsername")))
username_field.send_keys("Admin")

# Enter password
password_field = driver.find_element(By.ID, "txtPassword")
password_field.send_keys("admin123")

# Click login button
login_button = driver.find_element(By.ID, "btnLogin")
login_button.click()

# Wait for the PIM module link to be clickable and click on it
pim_module_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "menu_pim_viewPimModule")))
pim_module_link.click()

# Wait for the Add button to be clickable and click on it
add_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "btnAdd")))
add_button.click()

# Fill in employee details
first_name_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "firstName")))
first_name_field.send_keys("Sakila")

last_name_field = driver.find_element(By.ID, "lastName")
last_name_field.send_keys("Banu")

# You can fill in other personal details here...

# Click save button
save_button = driver.find_element(By.ID, "btnSave")
save_button.click()

# Wait for success message to appear
success_message = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='message success fadable']"))
)

# Verify if the success message is displayed correctly
assert "Successfully Saved" in success_message.text, "Employee addition failed!"

# Print success message if assertion passes
print("The new employee has been added successfully.")


# Close the WebDriver
driver.quit()
username_field = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.ID, "txtUsername"))
)