import json
import os

BOOKMARK_FILE = "data/bookmarks.json"


def load_bookmarks():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(BOOKMARK_FILE):
        with open(BOOKMARK_FILE, "w") as f:
            json.dump([], f)

    with open(BOOKMARK_FILE, "r") as f:
        return json.load(f)


def save_bookmarks(bookmarks):
    with open(BOOKMARK_FILE, "w") as f:
        json.dump(bookmarks, f, indent=4)


def add_bookmark(article):
    bookmarks = load_bookmarks()

    new_item = {
        "title": article.get("title"),
        "url": article.get("url"),
        "source": article.get("source", {}).get("name", "Unknown")
    }

    if new_item not in bookmarks:
        bookmarks.append(new_item)
        save_bookmarks(bookmarks)
        return True

    return False


def remove_bookmark(url):
    bookmarks = load_bookmarks()
    bookmarks = [b for b in bookmarks if b["url"] != url]
    save_bookmarks(bookmarks)