
from argparse import Namespace
from logging import info, debug

from config.metadata import CfgMetadata
from library.report import Report



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
                    name='begin',
                    help='Begin date of the calculation period (inclusive): <YYYY-MM-DD>',
                ),
                dict(
                    name='end',
                    help='End date of the calculation period (inclusive): <YYYY-MM-DD>',
                ),
            ],
            func=self._calculate,
        )


    def _calculate(self, args: Namespace) -> None:
        assert self.jira
        assert self.metadata

        period = dict(
            begin = args.begin,
            end = args.end,
        )
        report = Report(self.jira, self.metadata.get_general())

        info('Calculate team metrics for a period "{begin}" - "{end}"'.format(**period))

        for team in self.metadata.get_teams():
            print('{}:'.format(team.get('name')))

            metrics = report.get_metrics(team, period)
            for metric in sorted(metrics):
                #TODO: convert seconds to hours from time
                print('- {}: {:0.3f}'.format(metric, metrics.get(metric) / 3600.0))
