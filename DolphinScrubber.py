import urllib
from urllib.request import urlopen

class DolphinScrubber():
    def __init__(self, url=""):
        self.url = url
        print("Welcome to Dolphin Scrubber!")
    def get_url(self):
        if self.url == "":
            self.url = input("Please input a URL (eg. https://en.wikipedia.org/wiki/Giant_oarfish): ")
        else:
            possible_answers = ["y", "n", "yes", "no", "yeah", "nope"]
            errrr = []
            dingdingding = []
            for answer in possible_answers:
                if answer.__contains__("y"):
                    dingdingding.append(answer)
                elif answer.__contains__("n"):
                    errrr.append(answer)
            user_choice = input(f"There is already a URL input: {self.url}, Would you like to input a new one? ")
            while user_choice.lower() not in possible_answers:
                user_choice = input(f"Valid options include {possible_answers}, Please try again: ")
            else:
                if user_choice in errrr:
                    print("Using old/current URL")
                    self.url = self.url
                elif user_choice in dingdingding:
                    print("Changing URL...")
                    self.url = input("Please input a new URL (eg. https://en.wikipedia.org/wiki/Giant_oarfish): ")
        return self.url

    # tutorial code from: https://realpython.com/python-web-scraping-practical-introduction/
    def open_url(self, url):
        try:
            page = urlopen(url)
            html_bytes = page.read()
            html = html_bytes.decode("utf-8")
        except Exception as e:
            print("URL could not be opened/decoded: ", e)
        print(html)
        return html

    # tutorial code from: https://realpython.com/python-web-scraping-practical-introduction/
    def html_tag_search(self, html):
        input_tag = input("Please input the tag of the text you want to search for (eg. '<title>'): ")
        start_index = html.find(f"{input_tag}") + len(f"{input_tag}")
        end_index = html.find("</title>")
        text = html[start_index:end_index]
        if text:
            print(f"Found text: {text}")
        else:
            print(f"No text was found under the tag {input_tag}")

if __name__ == "__main__":
    my_scrubber = DolphinScrubber()
    input_url = my_scrubber.get_url() # asks the user to set a global url variable
    output_html = my_scrubber.open_url(input_url) # reads the url and saves HTML 
    my_scrubber.html_tag_search(output_html)