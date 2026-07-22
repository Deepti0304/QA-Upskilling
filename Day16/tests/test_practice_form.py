from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_practice_form():

    driver = webdriver.Chrome()

    try:
        driver.maximize_window()

        driver.get("https://demoqa.com/automation-practice-form")

        wait = WebDriverWait(driver, 10)

        # -----------------------------
        # First Name
        # -----------------------------

        first_name = wait.until(
            EC.visibility_of_element_located((By.ID, "firstName"))
        )

        assert first_name.is_displayed()
        assert first_name.is_enabled()

        first_name.send_keys("Deepti")

        assert first_name.get_attribute("value") == "Deepti"

        # -----------------------------
        # Last Name
        # -----------------------------

        last_name = driver.find_element(By.ID, "lastName")

        last_name.send_keys("Patel")

        assert last_name.get_attribute("value") == "Patel"

        # -----------------------------
        # Email
        # -----------------------------

        email = driver.find_element(By.ID, "userEmail")

        email.send_keys("deepti@test.com")

        assert email.get_attribute("value") == "deepti@test.com"

        # -----------------------------
        # Gender - Radio Button
        # -----------------------------

        gender = driver.find_element(
            By.XPATH,
            "//label[text()='Female']"
        )

        gender.click()

        # -----------------------------
        # Mobile Number
        # -----------------------------

        mobile = driver.find_element(By.ID, "userNumber")

        mobile.send_keys("9876543210")

        assert mobile.get_attribute("value") == "9876543210"

        # -----------------------------
        # Subject
        # -----------------------------

        subject = driver.find_element(By.ID, "subjectsInput")

        subject.send_keys("Maths")

        subject.send_keys("\n")

        # -----------------------------
        # Hobby Checkbox
        # -----------------------------

        # hobby = driver.find_element(By.XPATH, "//label[text()='Sports']")

        # hobby.click()
        # -----------------------------
# Hobby Checkbox - Sports
# -----------------------------

        hobby_checkbox = wait.until(
             EC.presence_of_element_located(
        (By.ID, "hobbies-checkbox-1")
    )
)

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", hobby_checkbox)

        if not hobby_checkbox.is_selected():
            driver.execute_script(
        "arguments[0].click();", hobby_checkbox)

        assert hobby_checkbox.is_selected()

        # -----------------------------
        # Current Address
        # -----------------------------

        address = driver.find_element(By.ID, "currentAddress")

        address.send_keys("Hyderabad, India")

        #assert address.get_dom_attribute("value") == "Hyderabad, India"

        # -----------------------------
        # Submit
        # -----------------------------

        submit = wait.until(
            EC.presence_of_element_located((By.ID, "submit")))

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",submit)

        submit = wait.until(EC.element_to_be_clickable((By.ID, "submit")))

        assert submit.is_displayed()
        assert submit.is_enabled()

        driver.execute_script("arguments[0].click();",submit)

        # -----------------------------
        # Confirmation
        # -----------------------------

        confirmation = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "example-modal-sizes-title-lg")
            )
        )

        assert confirmation.text == "Thanks for submitting the form"

    finally:
        driver.quit()