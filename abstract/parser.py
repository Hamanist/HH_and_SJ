from abc import ABC, abstractmethod


class Parse_Abstract(ABC):
    @abstractmethod
    def get_vacancies(self): ...

    @abstractmethod
    def _parse(self, data): ...
