import requests
from bs4 import BeautifulSoup

from .log import logger

icon_rels = {
    "icon",
    "apple-touch-icon",
    "shortcut icon"
}
block_list_rels = {
    "preload",
    "image_src",
    "preconnect",
    "canonical",
    "alternate",
    "stylesheet"
}
icon_extenstions = {
    ".ico",
    ".png",
    ".jpg",
    ".jpeg"
}
media_types = {
    "image/png",
    "image/x-icon",
    "image/vnd.microsoft.icon",
    "image/jpeg"
}


def parse_icon(hostname: str):
    request_parts = build_request(hostname)
    page = requests.get(
        request_parts['uri'],
        headers=request_parts['headers']
    ).text
    html = BeautifulSoup(page, "html.parser")

    links = [{
        "href": link.get("href"),
        "sizes": link.get("sizes"),
        "rel": link.get("rel")
    } for link in html.head.find_all('link')]

    icons = []
    for link in links:
        rel = link["rel"][0]
        if rel != "null" and rel.lower() in icon_rels:
            icons.append(icon_result(link))
        elif rel == "null" or rel.lower() not in block_list_rels:
            icons.append(icon_result(link))

    icons.sort(key=lambda x: x["priority"])
    #for icon in icons:
    #    if icon["path"].startswith("//"):

    return icons


def build_request(hostname: str):
    uri = f"https://{hostname}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/" +
            "537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 " +
            "Edge/16.16299",
        "Accept-Language": "en-US,en;q=0.8",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9," +
            "image/webp,image/apng,*/*;q=0.8"
    }

    return {
        "uri": uri,
        "headers": headers
    }


def icon_result(link: dict):
    icon = {
        "path": link["href"],
        "sizes": link["sizes"]
    }

    if icon["sizes"] != None:
        width, height = icon["sizes"].split("x")

        if width == height:
            priorities = {
                "32": 1,
                "64": 2,
                "16": 4,
            }

            if width in priorities.keys():
                icon["priority"] = priorities[width]
            elif int(width) >= 24 and int(width) <= 128:
                icon["priority"] = 3
            else:
                icon["priority"] = 100
    else:
        icon["priority"] = 200

    return icon


def get_scheme(uri):
    return "http" if uri.split("://") else "https"
