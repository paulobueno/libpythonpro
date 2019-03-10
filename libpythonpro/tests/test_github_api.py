from unittest.mock import Mock
import pytest
from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars0.githubusercontent.com/u/24903100?v=4'
    resp_mock.json.return_value = {
        'login': 'paulobueno',
        'id': 24903100,
        'avatar_url': url
    }
    get_mock=mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value=resp_mock
    return url


def test_avatar_seeker(avatar_url):
    url = github_api.avatar_seeker('paulobueno')
    assert avatar_url == url


def test_avatar_seeker_integration():
    url = github_api.avatar_seeker('renzon')
    assert 'https://avatars3.githubusercontent.com/u/3457115?v=4' == url