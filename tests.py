import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
#class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    #def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        #collector = BooksCollector()

        # добавляем две книги
        #collector.add_new_book('Гордость и предубеждение и зомби')
        #collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        #assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

class TestBooksCollector:

    def test_add_new_book_if_add_one_book_positive_case(self, collector):
        collector.add_new_book('Грозовой перевал')
        assert 'Грозовой перевал' in collector.books_genre

    def test_add_new_book_if_genre_is_empty_by_default_positive_case(self, collector):
        collector.add_new_book('Грозовой перевал')
        assert collector.books_genre['Грозовой перевал'] == ''

    def test_add_new_book_if_book_name_40_symbols_positive_case(self, collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert 'Что делать, если ваш кот хочет вас убить' in collector.books_genre

    def test_add_new_book_if_same_book_added_twice_positive_case(self, collector):
        collector.add_new_book('Грозовой перевал')
        collector.add_new_book('Грозовой перевал')
        assert list(collector.books_genre.keys()).count('Грозовой перевал') == 1

    def test_add_new_book_if_book_name_more_than_40_symbols_negative_case(self, collector):
        collector.add_new_book('Гарри Поттер и узник Азкабана. Том третий') #41 символ
        assert 'Гарри Поттер и узник Азкабана. Том третий' not in collector.books_genre

    def test_add_new_book_if_empty_name_negative_case(self, collector):
        collector.add_new_book('')
        assert '' not in collector.books_genre

    def test_set_book_genre_if_book_in_books_genre_positive_case(self,collector):
        collector.add_new_book('Я, робот')
        collector.set_book_genre('Я, робот', 'Фантастика')
        assert collector.books_genre['Я, робот'] == 'Фантастика'

    def test_set_book_genre_if_book_not_in_books_genre_negative_case(self,collector):
        collector.set_book_genre('Я, робот', 'Фантастика')
        assert 'Я, робот' not in collector.books_genre

    def test_set_book_genre_if_genre_not_in_list_negative_case(self, collector):
        collector.add_new_book('Исчезнувшая')
        collector.set_book_genre('Исчезнувшая', 'Триллер')
        assert collector.books_genre['Исчезнувшая'] == ''

    def test_get_book_genre_if_genre_is_set_positive_case(self, collector):
        collector.add_new_book('Я, робот')
        collector.set_book_genre('Я, робот', 'Фантастика')
        assert collector.get_book_genre('Я, робот') == 'Фантастика'

    def test_get_book_genre_if_genre_is_not_set_positive_case(self, collector):
        collector.add_new_book('Я, робот')
        assert collector.get_book_genre('Я, робот') == ''

    def test_get_book_genre_if_book_not_in_books_genre_negative_case(self, collector):
        assert collector.get_book_genre('Я, робот') is None


    def test_get_books_with_specific_genre_if_books_in_list_positive_case(self, collector):
        collector.add_new_book('Я, робот')
        collector.set_book_genre('Я, робот', 'Фантастика')

        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        collector.add_new_book('Солярис')
        collector.set_book_genre('Солярис', 'Фантастика')
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 3

    def test_get_books_with_specific_genre_if_books_have_different_genres_positive_case(self, collector):
        collector.add_new_book('Я, робот')
        collector.set_book_genre('Я, робот', 'Фантастика')

        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')

        collector.add_new_book('Исчезнувшая')
        collector.set_book_genre('Исчезнувшая', 'Детективы')
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

    def test_get_books_with_specific_genre_returns_empty_list_if_no_books_match_positive_case(self, collector):
        collector.add_new_book('Я, робот')
        collector.set_book_genre('Я, робот', 'Фантастика')

        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_with_specific_genre('Детективы') == []

    def test_get_books_genre_returns_current_dict_positive_case(self, collector):
        collector.add_new_book('Я, робот')
        collector.set_book_genre('Я, робот', 'Фантастика')
        assert collector.get_books_genre() == {'Я, робот': 'Фантастика'}

    def test_get_books_for_children_return_list_with_books_for_children_positive_case(self, collector):
        collector.add_new_book('Я, робот')
        collector.set_book_genre('Я, робот', 'Фантастика')
        assert collector.get_books_for_children() == ['Я, робот']

    def test_get_books_for_children_returns_empty_list_if_book_has_age_rating_positive_case(self, collector):
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_if_book_add_in_books_genre_positive_case(self, collector):
        collector.add_new_book('Я, робот')
        collector.add_book_in_favorites('Я, робот')
        assert 'Я, робот' in collector.favorites

    def test_add_book_in_favorites_if_book_added_twice_positive_case(self, collector):
        collector.add_new_book('Я, робот')
        collector.add_book_in_favorites('Я, робот')
        collector.add_book_in_favorites('Я, робот')
        assert collector.favorites.count('Я, робот') == 1

    def test_delete_book_from_favorites_if_book_add_to_favorites_positive_case(self,collector):
        collector.add_new_book('Я, робот')
        collector.add_book_in_favorites('Я, робот')
        collector.delete_book_from_favorites('Я, робот')
        assert 'Я, робот' not in collector.favorites

    def test_delete_book_from_favorites_if_book_not_in_favorites_negative_case(self, collector):
        collector.add_new_book('Я, робот')
        collector.delete_book_from_favorites('Я, робот')
        assert collector.favorites == []

    @pytest.mark.parametrize('book', ['Я, робот', 'Дюна', 'Солярис'])
    def test_get_list_of_favorites_books_returns_list_of_favorites_books_positive_case(self, collector, book):
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert book in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_returns_empty_list_if_book_not_in_favorites(self, collector):
        collector.add_new_book('Я, робот')
        assert collector.get_list_of_favorites_books() == []
