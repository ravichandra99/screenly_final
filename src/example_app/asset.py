import requests,json

def get_dict(device,asset_id):
    url = 'http://usakernel.iviscloud.net:8182/ivis-kernel-server/Dignostics?action=diagnostics&type=assetdeffromscreenly&deviceId='
    r = requests.get(url + device)
    r1 = eval(r.text)
    r2 = eval(r1[0]['signal'])
    r3 = list(filter(lambda x: x['asset_id'] == asset_id, r2))
    return r3[0]

def mimetype(device,asset_id):
    data = get_dict(device,asset_id)
    return data['mimetype']

def duration(device,asset_id):
    data = get_dict(device,asset_id)
    return data['duration']


if __name__ == '__main__':
    device = 'IVISUSAA1005'
    asset_id = 'testc'
    print(mimetype(device,asset_id))
    print(duration(device,asset_id))