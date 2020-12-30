
from logging import debug
from requests import Response, codes, get, post

from .cfg import JiraCFG



class URL:

    def __init__(self, server) -> None:
        self.rest = server + '/rest/api/2/'


    def createmeta(self) -> str:
        return '{}issue/createmeta'.format(self.rest)


    def search(self) -> str:
        return '{}search'.format(self.rest)


    def worklog(self, issue_id) -> str:
        return '{}issue/{}/worklog'.format(self.rest, issue_id)



class Connect:

    def __init__(self, connect: JiraCFG) -> None:
        self.server = connect.server
        self.auth = (connect.user, connect.password)

        self.url = URL(self.server)

        self._check_connect()


    def _check_connect(self) -> None:
        self._send_get(self.url.createmeta())

        debug("Successful connect to '{}'".format(self.server))


    def _send_get(self, url: str) -> dict:
        responce = get(url, auth=self.auth)

        debug("Response status: '{}'".format(responce.status_code))

        return self._receive_result(responce)


    def _send_post(self, url: str, data: dict) -> dict:
        ''' POST request for search by JQL:
            - jql: <JQL>
            - startAt: <number>
            - maxResults: <number>
            - fields:
                - <string>
                - <string>
        '''
        responce = post(url, auth=self.auth, json=data)

        return self._receive_result(responce)


    def _receive_result(self, responce: Response) -> dict:

        if responce.status_code != codes.ok:
            raise ConnectionError(self.server)

        result = responce.json()

        total       = result.get('total', 0)
        max_results = result.get('maxResults', 0)
        if total > max_results:
            raise Exception("Total items '{}' more max result '{}'".format(total, max_results))

        return result


    def search_issues(self, jql: str) -> list:
        data = dict(
            jql=jql
        )

        try:
            result = self._send_post(self.url.search(), data)
        except ConnectionError:
            raise Exception("Connot get issues by JQL '{}'".format(jql))

        return result.get('issues')


    def get_issue_worklogs(self, issue_id: str) -> list:
        try:
            result = self._send_get(self.url.worklog(issue_id))
        except ConnectionError:
            raise Exception("Connot get issue worklogs by issue '{}'".format(issue_id))

        return result.get('worklogs')
