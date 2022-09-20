from selenium import webdriver
from src.env_utils.env_utils import EnvUtils


class WebDriverUtils:

    @staticmethod
    def generate_webdriver_chrome(path_webdriver):
        chrome_options = webdriver.ChromeOptions()
        chrome_capabilities = webdriver.DesiredCapabilities().CHROME.copy()

        if EnvUtils.get_env_value('HEADLESS').lower() in ('true', '1'):
            chrome_options.headless = True

        chrome_webdriver = webdriver.Chrome(executable_path=path_webdriver,
                                            desired_capabilities=chrome_capabilities,
                                            options=chrome_options)

        return chrome_webdriver

    @staticmethod
    def close_webdriver_chrome(web_driver_chrome: webdriver.Chrome):
        web_driver_chrome.close()
        web_driver_chrome.quit()
