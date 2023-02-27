from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys


class Test_Todo:
    driver = webdriver.Chrome()
    url = "http://todomvc.com/examples/angularjs/#/"
    driver.get(url)
    # enter_to_do_1 = "python"
    # enter_to_do_2 = "pytest"
    # enter_to_do_3 = "Selenium"
    # enter_to_do_4 = "jenkins"
    # list = [enter_to_do_1,enter_to_do_2,enter_to_do_3,enter_to_do_4]

    driver.implicitly_wait(5)

    def test_add_todo(self):

        input_first_to_do_element = self.driver.find_element(By.CSS_SELECTOR, ".todo-form>input")
        input_first_to_do_element.send_keys("python", Keys.ENTER)
        input_second_to_do_element = self.driver.find_element(By.CSS_SELECTOR, ".todo-form>input")
        input_second_to_do_element.send_keys("pytest", Keys.ENTER)
        input_third_to_do_element = self.driver.find_element(By.CSS_SELECTOR, ".todo-form>input")
        input_third_to_do_element.send_keys("Selenium", Keys.ENTER)
        input_fourth_to_do_element = self.driver.find_element(By.CSS_SELECTOR, ".todo-form>input")
        input_fourth_to_do_element.send_keys("Jenkins", Keys.ENTER)
        check_to_do_list = self.driver.find_elements(By.XPATH, "//div[@class='view']/label")

        expected_to_do_list = ["python", "pytest", "Selenium", "Jenkins"]

        actual_to_do_list = []

        for i in check_to_do_list:
            if i.text in expected_to_do_list:
                actual_to_do_list.append(i.text)

        assert expected_to_do_list == actual_to_do_list


    def test_mark_as_complete(self):
        input_first_to_do_element = self.driver.find_element(By.CSS_SELECTOR, ".todo-form>input")
        input_first_to_do_element.send_keys("python", Keys.ENTER)
        input_second_to_do_element = self.driver.find_element(By.CSS_SELECTOR, ".todo-form>input")
        input_second_to_do_element.send_keys("pytest", Keys.ENTER)
        input_third_to_do_element = self.driver.find_element(By.CSS_SELECTOR, ".todo-form>input")
        input_third_to_do_element.send_keys("Selenium", Keys.ENTER)
        input_fourth_to_do_element = self.driver.find_element(By.CSS_SELECTOR, ".todo-form>input")
        input_fourth_to_do_element.send_keys("Jenkins", Keys.ENTER)
        check_bok_to_be_clicked = self.driver.find_element(By.XPATH, "//label[text()='python']/../input")
        check_bok_to_be_clicked.click()
        # check_todo_completed = self.driver.find_element(By.XPATH, "//label[text()='python']/../..")
        check_to_do_list = self.driver.find_elements(By.XPATH, "//li[@class = 'ng-scope completed']")
        if len(check_to_do_list) == 1:
            length = "True"
        to_do_counter = self.driver.find_element(By.XPATH, "//span[@class='todo-count']")

        assert to_do_counter.text == "3 items left"
        assert length == "True"


    def test_delete_to_do(self):
        input_first_to_do_element = self.driver.find_element(By.CSS_SELECTOR, ".todo-form>input")
        input_first_to_do_element.send_keys("python", Keys.ENTER)
        input_second_to_do_element = self.driver.find_element(By.CSS_SELECTOR, ".todo-form>input")
        input_second_to_do_element.send_keys("pytest", Keys.ENTER)
        input_third_to_do_element = self.driver.find_element(By.CSS_SELECTOR, ".todo-form>input")
        input_third_to_do_element.send_keys("Selenium", Keys.ENTER)
        input_fourth_to_do_element = self.driver.find_element(By.CSS_SELECTOR, ".todo-form>input")
        input_fourth_to_do_element.send_keys("Jenkins", Keys.ENTER)
        delete_button = self.driver.find_element(By.XPATH, "//label[text()='python']/following-sibling::button")
        self.driver.execute_script("arguments[0].click()", delete_button)
        check_to_do_list = self.driver.find_elements(By.XPATH, "//div[@class='view']/label")
        text_to_do_list = []

        for i in check_to_do_list:
            text_to_do_list.append(i.text)

        assert "python" not in text_to_do_list

    def test_filter_to_do(self):
        input_first_to_do_element = self.driver.find_element(By.CSS_SELECTOR, ".todo-form>input")
        input_first_to_do_element.send_keys("python", Keys.ENTER)
        input_second_to_do_element = self.driver.find_element(By.CSS_SELECTOR, ".todo-form>input")
        input_second_to_do_element.send_keys("pytest", Keys.ENTER)
        input_third_to_do_element = self.driver.find_element(By.CSS_SELECTOR, ".todo-form>input")
        input_third_to_do_element.send_keys("Selenium", Keys.ENTER)
        input_fourth_to_do_element = self.driver.find_element(By.CSS_SELECTOR, ".todo-form>input")
        input_fourth_to_do_element.send_keys("Jenkins", Keys.ENTER)
        check_bok_to_be_clicked = self.driver.find_element(By.XPATH, "//label[text()='python']/../input")
        check_bok_to_be_clicked.click()
        active_button = self.driver.find_element(By.LINK_TEXT, "Active")
        active_button.click()
        check_active_to_do_list = self.driver.find_elements(By.XPATH, "//div[@class='view']/label")
        active_list = []
        for i in check_active_to_do_list:
            active_list.append(i.text)

        completed_button = self.driver.find_element(By.XPATH, "//ul[@class='filters']/li/a[text()='Completed']")
        completed_button.click()

        check_completed_to_do_list = self.driver.find_elements(By.XPATH, "//div[@class='view']/label")
        completed_list = []
        for i in check_completed_to_do_list:
            completed_list.append(i.text)

        assert "python" not in active_list
        assert "python" in completed_list






