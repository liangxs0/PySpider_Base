import requests
import urllib.request
def get_url(url):
   headers = {'user-agent': 'mobile'}
   req = requests.get(url, headers=headers, verify=False)
   data = req.json()
   for data in data['aweme_list']:
       name = data['desc'] or data['aweme_id']
       url = data['video']['play_addr']['url_list'][0]
       urllib.request.urlretrieve(url, filename=name + '.mp4')


if __name__ == "__main__":
   get_url('https://api.amemv.com/aweme/v1/aweme/post/?max_cursor=0&user_id=98934041906&count=20&retry_type=no_retry&mcc_mnc=46000&iid=58372527161&device_id=56750203474&ac=wifi&channel=huawei&aid=1128&app_name=aweme&version_code=421&version_name=4.2.1&device_platform=android&ssmix=a&device_type=STF-AL10&device_brand=HONOR&language=zh&os_api=26&os_version=8.0.0&uuid=866089034995361&openudid=008c22ca20dd0de5&manifest_version_code=421&resolution=1080*1920&dpi=480&update_version_code=4212&_rticket=1548080824056&ts=1548080822&js_sdk_version=1.6.4&as=a1b51dc4069b2cc6252833&cp=dab7ca5f68594861e1[wIa&mas=014a70c81a9db218501e1433b04c38963ccccc1c4cac4c6cc6c64c')