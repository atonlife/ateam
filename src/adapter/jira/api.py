
from logging import debug, info
from datetime import datetime, timedelta

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
            worklogDate >= {begin}
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

            #* 'started' is true, 'created' is false
            started = self._get_worklog_date(worklog.get('started'))
            if started < period.get('begin') or period.get('end') < started:
                continue

            total_worklog += worklog.get('timeSpentSeconds')

        return total_worklog

    def _get_worklog_date(self, timestamp: str) -> str:
        ''' exemple: '2021-01-26T07:20:00.000+0400'
        '''
        return timestamp.split('T', maxsplit=1)[0]
