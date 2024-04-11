# urlShortening
Shortens the url; single or multiple(presented in a csv with "URL" column name.)


https://multiurlshortening.streamlit.app/


It provides the following features:

- Shorten a single URL by entering it in the input field.
- Upload a CSV file containing multiple URLs to shorten them in bulk.
- Download the updated CSV file with shortened URLs.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Dmukherjeetextiles/urlShortening.git
    ```

2. Navigate to the project directory:

    ```bash
    cd url-shortener-app
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run bitly.py
    ```

2. Open the provided URL in your web browser.

3. Use the input field to shorten a single URL or upload a CSV file containing multiple URLs.

4. Click the "Shorten" button to shorten the URL(s) and view the results.

5. If a CSV file was uploaded, you can download the updated CSV file with shortened URLs using the provided download button.

## File Structure

- `bitly.py`: The main Streamlit application script containing the app logic(I have a bad naming sense).
- `requirements.txt`: A list of Python dependencies required to run the app.
- `README.md`: This file provides information about the app.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Dmukherjeetextiles/urlShortening/blob/main/LICENSE) file for details.
