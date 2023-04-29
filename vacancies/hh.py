from base.vacancies import Vacancies_Base
from source import SourceType


class Vacancies_HH(Vacancies_Base):
    def __init__(self, title: str, source: SourceType, company: str, url: str, salary_min=0, salary_max=0):
        super().__init__(title, source, company, url, salary_min, salary_max)
        self.source = SourceType.hh
