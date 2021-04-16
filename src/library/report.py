
from logging import debug, info

from adapter.jira.api import JiraAPI



class Report:

    def __init__(self, jira: JiraAPI, general: dict) -> None:
        self.jira = jira
        self.jira.set_general(general)


    def get_metrics(self, team: dict, period: dict) -> dict:
        metrics = dict(
            summary_time_count = 0,
            summary_estimate_count = 0,
        )

        info('Calculate metrics for "{}" team'.format(team.get('name')))

        members = team.get('members', [])
        user_members = [member.get('user') for member in members]
        worklog_members = [member.get('worklog') for member in members]

        issues = self.jira.get_complete_issues(user_members, period)

        for issue in issues:
            fields = issue.get('fields')
            assert fields.get('timeoriginalestimate')
            metrics['summary_estimate_count'] += fields.get('timeoriginalestimate')

            metrics['summary_time_count'] += self.jira.get_issue_worklog(worklog_members, period, issue)

        debug('Calculated team metrics')
        return metrics
