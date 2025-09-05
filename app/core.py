import pyshorteners

def shorten_url(long_url: str) -> str:
    """
    Shortens a single URL using the TinyURL service.

    Args:
        long_url: The URL to shorten.

    Returns:
        The shortened URL.
    """
    if not long_url:
        raise ValueError("URL cannot be empty.")
    try:
        shortener = pyshorteners.Shortener()
        return shortener.tinyurl.short(long_url)
    except Exception as e:
        raise ConnectionError(f"Failed to shorten URL: {e}") from e