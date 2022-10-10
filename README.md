# DayTD

## overview
You can see the our project overview [this](https://www.notion.so/DayTD-project-e1c855fe39f84c38b74c20fa1dff0cc4) (KO)
<br>
>현대인들에게 패션은 이제 단순히 옷을 입는 것만이 아닌 자기 표현의 수단이다. 또한 거리두기가 해제되며 패션 업계 소비량은 증가했다. 날씨는 매일 바뀌고 오늘은 어떤 옷을 입을지 고민될 때 날 잘 아는 누군가가 내일 입을 옷을 매일 추천해준다면 어떨까?  DayTD는 인공지능을 이용해 날씨와 사용자의 스타일을 분석해 사용자 맞춤형 코디를 추천한다.

## demo
This is main recommendation system.
(gif이미지)
<br>
You can see the DayTD full system [here.](동영상 링크)

## requirements

- django
- django-restframework
- react
- MySQL
- tensorflow=

## dataset
We used clothes dataset from [AIHub](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100)
(public data)

We've turned this data into the category we want. So the final category is
|Final changing category name|Original provided category|
|-------|----------|
|SimpleBasic|리조트, 매니시, 모던, 클래식, 오피스|
|lovely|소피스트케이티드, 페미닌, 로맨틱|
|Sexygram|섹시|
|Unique|오리엔탈, 키치|
|Vintage|레트로, 컨트리, 히피, 웨스턴|
|Casual|스트리트, 스포티, 프레피, 힙합|
|Unisex|젠더리스, 톰보이|
|Etc|럭셔리, 아방가르드, 펑크, 밀리터리|

## AI model
- Mobilenet
  - 선정 이유: 컴퓨터 성능이 제한되거나 배터리 퍼포먼스가 중요한 곳에서 CNN 구조를 사용하기 위해 경량화된 Mobilenet 모델 사용
    - Channel Reduction, Depthwse Separable Convolutions, Distillation & Compression

## usage
```
DayTD
├── daytd_django-daytd : Backend djano code
├── :Frontend react code
