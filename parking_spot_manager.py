class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method
    def __str__(self):
        item = self.__item
        s = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

    # 생성자 함수, latitude와 longitude의 경우에는 무조건 실수로만 받아야 하므로, 입력 인자에 대해서 제한을 둬야 한다.
    def __init__(self, name, ptype, city, district, latitude: float, longitude: float):
        # 각 멤버에 관한 정보를 초기화 한다.
        self.__item = {'name': name, 'ptype': ptype, 'city': city, 'district': district, 'latitude': latitude,
                       'longitude': longitude}

    # Getter 함수, 단 해당 객체에 관해서 Key에 관한 정보만을 가져오게 한다.
    def get(self, key):
        return self.__item[key]


# 객체 리스트에 존재하는 모든 정보를 출력하는 함수를 생성.
def print_spots(spots):
    # 포맷 함수 사용, 리스트의 길이 출력
    print("---print elements({0:d})---".format(len(spots)))
    for spot in spots:
        print(spot)


# 문자열 리스트에 있는 정보를 기반으로 하여, 클래스 리스트를 만들어주는 기능을 수행한다.
def str_list_to_class_list(str_list):
    classlist = list()
    for str in str_list:
        # 각 리스트에 들어가야 하는 정보들을 파싱하는 과정 처리.
        strs = str.split(',')
        name = strs[1]
        city = strs[2]
        district = strs[3]
        ptype = strs[4]
        longitude = float(strs[5])
        latitude = float(strs[6])
        # 파싱 후, 해당 정보를 기반으로 한 객체 생성후 리스트에 append 대입
        ps = parking_spot(name, ptype, city, district, latitude, longitude)
        classlist.append(ps)
    return classlist

#필터함수 filter_by_name, filter_by_city, filter_by_district, filter_by_ptype.
#키 값에 대응하는 문자열 내부에 해당 키워드가 있는지 판단하는 로직하에 수행. (substring 파악)
def filter_by_name(spots, name):
    retlist = list()
    for spot in spots:
        if name in spot.get('name'):
            retlist.append(spot)
    return retlist
def filter_by_city(spots, city):
    retlist = list()
    for spot in spots:
        if city in spot.get('city'):
            retlist.append(spot)
    return retlist
def filter_by_district(spots, district):
    retlist = list()
    for spot in spots:
        if district in spot.get('district'):
            retlist.append(spot)
    return retlist
def filter_by_ptype(spots, ptype):
    retlist = list()
    for spot in spots:
        if ptype in spot.get('ptype'):
            retlist.append(spot)
    return retlist
#Filter by location = 2차원으로 구성된 튜플로 가져온 값에 대한 검증을 진행한 뒤 추가하는 구조.
def filter_by_location(spots, locations):
    retlist = list()

    for spot in spots:
        latitude = float(spot.get('latitude'))
        longitude = float(spot.get('longitude'))
        #Latitude에 대한 검증 시 실패하였을 경우에는 continue
        if not locations[0][0] < latitude < locations[0][1] :
            continue
        #Longitude에 대한 검증 시 실패하였을 경우 continue
        if not locations[1][0] < longitude < locations[1][1] :
            continue

        #해당 구문이 실행되는 경우는 오로지 상위 두 조건을 통과하였을 시에만 실행되게 하였음.
        retlist.append(spot)
    return retlist

#Sort by keyword 넣은 키워드에 대응하여 정렬하는 기능 추가
def sort_by_keyword(spots, keyword) :
    #파이썬 라이브러리 sorted 사용, lambda에는 정렬 기준을 따로 두었음.
    #리스트를 정렬하는 것이기 때문에 리스트의 단위가 되는 자료형은 dict가 들어가므로 key값에 대응한 값을 기준으로 정렬하는 것이 일반적임.
    #따라서 다으모가 같이 람다를 구성함.
    retlist = sorted(spots, key=lambda x: x.get(keyword), reverse= False)
    return retlist

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)

    # version#4
    #spots = sort_by_keyword(spots, 'name')
    #print_spots(spots)