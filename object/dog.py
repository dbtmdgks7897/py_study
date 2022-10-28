from animal import Animal


class Dog(Animal):

    count = 0

    def __init__(self,
                 name: str = "멍",
                 age: int = 0
                 ):
        """

        Args:
            name (str, optional): 고양이의 이름. 기본값은 "냥".
            age (int, optional): 고양이의 나이. 기본값은 0.
        """

        super().__init__(age)

        self.name = name

        Dog.count = Dog.count + 1

        return

    def eat(self):
        print(f"강아지 '{self.name}'이 음식을 먹었습니다.")

    @classmethod
    def get_count(cls):
        print(f"강아지가 {cls.count}마리 생성되었습니다.")