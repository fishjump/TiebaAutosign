import json
import datetime

def getNow():
    return datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')

def getJsonObj(path, is_from_path = True):
    if is_from_path:
        with open(path, 'r', encoding='utf-8') as f:
            json_str = f.read()
            f.close()
            json_obj = json.loads(json_str)
            return json_obj
    else:
        json_obj = json.loads(path)
        return json_obj    


def writeJsonObj(path, json_obj):
    with open(path, 'w', encoding='utf-8') as f:
        json_str = json.dumps(json_obj, indent=4)
        f.write(json_str)
        f.close()


def saveTiebaList(tieba_list):
    writeJsonObj(getConfig('tieba_list'), tieba_list)


def getConfig(name):
    return getJsonObj(r'.\config.json')[name]


def getHeader():
    return getJsonObj(getConfig('header'))


def getTiebaList():
    return getJsonObj(getConfig('tieba_list'))
