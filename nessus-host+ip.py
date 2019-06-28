#coding:utf-8
from bs4 import BeautifulSoup


ports = []
ips = []

with open('nessus.txt','r') as f:
    html = f.read()
soup = BeautifulSoup(html,'html.parser')
lines = soup.select('.plugin-output-table .noaction')

for line in lines:
    port=line.select('.lozenge')[0].text.split('/')[0].strip().encode('utf-8')
    ports.append(port)
    ips_data=line.select('.hosts-wrapper-hosts a')
    for i in ips_data:
        ip = i.text.rstrip(',').strip()
        ips.append(ip)

ips=list(set(ips))

with open('ip_port.txt','w') as f:
    f.write('port:\n')
    for port in ports:
        print port + ',',
        f.write(port + ',')
    print ''
    f.write('\nip:\n')
    for ip in ips:
        print ip
        f.write(ip + '\n')

print '[*]Success: result.txt'

