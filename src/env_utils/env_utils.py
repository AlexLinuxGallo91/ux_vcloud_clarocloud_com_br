import os
from dotenv import load_dotenv

class EnvUtils:

    @staticmethod
    def get_env_value(variable: str, default=''):
        load_dotenv()
        result = os.getenv(variable, default)

        if result is None:
            result = ''

        return result
