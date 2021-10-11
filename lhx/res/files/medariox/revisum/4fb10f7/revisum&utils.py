import os
from base64 import urlsafe_b64decode, urlsafe_b64encode
from pathlib import Path

from github import Github


gh_access_token = ''
gh_username = 'revisum-user'
gh_password = 'revisumtest123'


def get_project_root():
    """Returns project root folder."""
    return Path(__file__).parent


def gh_session():
    """Returns a PyGithub session."""
    if gh_access_token:
        return Github(gh_access_token)
    elif gh_username and gh_password:
        return Github(gh_username, gh_password)

    return Github()


def reverse_enum(f, start=None):
    start = start or 0
    fl = list(f)
    for i in reversed(range(len(fl))):
        yield i + start, fl[i]


def norm_path(file_path):
    path = file_path.replace(os.sep, '/')
    if path.startswith(('a/', 'b/')):
        return path[2:]
    if path.startswith('/'):
        return path[1:]

    return path


def b64_encode(string):
    encoded = urlsafe_b64encode(bytes(string, 'utf-8'))
    return encoded.decode('utf-8').rstrip('=')


def b64_decode(b64_hash):
    padding = 4 - (len(b64_hash) % 4)
    string = b64_hash + ('=' * padding)
    return urlsafe_b64decode(string).decode('utf-8')
