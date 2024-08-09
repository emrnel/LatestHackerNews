import requests
import threading
import tkinter as tk
from tkinter import scrolledtext
import webbrowser

NUM_OF_ARTICLES = 30

window = tk.Tk()
window.title("Latest HN")
window.geometry("800x600")
window.config(padx=24, pady=10, bg="green")

header_label = tk.Label(window, text="Latest Hacker News", font=("Helvetica", 32), background="green", foreground="white")
header_label.pack()

new_news_url = "https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty"
main_url = "https://hacker-news.firebaseio.com/v0/"

collected_urls = []
answers = []

# Create a ScrolledText widget to display content
text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Arial", 12), spacing3=8)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

def open_url(event):
    # Get the start and end indices of the tag where the click happened
    start_index = text_area.index("@%s,%s linestart" % (event.x, event.y))
    end_index = text_area.index(f"{start_index} lineend")

    # Extract the entire line (URL)
    url = text_area.get(start_index, end_index).strip().split(" ")[-1]
    webbrowser.open(url)

def print_content(answers):
    # Configure tags for formatting
    text_area.tag_configure("title", font=("Arial", 12, "bold"))
    text_area.tag_configure("details", font=("Arial", 12, "normal"))
    text_area.tag_configure("clickable", foreground="blue", underline=True)

    for answer in answers:
        # Check if the 'title' key exists and print the title in bold
        if "title" in answer:
            title = answer["title"].split("\n")[0].strip()
            text_area.insert(tk.END, title + "\n", "title")

        # Check if the 'url' key exists before accessing it
        if "url" in answer and answer["url"] is not None:
            text_area.insert(tk.END, "Details: ", "details")

            url = answer["url"].strip()
            start_index = text_area.index(tk.END)
            text_area.insert(tk.END, url + "\n\n", "clickable")
            end_index = text_area.index(tk.END)

            # Tag the URL and make it clickable
            text_area.tag_add("clickable", start_index, end_index)
            text_area.tag_bind("clickable", "<Button-1>", open_url)


def article_collector(articles):
    for article in articles:
        single_url = main_url + "item/" + str(article) + ".json?print=pretty"
        collected_urls.append(single_url)

def make_request(url):
    single_response = requests.get(url)
    answer = single_response.json()
    answers.append(answer)

def thread_function(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=make_request, args=(url,))
        thread.start()
        threads.append(thread)
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

# Fetch and display content
response = requests.get(new_news_url)
new_thirty = response.json()[:NUM_OF_ARTICLES]
article_collector(new_thirty)
thread_function(collected_urls)
print_content(answers)

window.mainloop()
