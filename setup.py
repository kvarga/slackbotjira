from setuptools import setup

setup(name='slackbotjira',
      version='0.3',
      description='Slackbot JIRA Plugin',
      url='tbd',
      author='Kyle Varga',
      author_email='slackbot-jira@kylevarga.com',
      install_requires=[
        'jira',
      ],
      license='MIT',
      packages=['slackbotjira'],
      zip_safe=False)