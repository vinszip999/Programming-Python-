import random
import string


class VCafe:

    def __init__(self):

        self.drink_sum = 0  # 음료수 가격 계산하는 변수
        self.drink_menu = []
        self.coffee = ["아메리카노", "카라멜마끼아또"]
        self.latte = ["고구마라떼", "초코라떼", "녹차라떼", "카페라떼", "바닐라라떼"]
        self.smoothie = ["망고스무디", "블루베리스무디", "딸기스무디", "수박스무디"]
        self.tea = ["복숭아아이스티", "레몬아이스티", "블루레몬아이스티", "밀크티"]
        self.ade = ["블루레몬에이드", "자몽에이드", "오렌지에이드", "라임에이드"]

        self.side_sum = 0  # 사이드메뉴 가격을 계산하는 변수
        self.side_menu = []
        self.cake = ["티라미슈", "초코케익", "치즈케익", "녹차케익"]
        self.sandwich = ["참치샌드위치", "모닝샌드위치", "야채샌드위치"]

    # def __str__(self):
    #     pass

    # 영수증 보여주기 ("~ 음료수 ( ~ 사이드 메뉴) 맞으십니까?")
    def all_show_receipt(self):
        pass

    # 좌석 고르기
    def choice_seat(self):
        fixed_seat = []
        print('<사용중인 좌석>')  # 사용 가능 좌석
        print(fixed_seat)
        while True:
            seat = int(input('1~10 좌석 중 앉을 좌석을 고르세요 ex) 1 : '))
            if seat != fixed_seat:
                fixed_seat.append(seat)
                print(fixed_seat)
                break
            else:  # seat == fixed_seat
                print('*** 이미 사용중인 좌석입니다. 미사용 좌석으로 다시 골라주세요 *** ')

    # 결제하기
    def payment(self):
        pass
        # Drink.choice_drink(self.drink_sum)

    # ("몇번자리: 음료수는 : 보안번호는 : ") 맞으면 퇴실처리, 틀리면 반복하거나 종료
    def return_drink(self):
        number_of_strings = 1
        length_of_string = 5
        for x in range(number_of_strings):
            print(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))


