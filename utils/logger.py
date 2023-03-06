import datetime
import os


LOGS_PATH = "../logs/log_"
LOGS_EXT = ".log"


class Logger():
    file_name = LOGS_PATH + str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + LOGS_EXT

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_start_step(cls, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Тест: {test_name}\n"
        data_to_add += f"Время начала: {str(datetime.datetime.now())}\n"
        data_to_add += f"Название метода: {method}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_end_step(cls, url: str, method: str):

        data_to_add = f"Время конца: {str(datetime.datetime.now())}\n"
        data_to_add += f"Название метода: {method}\n"
        data_to_add += f"URL: {url}\n"
        data_to_add += f"-----\n"

        cls.write_log_to_file(data_to_add)