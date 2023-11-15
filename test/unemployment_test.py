from app.unemployment import fetch_data


def test_fetch_data():
    data = fetch_data()
    assert len(data) > 100
    assert isinstance(data[0], dict)
    assert list(data[0].keys()) == ["date", "value"]