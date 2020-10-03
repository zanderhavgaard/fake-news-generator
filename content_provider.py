import json
import random


class ContentProvider:
    def __init__(self) -> None:

        # static ocntent to generate news articles from
        self.headers = []
        self.people = []
        self.things = []
        self.adjectives = []
        self.image_urls = {}

        # placeholder strings to replace
        self.people_placeholder = "%people%"
        self.thing_placeholder = "%things%"
        self.adjective_placeholder = "%adjective%"

        # load static content from json content file
        self.load_json_data()

    def load_json_data(self) -> None:
        # load data from
        with open("fake_news_content.json") as json_file:
            data = json.loads(json_file.read())

            # save data in object
            self.headers = data["headers"]
            self.people_dicts = data["people"]
            self.things_dicts = data["things"]
            self.adjectives = data["adjectives"]

            # create lookup dict for image urls
            self.image_urls = {}
            for p in self.people_dicts:
                self.image_urls[p["people"]] = p["url"]
            for t in self.things_dicts:
                self.image_urls[t["things"]] = t["url"]

            # change people and things to not contain urls
            self.people, self.things = [], []
            for p in self.people_dicts:
                self.people.append(p["people"])
            for t in self.things_dicts:
                self.things.append(t["things"])

    def get_random_header(self) -> str:
        return self.headers[random.randint(0, len(self.headers) - 1)]

    def get_random_people(self) -> str:
        return self.people[random.randint(0, len(self.people) - 1)]

    def get_random_thing(self) -> str:
        return self.things[random.randint(0, len(self.things) - 1)]

    def get_random_adjective(self) -> str:
        return self.adjectives[random.randint(0, len(self.adjectives) - 1)]

    def get_image_url(self, key: str) -> str:
        return self.image_urls[key]

    def replace_placeholders_in_header(self, header: str) -> str:
        # select image for article
        image_should_be_people = False
        image_should_be_things = False
        has_chosen_image_for_article = False
        image_url = "placeholder"
        if self.people_placeholder in header and self.thing_placeholder in header:
            # choose to use people or things based on what occurs first in header
            people_pos = header.find(self.people_placeholder)
            things_pos = header.find(self.thing_placeholder)
            # if things is first choose things for the image
            if people_pos > things_pos:
                image_should_be_things = True
            else:
                image_should_be_people = True
        elif self.people_placeholder in header:
            image_should_be_people = True
        elif self.thing_placeholder in header:
            image_should_be_things = True

        # keep track of items used
        used = []

        # replace people
        for _ in range(header.count(self.people_placeholder)):
            people = self.get_random_people()
            while people in used:
                people = self.get_random_people()
            # choose image for article based on selected people
            if not has_chosen_image_for_article and image_should_be_people:
                image_url = self.get_image_url(key=people)
                has_chosen_image_for_article = True
            used.append(people)
            header = header.replace(self.people_placeholder, people, 1)

        # replace things
        for _ in range(header.count(self.thing_placeholder)):
            thing = self.get_random_thing()
            while thing in used:
                thing = self.get_random_thing()
            # choose image based for article based on selected things
            if not has_chosen_image_for_article and image_should_be_things:
                image_url = self.get_image_url(key=thing)
                has_chosen_image_for_article = True
            used.append(thing)
            header = header.replace(self.thing_placeholder, thing, 1)

        # replace adjectives
        for _ in range(header.count(self.adjective_placeholder)):
            adjective = self.get_random_adjective()
            while adjective in used:
                adjective = self.get_random_adjective()
            used.append(adjective)
            header = header.replace(self.adjective_placeholder, adjective, 1)

        return (header, image_url)

    def generate_content(self) -> (str, str):
        header = self.get_random_header()
        header, image_url = self.replace_placeholders_in_header(header)
        return (header, image_url)
