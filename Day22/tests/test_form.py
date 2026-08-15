from pages.form_page import FormPage


def test_form(driver):

    driver.get(
        "https://demoqa.com/automation-practice-form"
    )

    form = FormPage(driver)

    form.enter_first_name("Deepti")
    form.enter_last_name("Patel")
    form.enter_email("deepti@test.com")
    form.enter_mobile("9876543210")
    form.enter_address("Hyderabad, India")

    assert driver.current_url == \
        "https://demoqa.com/automation-practice-form"
