from configparser import ConfigParser


class Config:
    """ Game Config """
    
    def __init__(self, config_file: str = 'config.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)
        self.game = self.config['game']
        self.TITLE = self.game['TITLE']
        self.ICON = self.game['ICON']
        self.settings = self.config['settings']
        self.WIDTH = int(self.settings['WIDTH'])
        self.HEIGHT = int(self.settings['HEIGHT'])
        self.FPS = int(self.settings['FPS'])