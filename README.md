# ateam
Calculate Team Metrics by Jira Statistics

* **[Dependence](#Dependence)**<br>
* **[Configuration](#Configuration)**<br>
* **[Using](#Using)**<br>


## Dependence
Only Python 3.7 standart library


## Configuration

### connect.ini
```ini
[DEFAULT]

[jira]
server = <Server>
user = <Username>
password = <User Password>
```

### metadata.json
```json
{
  "members": [
    {
      "alias" : <name_for_show>,
      "user": <username_for_JQL>,
      "worklog":  <worklog_name_in_Jira_DB>
    }
  ],
  "teams": [
    {
      "alias": <alias_for_show>,
      "group": <group_name_for_JQL>,
      "members": [ <members.user>, ... ]
    }
  ]
}
```
* Renaming username doesn't rename name in Jira Database

## Using
```shell
$ ateam --help
```

