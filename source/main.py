import ConfigParser


class Config(object):
    def add(self, name, section):
        setattr(self, name, section)


class Section(object):
    def __init__(self, values):
        for name, value in values:
            setattr(self, name, value)


class ConfigBuilder(object):
    def construct(self, file_path):
        raise NotImplementedError


class IniConfigBuilder(ConfigBuilder):
    def construct(self, file_path):
        config_parser = ConfigParser.ConfigParser()
        config_parser.read(file_path)
        config = Config()
        for section_name in config_parser.sections():
            section = Section(config_parser.items(section_name))
            config.add(section_name, section)

        return config

class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super(Singleton, cls).__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance

class ConfigSingleton(object):
    __metaclass__ = Singleton

    def set_config(self, config):
        self._config = config

    def get_config(self):
        return self._config

if __name__ == '__main__':
    import os
    env = os.getenv("APP_ENV", "dev")
    env_pointer = {
        'dev': "config/dev.ini",
        "prod": "config/prod.ini"
    }

    config = IniConfigBuilder().construct(env_pointer[env])

    s1 = ConfigSingleton()
    s1.set_config(None)
    print(s1.get_config())
    s2 = ConfigSingleton()
    s2.set_config(config)
    print(s2.get_config())