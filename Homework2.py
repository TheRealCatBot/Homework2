#Task1:
class Book:
    def __init__(self, name, author, published, pages):
        self._name = name
        self._author = author
        self._published = published
        self._pages = pages

    def info(self):
        print(f"Name: {self._name}, Author: {self._author}, Published in: {self._published}, Pages: {self._pages}")


book1 = Book("FNAF lore", "Tom Scott", "2014", "69")
book2 = Book("1984", "George Orwell", "1949", "70")

book1.info()
book2.info()
# print(book1._name) #არ ბეჭდავს

#Task2:
class EnlargedList(list):
    def min(self):
        temp = 0
        for i in self:
            if temp > self[i-1]:
                temp = i - 1
        print(temp, self[temp])

    def max(self):
        temp = 0
        for i in self:
            if temp < self[i - 1]:
                temp = i - 1
        print(temp, self[temp])


List1 = EnlargedList()
List1.append(1)
List1.append(2)
List1.append(3)
List1.min()
List1.max()

#Task3
class Animal():
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def info(self):
        print(self._name, self._age)

class Dog(Animal):
    def __init__(self, name, age, breed, colour):
        super().__init__(name, age)
        self.__breed = breed
        self.__colour = colour

    def info(self):
        print(self._name, self._age, self.__breed, self.__colour)

doggy = Dog("woofer", 10, "Golden", "Gold")
doggy.info()
# print(doggy.__name) #არ ბეჭდავს

#Task 4
class CallMixin():
    def call(self, name, lastname, phone):
        print("Calling:",name,lastname,"On:",phone)


class Person(CallMixin):
    def __init__(self,fname,lname,phone):
        self.name = fname
        self.surname = lname
        self.phone = phone

    def info(self):
        print(self.name, self.surname, self.phone)

    def call(self, **kwargs):
        CallMixin.call(self, self.name, self.surname, self.phone)


Person1 = Person("Guja", "Kikabidze", "599781277")
Person1.call()