class Car():
    def __init__(self, *args, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    def __str__(self):
        return f"Car with {self.wheels} wheels"

# 상위 클래스 상속
class Conventable(Car):
    def __init__(self, *args, **kwargs):
        # 상위 클래스의 메소드 상속 없으면 오버라이딩
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"

    def __str__(self):
        return f"Car with no roof"


porche = Conventable(color="green", price="$40")
print(porche.color)
