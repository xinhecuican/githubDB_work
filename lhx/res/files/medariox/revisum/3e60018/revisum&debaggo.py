
from github import Github

gh_username = 'medariox'
gh_password = 'comliebt92'

repo = Github(gh_username, gh_password).get_repo('psf/requests')
pulls = repo.get_pulls(state='all', sort='updated', direction='desc')


for pull in pulls:
    bu = pull
    print('haha')