#coding:utf-8
from bs4 import BeautifulSoup

with open('nessus.txt','r') as f:
    html = f.read()
soup = BeautifulSoup(html,'html.parser')
lines = soup.select('.plugin-output-table .noaction')

ports = []
for line in lines:
    port = line.select('.lozenge')[0].text.split('/')[0].strip().encode('utf-8')
    ports.append(port)


ports = set(ports)

with open('ports.txt','w') as f:
    for port in ports:
		print port + ',',
		f.write(port + ',')

print '[*]Success: ports.txt'

