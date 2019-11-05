## kobis_open_api
- kobis open api로 영화 목록 가져오기
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
                         [--numPages NUMPAGES]

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
  --numPages NUMPAGES             현재 페이지(curPage)로부터 몇 페이지 조회할 것인지(default="1")  
```

## postagging_for_wordvec.py
wordvector를 학습하기 위해 알맞는 형태로 만드는 파일.
1문장으로 인식된 것이 1줄에 입력 되도록 하는데 "Noun","Verb", "Adjective" 만 선택.

예시)
원본
```
첫번째 문장입니다. 데이터는 영화 줄거리입니다. 모든 장난감들이 겪는 가장 슬픈일은 바로 주인이 성장해 더이상 자신들과 놀아주지 않는 것. 우디와 버즈에게도 그 위기가 찾아온다. 앤디가 대학에 진학, 집을 떠나게 된 것. 헤어짐의 불안에 떨던 토이들은 앤디 엄마의 실수로 집을 나오게 된 이들은 우여곡절 끝에 탁아소에 기증되는 신세가 된다! 그런데 오마이갓, 어린이집 애들 장난이 아니게 난폭하고 험하다. 그리고 상상도 못했던 거대한 음모까지 숨겨져 있는 어린이집 장난감의 세계. 그러다 앤디가 여전히 자신들을 사랑한다는 사실을 알게 된 토이 군단은 앤디 곁으로 돌아가기 위해 생애 가장 큰 모험을 결심한다. 우디를 중심으로 똘똘뭉친 토이들 과연 이들의 위대한 탈출은 성공할 것인가! 깜찍발랄하지만 개인에 매몰된 세계관이라니! 미안해, 왜 널 잊었을까. 혈관이 만져지는 ‘휴먼 스토리’! 
```

적용 후
```
첫 문장 이다 
데이터 영화 줄거리 이다 
모든 장난감 겪다 가장 슬프다 일 바로 주인 성장하다 더 이상 자신 놀다 않다 것 우디 버즈 그 위기 찾아오다 
앤디 대학 진학 집 떠나다 되다 것 헤어지다 불안 떨다 토이 앤디 엄마 실수 집 나오다 되다 이 우여곡절 끝 탁아소 기증 되다 신세 되다 
오마이갓 어린이집 애 장난 아니다 난폭하다 험하다 
상상 하다 거대하다 음모 숨기다 있다 어린이집 장난감 세계 그렇다 앤디 여전하다 자신 사랑 사실 알 되다 토이 군단 앤디 곁 돌아가다 위해 생애 가장 크다 모험 결심 하다 
우디 중심 똘똘뭉친 토이 과연 이 위대하다 탈출 성공하다 것 깜찍 발랄하다 개인 매몰 되다 세계관 미안하다 왜 널 잊다 혈관 만지다 휴먼 스토리
```


## weat score.ipynb
Word Embedding Association Tests 결과  

targets 1, 2 : 일반영화, 예술영화, 독립영화, 예술독립영화 중 2개  
attributes 1, 2: '다큐멘터리','멜로로맨스','서부극(웨스턴)','범죄','뮤지컬','가족',  
              '액션','기타','공연','미스터리','성인물(에로)','스릴러','전쟁','코미디','어드벤처',  
              '공포(호러)','SF','드라마','판타지','애니메이션','사극' 중 2개
