import twitter
import telegram
import json
import html
from datetime import datetime

api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

telgm_token = ''
bot = telegram.Bot(token = telgm_token)

All_account = ['BTS_twt', 'bts_bighit', 'BTS_jp_official', 'bts_love_myself', 'Smeraldo_Books', 'BT21_', 'BT21_Japan', 'TinyTANofficial', 'BTSW_official']
select_account = ['BIGHIT_MUSIC', 'weverseofficial', 'HYBEOFFICIALtwt', 'HYBE_LABELS_JP', 'weverseshop', 'HYBE_MERCH', 'BigHitShop', 'INTHESOOP_TV', 'RhythmHive_twt', 'fila_korea', 'Coway_Global']

# 로그
print(datetime.today().strftime("%Y.%m.%d %H:%M:%S"))

def find_new_tweet(account):
    tweet = api.GetUserTimeline(screen_name=account, count=5, include_rts=True, exclude_replies=False)
    
    with open('./media/'+account+'.json', 'r', encoding="utf-8") as save_file:
        json_data = json.load(save_file)

    save_index = 0
    for i in range(len(tweet)-1, -1, -1):
        for k in range(len(json_data)):
            if (tweet[i].text == json_data[k]['text']):
                save_index = i

    if (save_index != 0):
        for i in range(save_index):
            save_tweet = html.unescape(tweet[i].text)
            save_url = 'https://twitter.com/'+str(tweet[i].user.screen_name)+'/status/'+str(tweet[i].id)
            sendTxt = str(tweet[i].user.name)+'님이 새로운 트윗을 올렸습니다!'+'\n\n'+save_tweet+'\n\n'+save_url
            twtSendTxt = str(tweet[i].user.name)+'(@'+str(tweet[i].user.screen_name)+')님의 새 트윗'+'\n#BTS #BTS_Butter #Rkive #JIN #석진 #SUGA #윤기 #RM #남준 #JHOPE #호석 #JIMIN #지민 #V #태형 #정국 #JK'+'\n'+save_url

            # 채널의 경우 chat_id = '- n'
            bot.sendMessage(chat_id = '', text=sendTxt)
            api.PostUpdate(twtSendTxt)

            print(str(tweet[i].user.name)+'님이 새로운 트윗을 올렸습니다!')

        with open('./media/'+account+'.json', 'w', encoding="utf-8") as make_file:
            json.dump(list(map(lambda x: x.AsDict(), tweet)), make_file)

def find_BTS_new_tweet(account):
    tweet = api.GetUserTimeline(screen_name=account, count=10, include_rts=True, exclude_replies=False)
    ans = []
    for status in tweet:
        if (any(status.text.find(x) != -1 for x in ["방탄소년단", "BTS", "TinyTAN"])) :
            ans.append(status.AsDict())
        if len(ans) == 5: break

    with open('./media/'+account+'.json', 'r', encoding="utf-8") as save_file:
        json_data = json.load(save_file)

    save_index = 0
    for i in range(len(ans)-1, -1, -1):
        for k in range(len(json_data)):
            if (ans[i]['text'] == json_data[k]['text']):
                save_index = i

    if (save_index != 0):
        for i in range(save_index):
            save_tweet = html.unescape(ans[i]['text'])
            save_url = 'https://twitter.com/'+str(ans[i]['user']['screen_name'])+'/status/'+str(ans[i]['id'])
            sendTxt = str(ans[i]['user']['name'])+'님이 새로운 트윗을 올렸습니다!'+'\n\n'+save_tweet+'\n\n'+save_url
            twtSendTxt = str(ans[i]['user']['name'])+'(@'+str(ans[i]['user']['screen_name'])+')님의 새 트윗\n#BTS #BTS_Butter #Rkive #JIN #석진 #SUGA #윤기 #RM #남준 #JHOPE #호석 #JIMIN #지민 #V #태형 #정국 #JK'+'\n'+save_url

            # 채널의 경우 chat_id = '- n'
            bot.sendMessage(chat_id = '', text=sendTxt)
            api.PostUpdate(twtSendTxt)

            print(str(ans[i]['user']['name'])+'님이 새로운 트윗을 올렸습니다!')

        with open('./media/'+account+'.json', 'w', encoding="utf-8") as make_file:
            json.dump(ans, make_file)

# 계정 타임라인 전부 스트리밍
for i in range(len(All_account)):
    find_new_tweet(All_account[i])

# 일부 단어 포함 스트리밍
for k in range(len(select_account)):
    find_BTS_new_tweet(select_account[k])