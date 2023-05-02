from parser.parser_hh import Parser_HH
from parser.parser_sj import Parser_SJ
from vacancies.catalog import Catalog
from vacancies.sj import Vacancies_SJ

Parser_HH().get_vacancies()
Parser_SJ().get_vacancies()
cat = Catalog()
cat.upload_vacancies()
cat.save_to_file()

