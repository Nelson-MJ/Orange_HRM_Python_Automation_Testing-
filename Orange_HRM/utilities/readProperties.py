import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Orange_HRM\Configuration\config.ini")



class ReadConfig:

    @staticmethod
    def get_application_url():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def get_username():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password

    print("Config file path:", "./Configuration/config.ini")
    print("Sections:", config.sections())

