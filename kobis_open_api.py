import json
import requests
import argparse

url_movie_base = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?"


class kobis:
    def __init__(self):
        self.movie_args = ['key', 'curPage', 'itemPerPage', 'movieNm', 'directorNm', 'openStartDt',
                           'openEndDt', 'prdtStartYear', 'prdtEndYear', 'repNationCd', 'movieTypeCd' ]

    def query_movies(self, **kwargs):
        tmp_list = []
        for k, val in kwargs.items():
            if k in self.movie_args:
                tmp_list.append("{0}={1}".format(k, val))
        return '&'.join(map(str, tmp_list))

    def make_file_name(self, **kwargs):
        tmp_list = []
        for k, val in kwargs.items():
            if k != 'key':
                tmp_list.append("{0}={1}".format(k, val))
        return '&'.join(map(str, tmp_list))

    def req(self, base, query):
        r = requests.get(base + query)
        if r.status_code == 200:
            return r.json()
        else:
            print("Error Code:" + str(r.status_code))
            print(base + query)
            return False

    def save(self, file_path, file_name, data):
        try:
            with open(file_path + file_name + '.json', 'w') as outfile:
                json.dump(data, outfile) #, ensure_ascii=False)
                print('save')
        except:
            print("save error")

def get_argument_parser():
    parser = argparse.ArgumentParser()
    # movie list
    parser.add_argument('--key',
                        help='발급받은키 값을 입력', type=str)
    parser.add_argument('--curPage',
                        help='현재 페이지를 지정(default : “1”)', type=str)
    parser.add_argument('--itemPerPage',
                        help='결과 ROW 의 개수를 지정(default : “10”)', type=str)
    parser.add_argument('--movieNm',
                        help='영화명으로 조회(UTF-8 인코딩)', type=str)
    parser.add_argument('--directorNm',
                        help='감독명으로 조회(UTF-8 인코딩)', type=str)
    parser.add_argument('--openStartDt',
                        help='YYYY형식의 조회시작 개봉연도를 입력', type=str)
    parser.add_argument('--openEndDt',
                        help='YYYY형식의 조회종료 개봉연도를 입력', type=str)
    parser.add_argument('--prdtStartYear',
                        help='YYYY형식의 조회시작 제작연도를 입력', type=str)
    parser.add_argument('--prdtEndYear',
                        help='YYYY형식의 조회종료 제작연도를 입력', type=str)
    parser.add_argument('--repNationCd',
                        help='	N개의 국적으로 조회할 수 있으며, 국적코드는 공통코드 조회 서비스에서 “2204” 로서 조회된 국적코드(default : 전체)',
                        type=str)
    parser.add_argument('--movieTypeCd',
                        help='N개의 영화유형코드로 조회할 수 있으며, 영화유형코드는 공통코드 조회 서비스에서 “2201”로서 조회된 영화유형코드(default: 전체)',
                        type=str)
    #
    return {k: v for k, v in vars(parser.parse_args()).items() if v is not None}


def main():
    k = kobis()
    args = get_argument_parser()
    qr = k.query_movies(**args)    # 입력값으로 query 생성
    movie_list = k.req(url_movie_base, qr)    # 데이터 받아오기
    k.save('./data/movie_list/', k.make_file_name(**args), movie_list)    #데이터 저장

if __name__ == '__main__':
    main()
