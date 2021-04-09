
from logging import debug, info

from .connect import Connect
from .cfg import JiraCFG



class JiraAPI:

    def __init__(self, cfg: JiraCFG) -> None:
        info('Jira init')

        self.connect = Connect(cfg)


    def get_complete_issues(self, author: str, period: dir) -> list:
        return []
#TODO return list issues


    def _get_issues(self, jql: str) -> list:
        return self.connect.search_issues(jql)


    def get_issue_worklog(self, issue_id: str, author: str, period: dir) -> int:
        #worklogs = self.connect.get_issue_worklogs(issue_id)
        return []
#TODO return sum of issue worklogs by author in seconds
