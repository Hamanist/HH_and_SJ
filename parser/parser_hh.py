from typing import List, Optional

from abstract.parser import Parse_Abstract
from source import SourceType
from vacancies.hh import Vacancies_HH
import requests


class Parser_HH(Parse_Abstract):
    __url = 'https://api.hh.ru/vacancies/'

    def get_vacancies(self) -> Optional[List[Vacancies_HH]]:
        response = requests.get(self.__url)
        if response.status_code == 200:
            return self._parse(response.json())
        return None

    def _parse(self, data):
        print('')
        answers = []
        for report in data['items']:
            answers.append(
                Vacancies_HH(
                    title=report['name'],
                    company=report['employer']['name'],
                    url=report['url'],
                    source=SourceType.hh,
                    salary_min=(report['salary'] or {}).get("from"),
                    salary_max=(report['salary'] or {}).get("to")
                )
            )
        return answers
