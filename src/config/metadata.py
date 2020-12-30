
from logging import info
from json import load

from .path import CfgPath



class MDTeams:

    def __init__(self, teams: dict) -> None:
        self.teams = teams
        self.teams_index = len(teams)


    def __iter__(self) -> None:
        return self


    def __next__(self) -> None:

        if self.teams_index == 0:
            raise StopIteration

        self.teams_index -= 1

        return self.teams[self.teams_index]



class CfgMetadata:

    def __init__(self, metadata_path: str) -> None:
        info('CFG Metadata init')

        cfg = CfgPath(metadata_path)

        with open(cfg.get_path()) as metadata_json:
            metadata = load(metadata_json)

        self.teams = MDTeams(metadata.get('teams'))


    def get_teams(self) -> MDTeams:
        return self.teams
