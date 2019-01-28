import ConfigParser


class Config(object):
    def add(self, name, section):
        setattr(self, name, section)


class Section(object):
    def __init__(self, values):
        for name, value in values:
            setattr(self, name, value)


if __name__ == '__main__':
    import os
    env = os.getenv("APP_ENV", "dev")
    print(env)
    config_parser = ConfigParser.ConfigParser()
    config_parser.read("config/dev.ini")

    config = Config()
    for section_name in config_parser.sections():
        section = Section(config_parser.items(section_name))
        config.add(section_name, section)