class Drink(VCafe):

    # 음료수 메뉴 보여주기
    def show_drink_menu(self):
        print('--------------------<음료수>--------------------\n'
              '1. 커피 (3000)\n'
              f'{self.coffee}\n'
              '2. 라떼(3500)\n'
              f'{self.latte}\n'
              '3. 스무디(3000)\n'
              f'{self.smoothie}\n'
              '4. 티(2500)\n'
              f'{self.tea}\n'
              '5. 에이드(3000)\n'
              f'{self.ade}')
        print('='*50)

    # 음료수 선택하기
    def choice_drink(self):
        while True:
            choice_menu = input('"1. 커피 2. 라떼 3. 스무디 4. 티 5. 에이드" 중 마실 음료수 종류를 고르세요 ex) 1~5 : ')

            if choice_menu == '1':
                self.drink_sum += 3000
                print('=' * 50)
                print(f'1. 커피 (3000)\n'
                      f'{self.coffee}')
                print('=' * 50)

                while True:
                    choice_coffee = input(f'"{self.coffee}" 중 원하는 음료수를 선택하세요 : ')
                    for co in self.coffee:
                        if co == choice_coffee:
                            self.drink_menu.append(co)
                            print(self.drink_menu)
                            return self.drink_sum
                        elif choice_coffee == 'esc':
                            break
                        else:  # c != choice_coffee:
                            print(f' *** "{self.coffee}" 중 다시 고르세요 ***\n'
                                  ' << 나가려면 "esc"를 치세요 >>')
                            break


            elif choice_menu == '2':
                self.drink_sum += 3500
                print('=' * 50)
                print('2. 라떼(3500)\n'
                      f'{self.latte}')
                print('=' * 50)

                while True:
                    choice_latte = input(f'"{self.latte}" 중 원하는 음료수를 선택하세요 : ')
                    for la in self.latte:
                        if la == choice_latte:
                            self.drink_menu.append(choice_latte)
                            print(self.drink_menu)
                            return self.drink_sum
                        elif choice_latte == 'esc':
                            break
                        else:  # la != choice_latte:
                            print(f' *** "{self.latte}" 중 다시 고르세요 ***\n'
                                  ' << 나가려면 "esc"를 치세요 >>')
                            break

            elif choice_menu == '3':
                self.drink_sum += 3000
                print('=' * 50)
                print('3. 스무디(3000)\n'
                      f'{self.smoothie}')
                print('=' * 50)

                while True:
                    choice_smoothie = input(f'"{self.smoothie}" 중 원하는 음료수를 선택하세요 : ')
                    for smoo in self.smoothie:
                        if smoo == choice_smoothie:
                            self.drink_menu.append(choice_smoothie)
                            print(self.drink_menu)
                            return self.drink_sum
                        elif choice_smoothie == 'esc':
                            break
                        else:  # smoo != choice_smoothie:
                            print(f' *** "{self.smoothie}" 중 다시 고르세요 ***\n'
                                  ' << 나가려면 "esc"를 치세요 >>')
                            break

            elif choice_menu == '4':
                self.drink_sum += 2500
                print('=' * 50)
                print('4. 티(2500)\n'
                      f'{self.tea}')
                print('=' * 50)

                while True:
                    choice_tea = input(f'"{self.tea}" 중 원하는 음료수를 선택하세요 : ')
                    for te in self.tea:
                        if te == choice_tea:
                            self.drink_menu.append(choice_tea)
                            print(self.drink_menu)
                            return self.drink_sum
                        elif choice_tea == 'esc':
                            break
                        else:  # te != choice_tea:
                            print(f' *** "{self.tea}" 중 다시 고르세요 ***\n'
                                  ' << 나가려면 "esc"를 치세요 >>')
                            break

            elif choice_menu == '5':
                self.drink_sum += 3000
                print('=' * 50)
                print('5. 에이드(3000)\n'
                      f'{self.ade}')
                print('=' * 50)

                while True:
                    choice_ade = input(f'"{self.ade}" 중 원하는 음료수를 선택하세요 : ')
                    for ad in self.ade:
                        if ad == choice_ade:
                            self.drink_menu.append(choice_ade)
                            print(self.drink_menu)
                            return self.drink_sum
                        elif choice_ade == 'esc':
                            break
                        else:  # x != choice_coffee:
                            print(f' *** "{self.ade}" 중 다시 고르세요 ***\n'
                                  ' << 나가려면 "esc"를 치세요 >>')
                            break

            elif choice_menu == 'esc':
                break

            else:
                print(' *** "1. 커피 2. 라떼 3. 스무디 4. 티 5. 에이드" 중 마실 음료수 종류를 다시 고르세요 *** \n'
                      ' << 나가려면 "esc"를 치세요 >> ')

    # 어떤 타이틀 음료수 메뉴 추가할건지 물어보기 ("1. 커피, 2. 라떼, 3. 스무디, 4. 티, 5. 에이드 메뉴 중 어떤 메뉴의 음료수를 추가하시겠습니까?")
    def add_drink_menu(self):
        while True:
            menu_choice = input('"1. 커피 2. 라떼 3. 스무디 4. 티 5. 에이드" 메뉴 중 어떤 메뉴의 음료수를 추가하시겠습니까? ex) 1~5 : ')
            if menu_choice == '1':
                print(self.coffee)
                append_coffee = input(f'{self.coffee}를 제외하고 추가할 메뉴를 입력하세요 : ')
                # ch: str
                for ch_co in self.coffee:
                    if ch_co == append_coffee:
                        print(" *** 입력하신 메뉴는 이미 있는 메뉴 입니다. ***\n"
                              " --- 기존 메뉴를 제외한 메뉴를 입력해주세요 ---")
                        break
                    else:
                        self.coffee.append(append_coffee)
                        print(f'성공적으로 "{append_coffee}"가 메뉴에 추가되었습니다.')
                        break

            elif menu_choice == '2':
                print(self.latte)
                append_latte = input(f'{self.latte}를 제외하고 추가할 메뉴를 입력하세요 : ')
                for ch_la in self.latte:
                    if ch_la == append_latte:
                        print(" *** 입력하신 메뉴는 이미 있는 메뉴 입니다. ***\n"
                              " --- 기존 메뉴를 제외한 메뉴를 입력해주세요 ---")
                        break
                    else:
                        self.latte.append(append_latte)
                        print(f'성공적으로 "{append_latte}"가 메뉴에 추가되었습니다.')
                        break

            elif menu_choice == '3':
                print(self.smoothie)
                append_smoothie = input(f'{self.smoothie}를 제외하고 추가할 메뉴를 입력하세요 : ')
                for ch_smoo in self.smoothie:
                    if ch_smoo == append_smoothie:
                        print(" *** 입력하신 메뉴는 이미 있는 메뉴 입니다. ***\n"
                              " --- 기존 메뉴를 제외한 메뉴를 입력해주세요 ---")
                        break
                    else:
                        self.smoothie.append(append_smoothie)
                        print(f'성공적으로 "{append_smoothie}"가 메뉴에 추가되었습니다.')
                        break

            elif menu_choice == '4':
                print(self.tea)
                append_tea = input(f'{self.tea}를 제외하고 추가할 메뉴를 입력하세요 : ')
                for ch_te in self.tea:
                    if ch_te == append_tea:
                        print(" *** 입력하신 메뉴는 이미 있는 메뉴 입니다. ***\n"
                              " --- 기존 메뉴를 제외한 메뉴를 입력해주세요 ---")
                        break
                    else:
                        self.tea.append(append_tea)
                        print(f'성공적으로 "{append_tea}"가 메뉴에 추가되었습니다.')
                        break

            elif menu_choice == '5':
                print(self.ade)
                append_ade = input(f'{self.ade}를 제외하고 추가할 메뉴를 입력하세요 : ')
                for ch_ad in self.ade:
                    if ch_ad == append_ade:
                        print(" *** 입력하신 메뉴는 이미 있는 메뉴 입니다. ***\n"
                              " --- 기존 메뉴를 제외한 메뉴를 입력해주세요 ---")
                        break
                    else:
                        self.ade.append(append_ade)
                        print(f'성공적으로 "{append_ade}"가 메뉴에 추가되었습니다.')
                        break

            elif menu_choice == 'esc':
                break

            else:
                print(' *** "1. 커피 2. 라떼 3. 스무디 4. 티 5. 에이드" 중 다시 고르세요 *** \n'
                      ' << 나가려면 "esc"를 치세요 >> ')

    def drink_payment(self):
        print(f'고객님이 고르신 {self.drink_menu}의 가격은 {self.drink_sum}원 입니다.')
        while True:
            drink_pay = int(input('결제 금액을 입력하세요 : '))
            if drink_pay == self.drink_sum:
                print(f'성공적으로 {self.drink_menu} 결제가 완료되었습니다~')
                break
            else:
                print('*** 올바른 금액을 입력해주세요 ***')


