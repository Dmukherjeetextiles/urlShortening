import pandas as pd
from app.core import shorten_url

def process_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Processes a DataFrame to shorten URLs in the 'URL' column.

    Args:
        df: The input DataFrame with a 'URL' column.

    Returns:
        The DataFrame with an added 'Shortened URL' column.
    """
    if 'URL' not in df.columns:
        raise ValueError("CSV file must contain a 'URL' column.")

    df['Shortened URL'] = df['URL'].apply(lambda url: shorten_url(url) if pd.notna(url) else '')
    return df