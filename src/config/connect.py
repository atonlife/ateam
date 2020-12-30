
from configparser import ConfigParser
from logging import info

from .path import CfgPath

from adapter.jira.cfg import JiraCFG



class CfgConnect:

    def __init__(self, connect_path: str) -> None:
        info('CFG Connect init')

        cfg = CfgPath(connect_path)

        self.connect = ConfigParser()
        self.connect.read(cfg.get_path())


    def get_jira(self) -> JiraCFG:
        return JiraCFG(self.connect['jira'])

