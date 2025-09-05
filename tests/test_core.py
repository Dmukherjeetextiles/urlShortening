import pytest
from app.core import shorten_url

def test_shorten_url_success():
    """
    Tests successful URL shortening.
    """
    long_url = "https://www.google.com"
    short_url = shorten_url(long_url)
    assert short_url.startswith("https://tinyurl.com/")

def test_shorten_url_empty():
    """
    Tests behavior with an empty URL.
    """
    with pytest.raises(ValueError):
        shorten_url("")

def test_shorten_url_invalid():
    """
    Tests behavior with an invalid URL.
    """
    # pyshorteners might not raise an exception for invalid-looking URLs,
    # it depends on the service. This test may need adjustment.
    long_url = "not a valid url"
    # This might raise a ConnectionError or other exception depending on the service
    with pytest.raises(Exception):
        shorten_url(long_url)

