from abc import ABC, abstractmethod
from typing import Literal


class LanguageTranslator(ABC):
    @abstractmethod
    def translate(self, keyword):
        pass


class EnglishLocalizer(LanguageTranslator):

    def translate(self, keyword):
        return keyword


class FrenchLocalizer(LanguageTranslator):

    def __init__(self):
        self.language_map = {
            "car": "voiture",
            "bike": "bicyclette",
            "cycle": "cyclette"
        }

    def translate(self, keyword):
        return self.language_map.get(keyword, "Mapping Not Found!")


class SpanishLocalizer(LanguageTranslator):

    def __init__(self):
        self.language_map = {
            "car": "coche",
            "bike": "bicicleta",
            "cycle": "ciclo"
        }

    def translate(self, keyword):
        return self.language_map.get(keyword, "Mapping Not Found!")


language_list = Literal['english', 'french', 'spanish']
language_map = {
    'english': EnglishLocalizer,
    'french': FrenchLocalizer,
    'spanish': SpanishLocalizer
}


class TextManager:

    __slots__ = (
        '_lang',
        '_translator'
    )

    def __init__(self, lang: language_list = "english"):
        self._lang = lang
        self._translator = language_map.get(self._lang)()

    @property
    def translator(self):
        return self._translator

    @translator.setter
    def translator(self, other):
        self._translator = other

    @property
    def set_language(self):
        return self._lang

    @set_language.setter
    def set_language(self, lang: language_list):
        self._lang = lang
        self.translator = language_map.get(self._lang)()

    def translate(self, keyword):
        return self.translator.translate(keyword)


if __name__ == '__main__':
    tm = TextManager()
    print(tm.translate('car'))
    tm.set_language = "spanish"
    print(tm.translate('car'))
    tm.set_language = "french"
    print(tm.translate('car'))
