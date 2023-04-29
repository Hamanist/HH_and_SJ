from source import SourceType


class Vacancies_Base:
    """

    """
    title: str
    company: str
    url: str
    salary_min: int | float
    salary_max: int | float
    source: SourceType


    def __init__(self, title: str, source: SourceType, company: str, url: str, salary_min=0, salary_max=0):
        self.title = title
        self.company = company
        self.url = url
        self.salary_min = salary_min or 0
        self.salary_max = salary_max or 0

        self.source = source

    def __str__(self):
        return f'{self.title}' \
               f' в {self.company}' \
               f' ссылка {self.url}' \
               f' Зарплата от {self.salary_min} до {self.salary_max}' \
               f' Источник {self.source.value}'

    def __eq__(self, other):
        return self.salary_max == other.salary_max

    def __ne__(self, other):
        return self.salary_max != other.salary_max

    def __lt__(self, other):
        return self.salary_max < other.salary_max

    def __le__(self, other):
        return self.salary_max <= other.salary_max

    def __gt__(self, other):
        return self.salary_max > other.salary_max

    def __ge__(self, other):
        return self.salary_max >= other.salary_max

    def get_from_string(self):
        return ';'.join(
            [self.title, self.company, self.url, str(self.salary_min), str(self.salary_max), self.source.value]) + "\n"
