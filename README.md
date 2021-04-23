# ateam
Calculate Team Metrics by Jira Statistics

* **[Dependence](#Dependence)**<br>
* **[Configuration](#Configuration)**<br>
* **[Using](#Using)**<br>


## Dependence
Only Python 3.7+ standart library


## Configuration

### connect.ini
```ini
[DEFAULT]

[jira]
server = <server>
user = <username>
password = <user password>
```

### metadata.json
```json
{
  "general": {
    "filter": "<general JQL filter for all teams>"
  },
  "teams": [
    {
      "name": "<name for show>",
      "members": [
        {
          "user": "<username for JQL>",
          "worklog":  "<worklog name in Jira DB>"
        }
      ]
    }
  ]
}
```
* Renaming username doesn't rename name in Jira Database

## Using
```shell
$ ateam --help
```

