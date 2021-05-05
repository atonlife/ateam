#!/usr/bin/env python3

from logging import DEBUG, basicConfig, debug, exception, info

from external.jira.api import JiraAPI
from external.cli import CLI
from business.logic.сomposite import BLComposite
from external.config.connect import CfgConnect
from external.config.metadata import CfgMetadata



class ATeam:
    ''' path:
        - connect
        - metadata
    '''

    def __init__(self, paths={}) -> None:
        connect_path = paths.get('connect', 'src/etc/connect.ini')
        metadata_path = paths.get('metadata', 'src/etc/metadata.json')

        try:
            self.connect = CfgConnect(connect_path)

            metadata = CfgMetadata(metadata_path)
            self.blc = BLComposite(metadata)
        except FileNotFoundError as path:
            exception("Cannot found '{0}'".format(path))


    def run(self) -> None:
        try:
            jira = JiraAPI(self.connect.get_jira())

            self.blc.set_adapters(dict(
                jira=jira,
            ))

            cli = CLI(self.blc.get_cli())
            cli.parse()
        except ConnectionError as server:
            exception("Cannot connection to '{0}'".format(server))



if __name__ == '__main__':
    basicConfig(
        filename='{}.log'.format(__name__),
        level=DEBUG,
        filemode='w',
        format='%(asctime)s\t[%(levelname)s]\t%(message)s',
    )

    debug('BEGIN')
    try:
        ateam = ATeam()
        ateam.run()
    except Exception as error:
        exception("Unexpected error: {0}".format(error))
    else:
        info('Successful')
        print('OK')
    finally:
        debug('END')
