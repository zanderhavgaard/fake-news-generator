import base64

DEFUALT_DESCRIPTION = """These latest news on the issue shed the whole thing in a new light! WHo would have thought it turned out this way? It was mentioned that..."""


class Article:
    def __init__(
        self,
        header: str,
        image_url: str,
        article_url: str,
        description: str = DEFUALT_DESCRIPTION,
    ) -> None:

        self.header = header
        self.image_url = image_url
        self.article_url = article_url
        self.description = description

    def get_content_dict(self) -> dict:
        return self.__dict__

    def base64_encode(self, string: str):
        return str(base64.urlsafe_b64encode(string.encode("utf-8")), "utf-8")

    def base64_decode(self, string: str):
        return str(base64.urlsafe_b64decode(string), "utf-8")
