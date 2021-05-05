
from logging import debug, info, warning

from external.jira.api import JiraAPI



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
            timetracking = issue.get('fields').get('timetracking')
            assert timetracking

            estimate = timetracking.get('originalEstimateSeconds')
            if estimate == 0:
                warning(
                    'Issue without Original Estimate: "{key}"'.format(
                        key=issue.get('key')
                    )
                )
            metrics['summary_estimate_count'] += estimate

            issue_worklog = self.jira.get_issue_worklog(worklog_members, period, issue)
            metrics['summary_time_count'] += issue_worklog

        debug('Calculated team metrics')
        return metrics
