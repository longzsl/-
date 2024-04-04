import time

from DrissionPage import WebPage
from DrissionPage.common import Actions

wp = WebPage()
#每次新打开需要用这个，然后扫码登录，并在搜索栏输入想要的内容，
# wp.get('https://www.xiaohongshu.com')
ac = Actions(wp)
wp.ele('xpath://div[@class="search-icon"]').click()
info = []
wp.listen.start(['web/v1/search/notes', 'api/sns/web/v1/feed'])

#这里定义了5条数据，想要更多直接改数字即可
for page in range(0,5):
    packet = wp.listen.wait()
    num = 0
    for i in range(0, len(wp.eles('xpath://a[@class="cover ld mask"]'))):
        temp = wp.eles('xpath://a[@class="cover ld mask"]')[i]
        if temp.attr('href') not in info:
            info.append(temp.attr('href'))
            temp.click()
            pack = wp.listen.wait()
            print(pack.response.body)
            text = pack.response.body
            wp.ele('xpath://div[@class="close close-mask-dark"]').click()
            time.sleep(1)
            num += 1
            with open('output.txt', 'a', encoding='utf-8') as file:
                file.write(text["data"]["items"][0]["note_card"]["desc"])
