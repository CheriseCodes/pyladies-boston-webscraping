import requests
from bs4 import BeautifulSoup

def main():
    # Make HTTP request to Wikipedia to retrieve HTML
    response = requests.get("https://en.wikipedia.org/wiki/OpenAI")

    # Load HTML into Beautiful Soup HTML parser
    soup = BeautifulSoup(response.content, 'html.parser')

    # Retrieve the first table using CSS Selectors
    result = soup.select_one("#mw-content-text > div.mw-content-ltr.mw-parser-output > table.infobox.ib-company.vcard")

    # Print the result
    print(result)


if __name__ == "__main__":
    main()