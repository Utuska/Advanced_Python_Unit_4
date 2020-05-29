from datetime import datetime
import dis


def decorators_logger(old_function):
    def collection_date(*args, **kwargs):
        start = datetime.now()

        result = old_function(*args, **kwargs)

        delta_time = datetime.now() - start
        print(delta_time)

        name_foo = old_function.__name__
        open_write = open('properties.txt', 'wb')
        open_write.write(
            f' Имя функции: {name_foo} \n Запуск: {start} \n Входные переменные: {args} {kwargs} \n Результат: {result} \n Время работы программы: {delta_time}'.encode())
        dis.dis(old_function)
        open_write.close()
        return result

    return collection_date


@decorators_logger
def foo(x):
    print("Выполнение" * x)
    return x


if __name__ == '__main__':
    m = foo(10000)
