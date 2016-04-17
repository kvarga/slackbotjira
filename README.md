## Synopsis

A [slackbot](https://github.com/lins05/slackbot) plugin that queries the JIRA API for information about a ticket when mentioned in a channel.

## Installation

1. Setup [slackbot](https://github.com/lins05/slackbot)
2. `pip install slackbotjira`
3. In slackbot_settings.py:
  * Add 'slackbotjira' to PLUGINS list
  * `import os` to use environment variables for JIRA user/pass
  * Configure Python Variables in slackbot_settings.py
    * JIRA_URL = '{JIRA URL}'
    * JIRA_AUTH = (os.environ['JIRA_USER'], os.environ['JIRA_PASS'])
    * JIRA_PROJECTS = ['SPT']  # JIRA Project Keys
4. Configure Environment Variables for Authorization
  * JIRA_USER
  * JIRA_PASS
 
## Contributors

[kvarga](https://github.com/kvarga)

## License

The MIT License (see [LICENSE](LICENSE))
