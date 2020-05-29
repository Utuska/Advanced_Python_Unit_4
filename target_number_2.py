from datetime import datetime
import dis


def decorators_logger(path):
    way = str(path)

    def path_write(old_function):
        def collection_date(*args, **kwargs):
            start = datetime.now()

            result = old_function(*args, **kwargs)

            delta_time = datetime.now() - start

            name_foo = old_function.__name__
            open_write = open(way + r'\information_' + str(name_foo) + '.txt', 'wb')
            open_write.write(
                f' Имя функции: {name_foo} \n Запуск: {start} \n Входные переменные: {args} {kwargs} \n Результат: {result} \n Время работы программы: {delta_time}'.encode())
            dis.dis(old_function)
            open_write.close()
            return result

        return collection_date

    return path_write


@decorators_logger(r'c:\Unit\Adv_py\Unit_1(4)_nam')  # указываем путь куда будем записывать
def foo(x):
    print("Выполнение" * x)
    return x


if __name__ == '__main__':
    m = foo(10000)
