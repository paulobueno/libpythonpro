from unittest.mock import Mock
import pytest
from libpythonpro import github_api


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars0.githubusercontent.com/u/24903100?v=4'
    resp_mock.json.return_value = {
        'login': 'paulobueno',
        'id': 24903100,
        'avatar_url': url
    }
    request_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = request_original


def test_avatar_seeker(avatar_url):
    url = github_api.avatar_seeker('paulobueno')
    assert avatar_url == url


def test_avatar_seeker_integration():
    url = github_api.avatar_seeker('paulobueno')
    assert 'https://avatars0.githubusercontent.com/u/24903100?v=4' == url