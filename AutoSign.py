import gzip
import time
from urllib import parse, request

import helper

if __name__ == '__main__':
    headers = helper.getHeader()
    tieba_list = helper.getTiebaList()

    sign_path = helper.getConfig('sign')

    with open(helper.getConfig('logs'), 'a') as f:
        f.write('{0}开始签到\n'.format(helper.getNow()))
        for tieba_name in tieba_list:
            data = {'ie': 'utf-8', 'kw': tieba_name}
            encoded_data = parse.urlencode(data).encode('utf-8')
            req = request.Request(
                sign_path, headers=headers, data=encoded_data)
            response = request.urlopen(req)
            result_json_str = gzip.decompress(
                response.read()).decode('unicode-escape')
            result_json_obj = helper.getJsonObj(
                result_json_str, is_from_path=False)
            if result_json_obj['no'] == 0:
                f.write('{0}{1}\t: 签到成功\n'.format(helper.getNow(), tieba_name))
            else:
                f.write('{0}{1}\t: 签到失败\t错误码 : {2}\t错误描述 : {3}\n'.format(
                    helper.getNow(), tieba_name, result_json_obj['no'], result_json_obj['error']))
            time.sleep(helper.getConfig('delay_s'))
        f.write('{0}签到完成\n'.format(helper.getNow()))
        f.close()
