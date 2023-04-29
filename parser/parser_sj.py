from typing import Optional, List

from abstract.parser import Parse_Abstract
import requests

from source import SourceType
from vacancies.sj import Vacancies_SJ


class Parser_SJ(Parse_Abstract):
    __headers = {
        'X-Api-App-Id':
            'v3.r.137507831.2669b6366e3e47dcac7a8e6a728c694eaee05ed6.ca9e1a3d88806c103e001d985e00ea493a188827'
    }
    __url = 'https://api.superjob.ru/2.0/vacancies'

    def get_vacancies(self) -> Optional[List[Vacancies_SJ]]:
        response = requests.get(self.__url, headers=self.__headers)
        if response.status_code == 200:
            return self._parse(response.json())
        return None

    def _parse(self, data) -> Optional[List[Vacancies_SJ]]:
        answers = []
        for report in data['objects']:
            answers.append(
                Vacancies_SJ(
                    title=report['profession'],
                    company=report['firm_name'],
                    url=report['link'],
                    salary_min=report['payment_from'],
                    salary_max=report['payment_to'],
                    source=SourceType.sj
                )
            )
        return answers
