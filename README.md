# Rkive-bot
### [Rkive.cloud](https://www.rkive.cloud)의 알림 봇 (Telegram / Twitter)
방탄소년단과 관련된 공식 계정들의 새로운 트윗이 올라올 때 알림을 받을 수 있다.    

### 사용 전 설치해야 할 모듈
```
pip3 install python-twitter
pip3 install python-telegram-bot
```

해당 봇은 트위터 계정의 전체 트윗을 불러오거나, 특정 단어가 들어간 트윗을 올린 것을 가져와 알림 해 준다.    
굳이 트위터에 계정 알림 설정이 있는데 왜 쓰냐고 묻는다면,    
현재 방탄소년단의 소속사인 HYBE의 관리하에 있는 타 아이돌이 많아,    
알림 설정을 하면 방탄소년단과 관련된 트윗 외에도 알림 받기 때문이다.

#### 전체 트윗을 알림 받을 수 있는 계정
> BTS_twt    
bts_bighit    
BTS_jp_official    
bts_love_myself    
Smeraldo_Books    
INTHESOOP_TV    
BT21_    
BT21_Japan    
TinyTANofficial    
BTSW_official

#### BTS와 관련된 트윗만 알림 받을 수 있는 계정
> BIGHIT_MUSIC    
weverseofficial    
HYBEOFFICIALtwt    
HYBE_LABELS_JP    
weverseshop    
HYBE_MERCH    
BigHitShop    
RhythmHive_twt


### 비어있는 json파일에 트윗 불러오기
트윗 알림 봇을 사용하기 전에, 해당 계정의 최신 게시글에 대한 `json`파일이 있어야 한다.    
우선 해당 계정 아이디로 된 `json`파일을 만든다. (ex. `BTS_twt.json`)    
이때, 아이디의 대소문자를 구분해 주어야 한다.    
빈 `json`파일을 채워주기 위해서 다음과 같은 코드를 실행시켜 `json`파일에 내용을 작성해 주면 된다.

#### 모든 트윗을 불러오는 계정의 경우,
``` python
# 계정이 여러 개인 경우, 계정의 id를 list로 만든 후 반복문을 돌리면 된다.
for i in range(len(All_account)):
    tweet = api.GetUserTimeline(screen_name=All_account[i], count=1, include_rts=True, exclude_replies=False)
    with open('./media/'+All_account[i]+'.json', 'w', encoding="utf-8") as make_file:
        print(tweet[0], file=make_file)
```
#### 일부 트윗을 불러오는 계정의 경우,
``` python
for k in range(len(select_account)):
  tweet = api.GetUserTimeline(screen_name=select_account[k], count=100, include_rts=True, exclude_replies=False)
  flag = True
  j = 0
  while (flag == True):
    if ((tweet[j].text.find("BTS") != -1) or (tweet[j].text.find("방탄소년단") != -1)):
      with open('./media/'+select_account[k]+'.json', 'w', encoding="utf-8") as make_file:
        print(tweet[j], file=make_file)
      flag = False
    j += 1
```

### crontab 에서 파일의 경로를 찾을 수 없다고 로그가 뜰 때
에러 메세지
```
FileNotFoundError: [Errno 2] No such file or directory: './media/BTS_twt.json'
```
`./media/~`의 경로를 절대경로로 바꿔 주면 제대로 실행이 된다.