import requests
from requests.exceptions import ReadTimeout
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from requests.exceptions import ConnectionError

from src.timer_utils import var_results
from src.timer_utils.timer import Timer


class TaskEvalTimes:

    @staticmethod
    def verify_time_and_code_response_http(url_portal, timeout_portal=60):
        initial_time = Timer.get_current_time()

        try:
            r = requests.get(url=url_portal, timeout=timeout_portal)
            var_results.HTTP_STATUS_CODE = r.status_code
            var_results.HTTP_TIME_TOTAL_RESPONSE = round(r.elapsed.total_seconds(), 2)
        except ReadTimeout:
            var_results.HTTP_STATUS_CODE = 408
            var_results.HTTP_TIME_TOTAL_RESPONSE = Timer.get_total_time(initial_time, Timer.get_current_time())
        except ConnectionError:
            var_results.HTTP_STATUS_CODE = 502
            var_results.HTTP_TIME_TOTAL_RESPONSE = Timer.get_total_time(initial_time, Timer.get_current_time())

    @staticmethod
    def verify_time_render_portal(web_driver: webdriver.Chrome, url_portal: str, timeout_render: int = 60):
        initial_time = Timer.get_current_time()

        try:
            web_driver.set_page_load_timeout(timeout_render)
            web_driver.get(url_portal)
        except TimeoutException:
            var_results.RESULT_PORTAL_RENDERED_IS_CORRECT = False

        try:
            WebDriverWait(web_driver, 10).until(
                EC.presence_of_element_located((By.ID, "login_username")))
        except TimeoutException:
            var_results.RESULT_PORTAL_RENDERED_IS_CORRECT = False

        var_results.RESULT_PORTAL_RENDERED_IS_CORRECT = 1 if var_results.RESULT_PORTAL_RENDERED_IS_CORRECT else 0
        web_driver.set_page_load_timeout(60)
        var_results.TIME_TOTAL_RENDER_PORTAL = Timer.get_total_time(initial_time, Timer.get_current_time())

    @staticmethod
    def verify_time_render_portal_with_refresh(web_driver: webdriver.Chrome, url_portal: str,
                                               timeout_render: int = 60):
        initial_time = Timer.get_current_time()

        try:
            web_driver.set_page_load_timeout(10)
            web_driver.get(url_portal)
        except TimeoutException:
            try:
                web_driver.refresh()
            except TimeoutException:
                pass

        try:
            web_driver.set_page_load_timeout(timeout_render)
            web_driver.get(url_portal)
        except TimeoutException:
            var_results.RESULT_PORTAL_RENDERED_IS_CORRECT = False
        except WebDriverException:
            var_results.RESULT_PORTAL_RENDERED_IS_CORRECT = False

        try:
            WebDriverWait(web_driver, 10).until(
                EC.presence_of_element_located((By.ID, "login_username")))
        except TimeoutException:
            var_results.RESULT_PORTAL_RENDERED_IS_CORRECT = False

        var_results.RESULT_PORTAL_RENDERED_IS_CORRECT = 1 if var_results.RESULT_PORTAL_RENDERED_IS_CORRECT else 0
        web_driver.set_page_load_timeout(60)
        var_results.TIME_TOTAL_RENDER_PORTAL = Timer.get_total_time(initial_time, Timer.get_current_time())
