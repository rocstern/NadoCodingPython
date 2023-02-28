from random import *

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{self.name} : 유닛이 생성되었습니다.")

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 날아갑니다 [속도 {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")


# 공격 유닛
class AttackUnit(Unit):

    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage


    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다 [공격력 {self.damage}]")



    # def damaged(self, damage):
    #     print(f"{self.name} : {damage} 데미지를 입었습니다.")
    #     self.hp -= damage
    #     print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
    #     if self.hp <= 0:
    #         print(f"{self.name} : 파괴되었습니다.")

#마린
class Marine(AttackUnit):
    def __init__(self):
        # AttackUnit.__init__(self, "마린", 40, 1, 5
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp = self.hp - 10
            print(f"{self.name} : 스팀팩을 사용합니다. (HP 10 감소)")
        else:
            print(f"{self.name} : 체력이 부족하여 스팀팩을 사용하지 않습니다")

# 탱크
class Tank(AttackUnit):

    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        # 현재 시즈모드가 아닐때 -> 실행
        if self.seize_mode == False:
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.damage = self.damage * 2
            self.seize_mode = True
        # 현재 시즈모드일 때 -> 해제
        else:
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.damage = self.damage / 2
            self.seize_mode = False


# 날 수 있는 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")


# 공격 가능 공중 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 속도는 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print(f"{self.name} : 클로킹 모드 해제 합니다.")
            self.clocked = False
        else:
            print(f"{self.name} : 클로킹 모드 실행합니다")
            self.clocked = True



def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player: gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")





# 실제 게임 진행

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()
w2 = Wraith()


# 유닛 일괄
attack_unit = []
attack_unit.append(m1)
attack_unit.append(m2)
attack_unit.append(m3)
attack_unit.append(t1)
attack_unit.append(t2)
attack_unit.append(w1)
attack_unit.append(w2)

for unit in attack_unit:
    unit.move("1시")

Tank.seize_developed = True
print("탱크 시즈모드 개발이 완료되었습니다.")

for unit in attack_unit:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_unit:
    unit.attack("1시")

# 전군 피해
for unit in attack_unit:
    unit.damaged(randint(5, 400))

# 게임 종료
game_over()









































