import twitter
import json
from datetime import datetime

api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

All_account = ['BTS_twt', 'bts_bighit', 'BTS_jp_official', 'bts_love_myself', 'Smeraldo_Books', 'INTHESOOP_TV', 'BT21_', 'BT21_Japan', 'TinyTANofficial', 'BTSW_official']
select_account = ['BIGHIT_MUSIC', 'weverseofficial', 'HYBEOFFICIALtwt', 'HYBE_LABELS_JP', 'weverseshop', 'HYBE_MERCH', 'BigHitShop', 'RhythmHive_twt', 'fila_korea', 'Coway_Global']

# 로그
print(datetime.today().strftime("%Y.%m.%d %H:%M:%S"))

for i in range(len(All_account)):
    tweet = api.GetUserTimeline(screen_name=All_account[i], count=5, include_rts=True, exclude_replies=False)
    with open('./media/'+All_account[i]+'.json', 'w', encoding="utf-8") as make_file:
        json.dump(list(map(lambda x: x.AsDict(), tweet)), make_file)

for k in range(len(select_account)):
    tweet = api.GetUserTimeline(screen_name=select_account[k], count=100, include_rts=True, exclude_replies=False)
    ans = []
    for status in tweet:
        if (any(status.text.find(x) != -1 for x in ["방탄소년단", "BTS", "TinyTAN"])) :
            ans.append(status.AsDict())
        if len(ans) == 5: break
    with open('./media/'+select_account[k]+'.json', 'w', encoding="utf-8") as make_file:
        json.dump(ans, make_file)