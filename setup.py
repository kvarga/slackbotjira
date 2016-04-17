from setuptools import setup
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt', session=False)

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(name='slackbotjira',
      version='0.1',
      description='Slackbot JIRA Plugin',
      url='tbd',
      author='Kyle Varga',
      author_email='slackbot-jira@kylevarga.com',
      install_requires=reqs,
      license='MIT',
      packages=['slackbotjira'],
      zip_safe=False)