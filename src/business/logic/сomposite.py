
from logging import info

from external.config.metadata import CfgMetadata

from .metric import Metric



class BLComposite:
    ''' Business Logic Compositor: Input + Logic + Output
    '''

    def __init__(self, metadata: CfgMetadata) -> None:
        info('BLL init')

        self.logics = [
            Metric(metadata),
        ]


    def get_cli(self) -> list:
        return [ logic.get_cli() for logic in self.logics ]


    def set_adapters(self, adapters: dict) -> None:
        for logic in self.logics:
            logic.set_adapters(adapters)
