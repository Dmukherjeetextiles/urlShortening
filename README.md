# URL Shortener

A simple yet powerful URL shortener application built with Streamlit. This tool can shorten a single URL or process a CSV file to shorten multiple URLs in bulk.



## Features

-   **Single URL Shortening**: Quickly shorten a single URL.
-   **Bulk URL Shortening**: Upload a CSV file with a "URL" column to shorten multiple URLs at once.
-   **Download Results**: Download the processed CSV file with the shortened URLs.

## Project Structure

```
urlShortening/
├── .github/
│   └── workflows/
│       └── python-app.yml
├── .gitignore
├── app/
│   ├── __init__.py
│   ├── core.py
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_core.py
├── LICENSE
├── README.md
|── requirements.txt
└── run_app.py
```

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Dmukherjeetextiles/urlShortening.git
    cd urlShortening
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Streamlit application:**

    ```bash
    streamlit run run_app.py
    ```

2.  Open the URL provided by Streamlit in your web browser.

3.  To shorten a single URL, enter it in the text input field and click "Shorten".

4.  To shorten multiple URLs, upload a CSV file that contains a column named "URL".

5.  The results will be displayed on the page, and you can download the CSV file with the shortened URLs.

## Running Tests

To run the tests, execute the following command from the root directory:

```bash
pytest
```

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.