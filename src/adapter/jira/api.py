
from logging import debug, info

from .connect import Connect
from .cfg import JiraCFG



class JiraAPI:

    def __init__(self, cfg: JiraCFG) -> None:
        info('Jira init')

        self.connect = Connect(cfg)

    def get_issues(self, jql: str) -> list:
        return self.connect.search_issues(jql)

    def get_worklogs(self, issue_id: str) -> list:
        return self.connect.get_issue_worklogs(issue_id)
