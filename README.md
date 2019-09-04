# kobis_open_api
영화 목록 가져오기 
http://www.kobis.or.kr/kobisopenapi/homepg/main/main.do 에서 키 발급받기 

#### How to run
```bash
$ python kobis_open_api.py [option]
```

#### Options
```bash
kobis_open_api.py
usage: kobis_open_api.py [-h] [--key KEY] [--curPage CURPAGE]
                         [--itemPerPage ITEMPERPAGE] [--movieNm MOVIENM]
                         [--directorNm DIRECTORNM] [--openStartDt OPENSTARTDT]
                         [--openEndDt OPENENDDT]
                         [--prdtStartYear PRDTSTARTYEAR]
                         [--prdtEndYear PRDTENDYEAR]
                         [--repNationCd REPNATIONCD]
                         [--movieTypeCd MOVIETYPECD]

optional arguments:
  -h, --help                      show this help message and exit
  --key KEY                       발급받은키 값을 입력
  --curPage CURPAGE               현재 페이지를 지정(default : “1”)
  --itemPerPage ITEMPERPAGE       결과 ROW 의 개수를 지정(default : “10”)
  --movieNm MOVIENM               영화명으로 조회(UTF-8 인코딩)
  --directorNm DIRECTORNM         감독명으로 조회(UTF-8 인코딩)
  --openStartDt OPENSTARTDT       YYYY형식의 조회시작 개봉연도를 입력
  --openEndDt OPENENDDT           YYYY형식의 조회종료 개봉연도를 입력
  --prdtStartYear PRDTSTARTYEAR   YYYY형식의 조회시작 제작연도를 입력
  --prdtEndYear PRDTENDYEAR       YYYY형식의 조회종료 제작연도를 입력
  --repNationCd REPNATIONCD       N개의 국적으로 조회할 수 있으며, 국적코드는 공통코드 조회 서비스에서 “2204” 로서 조회된 국적코드(default : 전체)
  --movieTypeCd MOVIETYPECD       N개의 영화유형코드로 조회할 수 있으며, 영화유형코드는 공통코드 조회 서비스에서 “2201”로서 조회된 영화유형코드(default: 전체)
```
