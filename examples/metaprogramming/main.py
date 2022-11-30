# Metaprogramming

# Что такое класс? Это, в принципе, просто кусок кода, описывающий, как создать объект. Но в Питоне класс это нечто большее — классы также
# являются объектами; как только используется ключевое слово class, Питон исполняет команду и создаёт объект:

class A():
    ...


# В памяти будет создан объект с именем A.

# Классы, как и другие объекты, можно создавать на ходу:

def CustomClass(name):
    if name == "foo":
        class Foo:
            ...

        return Foo  # Возвращает именно класс, а не экземпляр
    else:
        class Bar:
            ...

        return Bar


MyClass = CustomClass("foo")
print(MyClass)  # Функция возвращает класс, а не экземпляр
print(my_class := MyClass())  # Можно создать экземпляр класса

# Но это не очень удобно, так как нам до сих пор приходится писать весь код класса.

# Метаклассы.
# Основная цель метаклассов — автоматически изменять класс в момент создания, генерируя классы в соответствии с текущим контекстом.
# Сами по себе метаклассы достаточно просты и работают примерно следующим образом:
# перехватывают создание класса,
# изменяют класс,
# возвращают модифицированный класс.

# Но обычно логику работы метаклассов насыщают вещами вроде интроспекции или манипуляцией наследованием, поэтому конечный код выглядит
# достаточно громоздко.

# Здесь надо добавить больше информации про type и про метаклассы, например, из https://habr.com/ru/post/145835/

# Применение метаклассов. При помощи метаклассов хорошо решаются задачи, например, генерации классов для ORM. Например, для
#  class Person(models.Model):
#     name = models.CharField(max_length=30)
#     age = models.IntegerField()
# код
# keanu = Person(name="Keanu Reeves", age=58)
#   print(keanu.age)
# распечатает число, взятое из БД, потому что потому что models.Model определяет __metaclass__, который сотворит некоторую магию
# и превратит класс Person, который мы только что определили достаточно простым выражением, в сложную привязку к базе данных.