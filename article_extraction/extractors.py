from abc import ABC, abstractmethod


class ArticleExtractor(ABC):
    """Base class for all article extractors"""

    @abstractmethod
    def extract_article(self, document: str) -> str:
        """Extract the article from the page contents.

        :param document: The html document to extract the article from
        :returns: Returns the extracted article
        """
