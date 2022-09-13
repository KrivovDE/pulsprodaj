from client import get_post


def test_get_post(requests_mock, positive_data_post):
    requests_mock.get('http://test.com/1', text=positive_data_post)
    assert get_post('http://test.com', 1)
