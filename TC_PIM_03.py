from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# Wait for username field to be visible and login
username_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "txtUsername")))
password_field = driver.find_element(By.ID, "txtPassword")
login_button = driver.find_element(By.ID, "btnLogin")

# Enter username and password
username_field.send_keys("Admin")
password_field.send_keys("admin123")
login_button.click()

# Wait for the page to load and click on the PIM module
pim_module = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "menu_pim_viewPimModule")))
pim_module.click()

# Locate the employee you want to delete and click on the delete button or checkbox
delete_checkbox = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox'][1]")))
delete_checkbox.click()

# Click on the delete button (assuming there's a delete button)
delete_button = driver.find_element(By.ID, "btnDelete")
delete_button.click()

# Handle confirmation dialog (if present)
confirm_delete_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "dialogDeleteBtn")))
confirm_delete_button.click()

# Verify deletion message
delete_success_message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='message success fadable']")))
assert "Successfully Deleted" in delete_success_message.text

# Close the WebDriver
driver.quit()