#coding:utf-8
from bs4 import BeautifulSoup

def get_one_port_ips(ips_data):
    ips = []
    for i in ips_data:
        ip = i.text.rstrip(',').strip()
        ips.append(ip)
    return ips
datas = []
with open('nessus.txt','r') as f:
    html = f.read()
soup = BeautifulSoup(html,'html.parser')
lines = soup.select('.plugin-output-table .noaction')
#print lines[0].select('.hide.mHide')[0].text.strip()
#one_port_ips_data = lines[0].select('.hosts-wrapper-hosts a')
for line in lines:
    data = {
        'port':line.select('.lozenge')[0].text.split('/')[0].strip().encode('utf-8'),
        'ips' : get_one_port_ips(line.select('.hosts-wrapper-hosts a'))
    }
    datas.append(data)

with open('result.txt','w') as f:
    for data in datas:
        for ip in data['ips']:
            info = ip + ':' + data['port']
            print info
            f.write(info + '\n')

print '[*]Success: result.txt'

