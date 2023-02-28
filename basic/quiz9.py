class SoldOutError(Exception):
    pass

stock_chicken = 10
wait_number = 1

try:
    while True:
        print(f"[남은 치킨 : {stock_chicken} 마리]")
        order = int(input("치킨 몇 마리를 주문하시겠습니까?"))

        if order > stock_chicken:
            print("재고가 부족합니다.")
        else:
            print(f"[대기번호 {wait_number}] {order} 마리 주문이 완료되었습니다.")
            wait_number = wait_number + 1
            stock_chicken = stock_chicken - order

        if stock_chicken <= 0:
            raise SoldOutError()
            break

except ValueError:
    print("잘못된 값을 입력하였습니다")
except SoldOutError:
    print("재고가 소진되어 더 이상 주문을 받지 않습니다.")