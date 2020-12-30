
from argparse import Namespace
from logging import info

from config.metadata import CfgMetadata



class Period:

    def __init__(self, start: str, end: str) -> None:
        self.start = start
        self.end = end



class Metric:

    def __init__(self, metadata: CfgMetadata):
        self.jira = None
        self.metadata = metadata


    def set_adapters(self, adapters: dict) -> None:
        self.jira = adapters.get('jira')


    def get_cli(self) -> dict:
        return dict(
            name='metric',
            help='Calculate a team metrics',
            aliases='m',
            option=[
                dict(
                    name='start',
                    help='Start date of the calculation period (inclusive): <YYYY-MM-DD>',
                ),
                dict(
                    name='end',
                    help='End date of the calculation period (inclusive): <YYYY-MM-DD>',
                ),
            ],
            func=self._calculate,
        )


    def _calculate(self, args: Namespace) -> None:
        info('Calculate metrics')
        assert self.jira
        assert self.metadata

        period = Period(args.start, args.end)

        for team in self.metadata.get_teams():
            #TODO add report with CLI date period by metadata
            pass

