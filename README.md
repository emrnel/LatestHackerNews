# Latest Hacker News

This is a Tkinter-based GUI application that fetches and displays the latest articles from Hacker News. The articles are fetched using the `requests` library and displayed in a scrollable text area. Users can click on the article URLs to open them in a web browser.

## Features

- Fetch the latest Hacker News articles
- Display article titles and URLs in a scrollable text area
- Clickable URLs to open articles in a web browser

## Screenshot

![App Screenshot](screenshot.png)

## Threading

This application uses Python's `threading` module to fetch multiple articles concurrently. Instead of fetching each article one by one, threading allows the application to make multiple network requests simultaneously. This significantly reduces the time it takes to retrieve and display the latest news.

### How It Works

- **Article Collection:** The application first collects the IDs of the latest articles from Hacker News.
- **Threaded Requests:** For each article ID, a separate thread is created to fetch the article details (title, URL, etc.) using the `requests` library.
- **Joining Threads:** After starting all threads, the application waits for all threads to complete using the `join()` method. This ensures that the content is only displayed once all articles have been fetched.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```bash
    python latest_hn.py
    ```

2. The latest articles from Hacker News will be displayed. Click on a URL to open the article in your web browser.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
