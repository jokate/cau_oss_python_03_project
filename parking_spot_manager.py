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
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)