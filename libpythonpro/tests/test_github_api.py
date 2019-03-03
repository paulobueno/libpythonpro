from unittest.mock import Mock
from libpythonpro import github_api


def test_avatar_seeker():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'paulobueno',
        'id': 24903100,
        'avatar_url': 'https://avatars0.githubusercontent.com/u/24903100?v=4'
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.avatar_seeker('paulobueno')
    assert 'https://avatars0.githubusercontent.com/u/24903100?v=4' == url