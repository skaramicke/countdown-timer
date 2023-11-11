import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestCountdownTimer(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")  # Run in headless mode
        options.add_experimental_option('w3c', False)  # To capture console log
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def test_countdown_timer_changes(self):
        base_url = "https://countdown-timer-5a6.pages.dev/"
        times = ["#2024-01-01+00:00", "#2024-01-02+00:00"]

        for time_fragment in times:
            self.driver.get(base_url + time_fragment)
            time.sleep(5)  # Wait for the countdown to update

            # Capture any JavaScript errors or warnings
            logs = self.driver.get_log('browser')
            for entry in logs:
                if entry['level'] in ['SEVERE', 'WARNING']:
                    self.fail(f"JavaScript error/warning: {entry['message']}")

            # Check if the countdown timer values are present
            days = self.driver.find_element(By.ID, "days").text
            self.assertNotEqual(days, '', "Days field is empty")

            # Additional checks for hours, minutes, and seconds can be added here

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
