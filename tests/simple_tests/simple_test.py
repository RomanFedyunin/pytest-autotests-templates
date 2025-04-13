import allure


@allure.feature("Feature 1")
class TestTest:
    @allure.title("Title test 1")
    def test_test1(self):
        with allure.step("Step 1"):
            pass
        with allure.step("Step 2"):
            pass
        assert True

    @allure.title("Title test 2")
    def test_test2(self):
        with allure.step("Step 1"):
            pass
        with allure.step("Step 2"):
            pass
        assert False


@allure.feature("Feature 2")
class TestTest2:
    @allure.title("Title test 1")
    def test_test1(self):
        with allure.step("Step 1"):
            pass
        with allure.step("Step 2"):
            pass
        assert True

    @allure.title("Title test 2")
    def test_test2(self):
        with allure.step("Step 1"):
            pass
        with allure.step("Step 2"):
            pass
        assert False
