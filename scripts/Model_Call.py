'''

pip install transformers 
-> 토큰화를 시키기 위해서 transformers 라이브러리 인스톨필요
transfomers 안에 BertTokenizer 및 사전 훈련된 모델들이 있음

from transformers import BertTokenizer, BertModel 
-> transformer 안에 있는 BertTokenizer(토큰화를 위한도구), BertModel(사전학습된 딥러닝모델) 을 불러오는 코드

-----------------------------------------------------------------------------------------------------------------------------

tokenizer = BertTokenizer.from_pretrained('skt/kobert-base-v1') -> 사전학습된 skt에서만든 kobert모델의 -토크나이저(기본)을 불러온것
model = BertModel.from_pretrained('skt/kobert-base-v1') -> 사전 학습된 kobert모델(기본)을 불러온것

BERT 모델 특징
-> WordPiece 토크나이저를 사용 -> 새로운 단어나 희귀한 단어를 더 작은 부분 단위(부분 단어, subword)로 나누는 방식
-> "playing"이라는 단어를 -> "play"와 "##ing" 으로 나눔 -> "##"는 뒤따라오는 토큰이 단어의 중간에서 시작됨을 나타냄
-> 결과적으로 단어의 중간에서 시작되는것을 나타내는 말을 쪼개줌으로써 카테고리식 데이터셋 매칭에 적합함
-> KoBERT는 한국어를 그렇게 한것

-----------------------------------------------------------------------------------------------------------------------------
# KLUE BERT 모델 로드
tokenizer = BertTokenizer.from_pretrained('klue/bert-base') -> 사전학습된 klue 모델의 - 토크나이저(기본) 불러오기
model = BertModel.from_pretrained('klue/bert-base') -> 사전학습된 klue모델(기본)을 불러온것



'''