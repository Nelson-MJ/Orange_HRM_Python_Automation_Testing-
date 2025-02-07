import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        log_dir = "./Logs"
        log_file = os.path.join(log_dir, "automation.log")


        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logger = logging.getLogger("AutomationLogger")
        logger.setLevel(logging.INFO)


        logger.handlers.clear()


        file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s",
                                      datefmt="%m/%d/%Y %I:%M:%S %p")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger
