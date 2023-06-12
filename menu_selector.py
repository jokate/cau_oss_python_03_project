#각 기능에 필요한 모듈 선제적 전처리로 받아오기.
import file_manager
import parking_spot_manager
def start_process(path):
    # 효율적인 코드 고려, 파일 리딩시, 최초에 한해서만 읽게 만든다.
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            #리스트를 클래스 리스트로 변경 후
            spots = parking_spot_manager.str_list_to_class_list(str_list)
            #해당 클래스에 관한 정보를 출력한다.
            parking_spot_manager.print_spots(spots)

        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                print("not implemented yet")
                # fill this block
            elif select == 2:
                keyword = input('type city:')
                print("not implemented yet")
                # fill this block
            elif select == 3:
                keyword = input('type district:')
                print("not implemented yet")
                # fill this block
            elif select == 4:
                keyword = input('type ptype:')
                print("not implemented yet")
                # fill this block
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                print("not implemented yet")
                # fill this block
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("Exit")
            exit(0)
            # fill this block
        else:
            print("invalid input")