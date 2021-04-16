
from logging import debug, info

from .connect import Connect
from .cfg import JiraCFG



class JiraAPI:

    def __init__(self, cfg: JiraCFG) -> None:
        info('Jira init')
        self.connect = Connect(cfg)


    def set_general(self, general: dict) -> None:
        self.general = general


    def get_complete_issues(self, members: list, period: dict) -> list:
        authors = self._get_authors(members)

        info('Jira search complete issues for "{}"'.format(authors))

        #TODO include end date in filter (add day, conv_jira())
        jql = '''
            filter = "{filter}"
                AND
            worklogAuthor in ({authors})
                AND
            worklogDate >= {start}
                AND
            worklogDate <= {end}
        '''.format(
            filter=self.general.get('filter'),
            authors=authors,
            **period,
        )
        return self.connect.search_issues(jql)


    def _get_authors(self, members: list) -> str:
        return ', '.join(members)


    def get_issue_worklog(self, members: list, period: dict, issue: dict) -> int:
        total_worklog = 0

        for worklog in self.connect.get_issue_worklogs(issue.get('id')):
            if worklog.get('author').get('name') not in members:
                continue

            # Format exemple: 2018-05-16T10:52:00.000+0300
            started = worklog.get('started')
            if started < period.get('start') or period.get('end') < started:
                continue

            total_worklog += worklog.get('timeSpentSeconds')

        return total_worklog
