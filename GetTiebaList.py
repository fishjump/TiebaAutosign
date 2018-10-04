import gzip
import re
import time
from urllib import parse, request

from bs4 import BeautifulSoup as bs

import helper

if __name__ == '__main__':
    headers = helper.getHeader()
    tieba_list = []

    my_like_path = helper.getConfig('my_like')

    i = 1
    print('开始扫描贴吧...\n')
    while True:
        param = "?&pn={0}".format(i)
        req = request.Request(my_like_path + param, headers=headers)
        response = request.urlopen(req)
        page_content = gzip.decompress(response.read()).decode('gbk')
        soup = bs(page_content)
        tmp = soup.find_all(href=re.compile('.*/f\?.*'))
        if len(tmp) == 0:
            break

        for item in tmp:
            tieba_list += item.contents
            print('发现贴吧 : {0}\n'.format(item.contents[0]))
            time.sleep(helper.getConfig('delay_s'))
        i += 1

    helper.saveTiebaList(tieba_list)
    input('配置文件保存至 : {0} \n按任意键退出'.format(helper.getConfig('tieba_list')))
