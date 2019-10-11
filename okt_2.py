import os
from konlpy.tag import Okt
from koalanlp.proc import SentenceSplitter, Tagger
from koalanlp import API


path_data1 = './data/type/type/'          #원래 데이터
path_data2 = './data/type/type_okt_noun_verb_adj/' #형태소 분석 후, 특정 품사인 단어들만 추출해 저장할 공간

def read_token(file_name):
    okt, tagger  = Okt(), Tagger(API.OKT)
    result = []
    with open(file_name, encoding='UTF8') as fread:
        while True:
            line = fread.readline() #한 줄씩 읽음.
            if not line: break #모두 읽으면 while문 종료.
            #line = okt.morphs(line)   #형태소 분석
              ### 품사분석기 ###
            tagged_sentence = tagger.tagSentence(line)
            paragraph = SentenceSplitter.sentencesTagged(tagged_sentence[0])

            for p in paragraph:

            tokenlist = okt.pos(p, stem=True, norm=True) # 형태소 분석 후 단어 품사 태깅
            for word in tokenlist:
                if word[1] in ["Noun","Verb", "Adjective"]:
                    result.append((word[0])) # 해당 단어를 저장함`
    return ' '.join(result)

files = [pos for pos in os.listdir(path_data1) if pos.endswith('.txt')]

for f in files:
    print(f, '파일 시작')
    tmp = read_token(os.path.join(path_data1, f))
    with open(path_data2 + f, 'a', encoding="utf-8") as file:
        file.write(tmp)
