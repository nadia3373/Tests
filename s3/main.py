from tests.main_hw import MainHWTest
from tests.user import UserTest


if __name__ == "__main__":
    from unittest import TestLoader, TextTestRunner

    loader = TestLoader()
    user_tests = loader.loadTestsFromTestCase(UserTest)
    main_hw_tests = loader.loadTestsFromTestCase(MainHWTest)

    suite = loader.loadTestsFromModule(__name__)

    suite.addTests(user_tests)
    suite.addTests(main_hw_tests)

    runner = TextTestRunner()
    result = runner.run(suite)

    exit(0 if result.wasSuccessful() else 1)
