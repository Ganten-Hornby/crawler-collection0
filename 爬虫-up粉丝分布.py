from pyquery import PyQuery as pq
from selenium import webdriver


def jsclick(css):
    js = "document.querySelector('{}').click()".format(css)
    driver.execute_script(js)


import time

cookies = [
    {
        "domain": ".bilibili.com",
        "expirationDate": 1635402473,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_uuid",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "E00BC70D-0700-DAA5-7AF8-810B0C6C504873346infoc",
        "id": 1
    },
    {
        "domain": ".bilibili.com",
        "expirationDate": 1619420870.596276,
        "hostOnly": False,
        "httpOnly": False,
        "name": "bili_jct",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "305021e0f8f9c0b37bbd728b249db6a9",
        "id": 2
    },
    {
        "domain": ".bilibili.com",
        "expirationDate": 1640526041,
        "hostOnly": False,
        "httpOnly": False,
        "name": "blackside_state",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "1",
        "id": 3
    },
    {
        "domain": ".bilibili.com",
        "expirationDate": 1611035252.579338,
        "hostOnly": False,
        "httpOnly": False,
        "name": "bp_t_offset_393467055",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "470737340590960686",
        "id": 4
    },
    {
        "domain": ".bilibili.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "bsource",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "search_google",
        "id": 5
    },
    {
        "domain": ".bilibili.com",
        "expirationDate": 1639816021,
        "hostOnly": False,
        "httpOnly": False,
        "name": "buivd_fp",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "8C63ACF5-DEF9-44C1-AF47-548AED39280D143091infoc",
        "id": 6
    },
    {
        "domain": ".bilibili.com",
        "expirationDate": 1639816021,
        "hostOnly": False,
        "httpOnly": False,
        "name": "buvid_fp_plain",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "8C63ACF5-DEF9-44C1-AF47-548AED39280D143091infoc",
        "id": 7
    },
    {
        "domain": ".bilibili.com",
        "expirationDate": 1698474473.478914,
        "hostOnly": False,
        "httpOnly": False,
        "name": "buvid3",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "8C63ACF5-DEF9-44C1-AF47-548AED39280D143091infoc",
        "id": 8
    },
    {
        "domain": ".bilibili.com",
        "expirationDate": 1640526041,
        "hostOnly": False,
        "httpOnly": False,
        "name": "CURRENT_FNVAL",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "80",
        "id": 9
    },
    {
        "domain": ".bilibili.com",
        "expirationDate": 1639821982,
        "hostOnly": False,
        "httpOnly": False,
        "name": "CURRENT_QUALITY",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "80",
        "id": 10
    },
    {
        "domain": ".bilibili.com",
        "expirationDate": 1619420870.596125,
        "hostOnly": False,
        "httpOnly": False,
        "name": "DedeUserID",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "393467055",
        "id": 11
    },
    {
        "domain": ".bilibili.com",
        "expirationDate": 1619420870.59617,
        "hostOnly": False,
        "httpOnly": False,
        "name": "DedeUserID__ckMd5",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "a67b82ae2b9da6db",
        "id": 12
    },
    {
        "domain": ".bilibili.com",
        "expirationDate": 1639816020,
        "hostOnly": False,
        "httpOnly": False,
        "name": "fingerprint",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "ebf2b4389c66080cdb73664d02839b82",
        "id": 13
    },
    {
        "domain": ".bilibili.com",
        "expirationDate": 1639816020,
        "hostOnly": False,
        "httpOnly": False,
        "name": "fingerprint_s",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "fe0df0549e745935059aee1b2982943f",
        "id": 14
    },
    {
        "domain": ".bilibili.com",
        "expirationDate": 1639816018,
        "hostOnly": False,
        "httpOnly": False,
        "name": "fingerprint3",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "673339dfd3b0ad168ae8fff7f02a2b90",
        "id": 15
    },
    {
        "domain": ".bilibili.com",
        "expirationDate": 2177452796.886681,
        "hostOnly": False,
        "httpOnly": False,
        "name": "LIVE_BUVID",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "AUTO6316041483718327",
        "id": 16
    },
    {
        "domain": ".bilibili.com",
        "expirationDate": 253402300799,
        "hostOnly": False,
        "httpOnly": False,
        "name": "PVID",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "2",
        "id": 17
    },
    {
        "domain": ".bilibili.com",
        "expirationDate": 1668121196.922811,
        "hostOnly": False,
        "httpOnly": False,
        "name": "rpdid",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "|(J|J|JmuRmm0J'uY|J)YYlR)",
        "id": 18
    },
    {
        "domain": ".bilibili.com",
        "expirationDate": 1619420870.596233,
        "hostOnly": False,
        "httpOnly": True,
        "name": "SESSDATA",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "14d22756%2C1619421873%2C631cf*a1",
        "id": 19
    },
    {
        "domain": ".bilibili.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "sid",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "5obn131u",
        "id": 20
    },
    {
        "domain": ".space.bilibili.com",
        "expirationDate": 1638375945,
        "hostOnly": False,
        "httpOnly": False,
        "name": "Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "1605347867,1606839946",
        "id": 21
    },
    {
        "domain": "space.bilibili.com",
        "hostOnly": True,
        "httpOnly": False,
        "name": "finger",
        "path": "/",
        "sameSite": "unspecified",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "-166317360",
        "id": 22
    }
]

driver = webdriver.Chrome()
# 设置隐式等待为10秒
driver.implicitly_wait(10)
# driver = webdriver.Ie()
# driver = webdriver.Edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")
driver.delete_all_cookies()
driver.get('https://space.bilibili.com/546195/fans/fans/')
# 关键点！其实简单只在这里处理即可。
for cook in cookies:
    # 遍历删除sameSite,注意，旧版chrome可能是没有samesite
    try:
        cook.pop('sameSite')
    except:
        pass
    driver.add_cookie(cook)
# for item in cook:
#    driver.add_cookie(item)
driver.get('https://space.bilibili.com/546195/fans/fans/')


# driver.get('https://space.bilibili.com/546195/fans/follow')


# driver.refresh()

def next_page():
    try:
        driver.find_element_by_partial_link_text('下一页').click()
    except:
        print('--------------no next page----------')


time.sleep(5)
with open('fans1.txt', 'w', encoding='utf-8') as f:
    f.write('B站ID\tB站空间地址\n')
    for page in range(50):
        doc = pq(driver.page_source)
        items = doc('li.clearfix').items()
        for item in items:
            print(page)
            # print(item)
            # a = item.find('.vip-name-check').text()
            # a = item.find('.vip-name-check').text()
            # print(a)
            # print(item.find('div>a.title').attr('href'))
            f.write('{}\t{}\n'.format(item.find('.vip-name-check').text(), item.find('div>a.title').attr('href')))
        time.sleep(3)
        next_page()
time.sleep(100)
# div.content > a
