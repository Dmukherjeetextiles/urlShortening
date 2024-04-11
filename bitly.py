import streamlit as st
import pandas as pd
import pyshorteners

# Function to shorten a single URL
def shorten_url(long_url):
    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(long_url)
        return short_url
    except Exception as e:
        return "Error: " + str(e)

# Function to shorten URLs in a DataFrame
def shorten_urls_in_dataframe(df):
    df['Shortened URL'] = df['URL'].apply(shorten_url)
    return df

# Main function
def main():
    st.title("URL Shortener")

    # Option to upload a CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Original DataFrame:")
        st.write(df)

        # Shorten URLs in the DataFrame
        df = shorten_urls_in_dataframe(df)

        st.write("DataFrame with Shortened URLs:")
        st.write(df)

        # Download the DataFrame with shortened URLs as CSV
        csv = df.to_csv(index=False)
        st.download_button(label="Download Shortened URLs", data=csv, file_name="shortened_urls.csv", mime="text/csv")

    else:
        # Option to enter a single URL
        url = st.text_input("Enter URL to shorten:")
        if st.button("Shorten"):
            if url:
                short_url = shorten_url(url)
                st.write("Shortened URL:", short_url)
            else:
                st.write("Please enter a URL.")

if __name__ == "__main__":
    main()
