# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
 #       print("{0} : {1} 방향으로 날아갑니다 [속도 {2}]".format(self.name, location, self.speed))
        print(f"{self.name} : {location} 방향으로 날아갑니다 [속도 {self.speed}]")


# 공격 유닛
class AttackUnit(Unit):

    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage


    def attack(self, location):
  #      print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다 [공격력 {self.damage}]")



    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다".format(self.name))


# 날 수 있는 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))    


# 공격 가능 공중 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 속도는 0
        Flyable.__init__(self, flying_speed)



# 발키리
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie. fly(valkyrie.name, "3시")

# 벌쳐
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저

battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly("배틀크루저")



