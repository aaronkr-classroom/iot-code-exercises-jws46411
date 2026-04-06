# 5_class.py

class Animal:
        def __init__(self, name):
                self.name = name
                
                def speak(self):
                    print(f"my name is {self.name}!")
                        #자식 클래스에서 구현
                    
                    def setName(self, name: str):	# 세터 매소드 = 재정의 
                        self.name = name
                    
                    """
                    set the Animal clsss's name.
                    Animal 클래스의 이름을 반환하는 함수.
                    :param name: 새로운 Animal의 이름
                    """
                    
                    self.name = name
                        
                    def getName(self) -> str:
                    
                    """
                    Return the Animal clsss's name.
                    Animal 클래스의 이름을 반환하는 함수.
                    :return: Animal의 이름
                    """
                    return self.name
                    
class Dog(Animal): # is-a 관계 (자식)
    def __init__(self, name, age = 3):
        super().__init__(name)
        self.age = age	# has-a 속성
        
        
        def speak(self):
            super().speak()
            print(f"{self.name} says woof!")
            
class cat(Animal):
    def speak(self):
        print(f"{self.name} says meow!")
        
# 호출

my_dog = Dog("spot")
my_cat = Cat("Headache")
my_dog.speak()
My_cat.speak()