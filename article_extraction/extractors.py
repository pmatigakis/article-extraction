from abc import ABC, abstractmethod
from urllib.request import urlopen


class ArticleExtractor(ABC):
    @abstractmethod
    def extract_article(self, document: str) -> str:
        """Extract the article from the page contents.

        :param document: The html document to extract the article from
        :returns: Returns the extracted article
        """

    def extract_article_from_url(self, url: str) -> str:
        """Extract the article from the page at the url.

        :param url: The url from which to extract the article
        :returns: Returns the extracted article
        """
        url = url.strip()
        if not url.startswith("http://") and not url.startswith("https://"):
            raise ValueError("only http and https schemes are allowed")

        filehandle = urlopen(url)
        content = filehandle.read()
        content = content.decode("utf-8")

        return self.extract_article(content)
