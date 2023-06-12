#각 기능에 필요한 모듈 선제적 전처리로 받아오기.
import file_manager
import parking_spot_manager
def start_process(path):
    # 효율적인 코드 고려, 파일 리딩시, 최초에 한해서 읽게 만든다.
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    # Modify가 필요한 경우 특정 구문 내의 지역 변수가 아닌, 함수 자체 내의 지역 변수로 변경이 필요 하기에 다음과 같이 변경
    spots = parking_spot_manager.str_list_to_class_list(str_list)
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
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
                # 이름에 관한 필터 (넣은 키워드와 대조하여 포함하고 있는 경우만 리스트로 넣는다)
                spots = parking_spot_manager.filter_by_name(spots, keyword)
                # fill this block
            elif select == 2:
                keyword = input('type city:')
                # 도시에 관한 필터 (넣은 키워드와 대조하여 포함하고 있는 경우만 리스트로 넣는다)
                spots = parking_spot_manager.filter_by_city(spots, keyword)
                # fill this block
            elif select == 3:
                keyword = input('type district:')
                # 키워드에 관한 필터 (넣은 키워드와 대조하여 포함하고 있는 경우만 리스트로 넣는다)
                spots = parking_spot_manager.filter_by_district(spots, keyword)
                # fill this block
            elif select == 4:
                keyword = input('type ptype:')
                # 타입에 따른 필터 (넣은 키워드와 대조하여 포함하고 있는 경우만 리스트로 넣는다)
                spots = parking_spot_manager.filter_by_ptype(spots, keyword)
                # fill this block
            elif select == 5:
                # 위치에 관한 필터
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                # 튜플 사용. 튜플 사용 시, 2차원 튜플로 만들어, 추후 개발 시 가시성을 보이게 만들음
                locations = ((min_lat, max_lat), (min_lon, max_lon))
                # 해당 경우에 한해서 Location 튜플을 사용
                spots = parking_spot_manager.filter_by_location(spots, locations)

                # fill this block
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                #원하는 키워드에 맞는 소팅작업 가능
                spots = parking_spot_manager.sort_by_keyword(spots, keyword)
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("Exit")
            exit(0)
            # fill this block
        else:
            print("invalid input")