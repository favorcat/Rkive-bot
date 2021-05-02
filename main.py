import twitter
import telegram
import json
import html

api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

telgm_token = ''
bot = telegram.Bot(token = telgm_token)

All_account = ['BTS_twt', 'bts_bighit', 'BTS_jp_official', 'bts_love_myself', 'Smeraldo_Books', 'INTHESOOP_TV', 'BT21_', 'BT21_Japan', 'TinyTANofficial', 'BTSW_official']
select_account = ['BIGHIT_MUSIC', 'weverseofficial', 'HYBEOFFICIALtwt', 'HYBE_LABELS_JP', 'weverseshop', 'HYBE_MERCH', 'BigHitShop', 'RhythmHive_twt', 'fila_korea', 'Coway_Global']

def find_new_tweet(account):
  with open('./media/'+account+'.json', 'r') as save_file:
    json_data = json.load(save_file)
    
  tweet = api.GetUserTimeline(screen_name=account, count=1, include_rts=True, exclude_replies=False)

  if (tweet[0].text != json_data['text']):
    save_tweet = html.unescape(tweet[0].text)
    save_url = 'https://twitter.com/'+str(tweet[0].user.screen_name)+'/status/'+str(tweet[0].id)
    sendTxt = str(tweet[0].user.name)+'님이 새로운 트윗을 올렸습니다!'+'\n\n'+save_tweet+'\n\n'+save_url
    twtSendTxt = '@'+str(tweet[0].user.screen_name)+' 님의 새 트윗\n#BTS #BTS_Butter #Rkive'+'\n'+save_url
    # 채널의 경우 chat_id = '- n'
    bot.sendMessage(chat_id = '', text=sendTxt)
    api.PostUpdate(twtSendTxt)
    
    with open('./media/'+account+'.json', 'w', encoding="utf-8") as make_file:
      for status in tweet:
        print(status, file=make_file)

# 계정 타임라인 전부 스트리밍
for i in range(len(All_account)):
    find_new_tweet(All_account[i])

# 일부 단어 포함 스트리밍
for k in range(len(select_account)):
  tweet = api.GetUserTimeline(screen_name=select_account[k], count=100, include_rts=True, exclude_replies=False)
  if ((tweet[0].text.find("BTS") != -1) or (tweet[0].text.find("방탄소년단") != -1)):
    find_new_tweet(select_account[k])