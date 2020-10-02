class form_locators():
    first_name = 'firstName'  #id
    last_name = "lastName"
    email = "userEmail"
    mobile_number = "userNumber"
    hobbies = "//input[@id='hobbies-checkbox-{}']"  #xpath with {} to change the number for checkbox input
    gender = "//input[@id='gender-radio-{}']"       #xpath with {} to change the number for radio input
    Subject = "//div[@id='subjectsContainer']//div[1]//div[1]"
    current_address = "currentAddress"
    state = "state"
    state_list = "react-select-3-option-{}"
    city = "city"
    city_list = "react-select-4-option-{}"
    submit = "submit"
    close = "closeLargeModal"

    
