import requests
from case.api.loginApi import PcLogin
from case.api.getUserToken import GetUserToken
import urllib3
urllib3.disable_warnings()


class Get_user_members():
    def __init__(self,s,host,proxies=None):
        self.s=s
        self.host=host
        self.proxies=proxies
        self.url=self.host+"/cc/member/getUserMemberDetails"

    def getusermembers(self,Authorization,appid):

            data={
                "Authorization":Authorization,
                "appid":appid
            }

            res=self.s.get(url=self.url,json=data,host=self.host,proxies=self.proxies,verify=False).json()
            return res


if __name__ == "main":
    from case.api.getSession import getSession
    host='https://backstageservices.dreawer.com'
    proxies= {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    s=getSession(host,proxies)
    res=Get_user_members(s=s,host=host,proxies=proxies).getusermembers(Authorization=None,appid=None)
    print(res)














