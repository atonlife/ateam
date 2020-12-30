
from argparse import ArgumentParser
from logging import info



class CLI:

    def __init__(self, cli = []) -> None:
        self.parser = ArgumentParser(description='Report builder')

        self.subparsers = self.parser.add_subparsers(
            title='commands',
            dest='subparser_name',
        )

        for command in cli:
            self._add(command)


    def _add(self, command):
        ''' command:
             - name
             - help
             - aliases
             - func
             - option:
                - name
                - help
                - default
        '''

        command_parser = self.subparsers.add_parser(command['name'],
            help=command['help'],
            aliases=command['aliases'],
        )

        for option in command['option']:
            command_parser.add_argument(option['name'],
                help=option['help'],
                action=option.get('action', 'store'),
                default=option.get('default', None),
            )

        command_parser.set_defaults(func=command['func'])


    def parse(self):
        info('CLI parse')

        args = self.parser.parse_args()
        args.func(args)
