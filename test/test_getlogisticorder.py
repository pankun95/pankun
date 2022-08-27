import pytest
from case.api.getSession import getSession
from case.api.getlogisticorder import Get_user_members

host = 'https://backstageservices.dreawer.com'
proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888'
}
s = getSession(host=host,proxies=proxies)
members = Get_user_members(s=s,host=host,proxies=proxies)


@pytest.mark.parametrize('Authorization',"appid",['1514e1d61686438f95fa46f19070c126'],["1514e1d61686438f95fa46f19070c126"])
def getmembers(Authorization,appid):
    res = members.getusermembers(Authorization,appid)
    assert res['code']=='000000'


res1=getmembers("9bcc87d5b1974888973a850cd3d44388","1514e1d61686438f95fa46f19070c126")






