
from logging import debug, info

from adapter.jira.api import JiraAPI



class Report:

    def __init__(self, jira: JiraAPI) -> None:
        self.jira = jira


    def get_metrics(self, team: dict, period: dict) -> dict:
        debug('Calculate metrics for "{0}" team'.format(team.get('alias')))

        metrics = dir(
            summary_time_count = 0,
            summary_estimate_count = 0,
        )

        for member in team.get('members', []):
            issues = self.jira.get_complete_issues(member, period)

#TODO check issue.fields.timeoriginalestimate
            metrics['summary_estimate_count'] += issue.fields.timeoriginalestimate

            for issue in issues:
#TODO check issue.key
                worklog = self.jira.get_issue_worklog(issue.key, member, period)

                metrics['summary_time_count'] += worklog

        debug('Calculated team metrics')
        return metrics

