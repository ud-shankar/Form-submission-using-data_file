##
# **Automate form submission using test data in yaml file**

The Test Automation Framework is created for automating all the Sanity, Smoke and Regression test cases.

### Scripting Language

Python is used as the scripting language. 
Selenium Webdriver is used to perform browser automation. The front end automation is achieved by implementing pytest test cases using webdriver based automation.

### Folder Structure

The Test Automation Suite is having below folders.

- **Features** : Feature files have been created based on each feature which is under test. The different scenarios and corresponding steps in each test case that is linked to the particular feature have been listed in the same feature file.
- **Source** : Source folder has been used to list the modules used to implement the source files for corresponding feature files steps. Emphasis has been kept to reuse the codes wherever possible using file level methods. In addition, this folder also contains util files which are used to describe some common actions as email access, being used across multiple files.
- **Pages** : This folder has been used to save the locators for each page in case of Front End Automation. Each file corresponds to each page in the UI and contains classes which groups the locators in each subsection or action.
- **Drivers** : Folder used to save driver details, docker configuration etc. used to link selenium to the corresponding browser driver.

### Creation of a test case

The following steps briefly describe how a new test case can be added to the framework.

1. Create a feature file, if required. Add the scenario and steps in the .feature file in Gherkin format.
2. Map the required page locators to the corresponding page class in the Pages folder. Do create a new page file in .py format if required.
3. Add the test cases scripts in the corresponding file in the Source folder. Do create a new script file if required. The steps and classes which are already implemented may be reused to reduce duplicate scripting.

### Test data file

Test_data.yaml files is used to store all kinds of test data.

datafile.py file is used to access the sample test data stored in yaml file and randomly pick data using random function in Python.
Object of test_data class in created in our test case and used to access the sample data for form filling.
