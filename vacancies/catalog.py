from typing import List
import csv

from parser.parser_hh import Parser_HH
from parser.parser_sj import Parser_SJ
from vacancies.hh import Vacancies_HH
from vacancies.sj import Vacancies_SJ


class Catalog:
    list_sj: List[Vacancies_SJ] = []
    list_hh: List[Vacancies_HH] = []

    def upload_vacancies(self):
        self.list_sj = Parser_SJ().get_vacancies()
        self.list_hh = Parser_HH().get_vacancies()

    def save_to_file(self):
        if self.list_sj or self.list_hh:
            with open('./vacancies.csv', 'a', encoding='utf-8') as file:
                file.writelines([report.get_from_string() for report in self.list_sj])
                file.writelines([report.get_from_string() for report in self.list_hh])
