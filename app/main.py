import streamlit as st
import pandas as pd
from app.core import shorten_url
from app.utils import process_csv

def main():
    """
    Main function to run the Streamlit application.
    """
    st.title("URL Shortener")

    # Option to upload a CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("Original DataFrame:")
            st.write(df)

            # Process the CSV to shorten URLs
            result_df = process_csv(df.copy())

            st.write("DataFrame with Shortened URLs:")
            st.write(result_df)

            # Download the DataFrame with shortened URLs as CSV
            csv = result_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Shortened URLs",
                data=csv,
                file_name="shortened_urls.csv",
                mime="text/csv",
            )
        except Exception as e:
            st.error(f"An error occurred: {e}")

    else:
        # Option to enter a single URL
        url = st.text_input("Enter URL to shorten:")
        if st.button("Shorten"):
            if url:
                with st.spinner('Shortening URL...'):
                    short_url = shorten_url(url)
                st.success("Shortened URL:")
                st.code(short_url, language='text')
            else:
                st.warning("Please enter a URL.")

if __name__ == "__main__":
    main()