class SideMenu(VCafe):

    # 사이드 메뉴 추가 여부 물어보기
    def add_side_menu(self):
        while True:
            add_sidemenu = input('사이드 메뉴도 드시겠습니까? yes or no : ')
            if add_sidemenu == 'yes':
                # 사이드 메뉴를 추가한다면

                # 사이드 메뉴판 보여주기
            # def show_side_menu(self):

                print('-----------<사이드 메뉴>------------\n'
                      '1. 케잌(5000)\n'
                      f'{self.cake}\n'
                      '2. 샌드위치(3000)\n'
                      f'{self.sandwich}')
                print('=' * 50)

                # 사이드 메뉴 선택하기
            # def choice_side_menu(self):
                while True:
                    choice_sidemenu = input('"1. 케잌 2. 샌드위치" 중 드실 메뉴를 고르세요 ex) 1 or 2 : ')

                    if choice_sidemenu == '1':
                        self.side_sum += 5000
                        print('=' * 50)
                        print(f'1. 케잌 (5000)\n'
                              f'{self.cake}')
                        print('=' * 50)

                        while True:
                            choice_cake = input(f'"{self.cake}" 중 원하는 케잌을 선택하세요 : ')
                            for ca in self.cake:
                                if ca == choice_cake:
                                    self.side_menu.append(choice_cake)
                                    print(self.side_menu)
                                    return self.side_sum
                                elif choice_cake == 'esc':
                                    break
                                else:  # ca != choice_side
                                    print(f' *** "{self.cake}" 중 다시 고르세요 ***\n'
                                          ' << 나가려면 "esc"를 치세요 >>')
                                    break

                    elif choice_sidemenu == '2':
                        self.side_sum += 3000
                        print('=' * 50)
                        print(f'1. 샌드위치 (3000)\n'
                              f'{self.sandwich}')
                        print('=' * 50)

                        while True:
                            choice_sandwich = input(f'"{self.sandwich}" 중 원하는 케잌을 선택하세요 : ')
                            for sand in self.sandwich:
                                if sand == choice_sandwich:
                                    self.side_menu.append(choice_sandwich)
                                    print(self.side_menu)
                                    return self.side_sum
                                elif choice_sandwich == 'esc':
                                    break
                                else:  # ca != choice_side
                                    print(f' *** "{self.sandwich}" 중 다시 고르세요 ***\n'
                                          ' << 나가려면 "esc"를 치세요 >>')
                                    break

                    elif choice_sidemenu == 'esc':
                        break

                    else:
                        print(' *** "1. 케잌 2. 샌드위치" 중 드실 메뉴를 다시 고르세요 *** \n'
                              ' << 나가려면 "esc"를 치세요 >> ')


                print(f'고객님이 고르신 {self.side_menu}의 가격은 {self.side_sum} 입니다.')
                while True:
                    side_pay = int(input('결제 금액을 입력하세요 : '))
                    if side_pay == self.side_sum:
                        print(f'성공적으로 {self.side_menu} 결제가 완료되었습니다~')
                        break
                    else:
                        print('*** 올바른 금액을 입력해주세요 ***')

            elif add_sidemenu == 'no':
                break

            else:
                print(' *** "yes, no" 중 다시 고르세요 ***')

    # def side_menu_payment(self):
    #     print(f'고객님이 고르신 {self.side_menu}의 가격은 {self.side_sum}원 입니다.')
    #     while True:
    #         side_pay = int(input('결제 금액을 입력하세요 : '))
    #         if side_pay == self.side_sum:
    #             print(f'성공적으로 {self.side_menu} 결제가 완료되었습니다~')
    #             break
    #         else:
    #             print('*** 올바른 금액을 입력해주세요 ***')

    #     print(f'총 고객님이 고르신 음료수 {self.drink_menu}와 사이드 메뉴 {self.side_menu}의 가격은 {self.drink_sum + self.side_sum} 입니다.')


# vCafe = VCafe()
# vCafe.choice_seat()
# vCafe.return_drink()

# drink = Drink()
# drink.choice_drink()

# sidemenu = SideMenu()
# sidemenu.add_side_menu()