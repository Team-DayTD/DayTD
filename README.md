# DayTD

## overview
You can see the our project overview [this](https://www.notion.so/DayTD-project-e1c855fe39f84c38b74c20fa1dff0cc4) (KO)
<br>
>현대인들에게 패션은 이제 단순히 옷을 입는 것만이 아닌 자기 표현의 수단이다. 그런 점에서 패션은 자신의 개성을 드러내는 도구이다. 최근 거리두기가 해제되며 패션 업계 소비량은 증가했다. 이런 지점에서 나를 잘 아는 누군가가 오늘의 날씨를 고려해 코디를 추천해주면 어떨까? DayTD는 인공지능 기반으로 사용자 맞춤형 코디를 제공한다. 사용자의 위치를 실시간으로 반영할 뿐만 아니라 내가 가야할 다른 지역의 날씨를 가지고도 옷코디를 추천받을 수 있다. <br/
>마음에 드는 옷은 상단부 좋아요 버튼을 눌러 내 옷장에 저장해두고 꺼내서 확인할 수 있으며 사용자가 좋아한 옷들을 기반으로 코디를 재추천한다. 좋아요 한 옷은 옷 종류 카테고리별로 나눠 확인할 수 있다. 
> 

## demo
This is main recommendation system.
<
<img src="https://user-images.githubusercontent.com/76083173/194900222-48f03b9b-71d8-43cb-b3eb-9e3ffbc14622.gif" width="600">


<br>You can see the DayTD full system [here.](https://youtu.be/HL41fkaI8M0)</br>

## requirements

- django==4.0.5
- django-restframework==3.13.1
- react==18.1.0
- sass==1.54.4
- MySQL==8.0
- tensorflow==2.0.1

## dataset
We used clothes dataset from [AIHub](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=51)
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
**Mobilenet**
- 모델 선정 이유: 컴퓨터 성능이 제한되거나 배터리 퍼포먼스가 중요한 곳에서 CNN 구조를 사용하기 위해 경량화된 Mobilenet 모델 사용
- Channel Reduction, Depthwse Separable Convolutions, Distillation & Compression
- keras 모듈에서 imagenet으로 pretrained 된 mobilenet 가져와 Fully Connected Layer에서 Feature Vector 추출

## usage
```
DayTD
├── daytd_django-daytd : Backend djano code
├── dayTD_client:Frontend react code
```

## contact
If you have any question, please sent e-mail [here](hyemin086@naver.com)
