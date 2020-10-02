Feature: User Navigates into demoQA to fill sample form using test data file

    Scenario: User access test-data from yaml file to randomly access data and fill the form
        Given User opens DemoQA sample forms page
        When User enters first and last names
        And User enters mail id, mobile number and subject
        And User selects gender and hobbies
        And User enter address in textbox
        And User selects state and city from the dropdown list
        Then User clicks on submit button
