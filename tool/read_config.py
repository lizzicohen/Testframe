import configparser
import os

from tool.log import Log


class ReadConfig:
    config = configparser.ConfigParser()
    config_path = os.path.abspath(os.path.dirname(os.getcwd())) + os.sep + 'config' + os.sep + 'config.ini'

    def __init__(self):
        log = Log()
        if not os.path.exists(self.config_path):
            print("config not found")
        else:
            print("config found")

    def read(self,sectionname, keyname):
        self.config.read(self.config_path)
        key = self.config.get(sectionname, keyname)
        return key

if __name__ == '__main__':
    rc = ReadConfig()
    print(rc.read("log_dir_name"))