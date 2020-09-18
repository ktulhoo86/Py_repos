#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  "add_gtnt_v2.py"
#
network = input('Введите адрес сети с префиксом(Например 10.1.1.0/30):')
number_of_mag = input('Введите номер магазина: ')
ip = network[:network.find('/')]
ip = ip.split('.')
oct1 = int(ip[0])
oct2 = int(ip[1])
oct3 = int(ip[2])
oct4 = 1 + (int(ip[3]))
oct5 = 1 + (int(oct4))
ce_ip = [str(oct1), str(oct2), str(oct3), str(oct4)]
ce_ip = '.'.join(ce_ip)
pe_ip = [str(oct1), str(oct2), str(oct3), str(oct5)]
pe_ip = '.'.join(pe_ip)

src_file_930 = '/var/share/config/rt-{}.hp-msr930.txt'.format(number_of_mag)
dest_file_930 = '/var/share/config/rt-{}.hp-msr930-gtnt.txt'.format(number_of_mag)
src_file_880 = '/var/share/config/rt-{}.cisco-880.txt'.format(number_of_mag)
dest_file_880 = '/var/share/config/rt-{}.cisco-880.txt'.format(number_of_mag)
src_file_2800 = '/var/share/config/rt-{}.cisco-2800-gtnt.txt'.format(number_of_mag)
dest_file_2800 = '/var/share/config/rt-{}.cisco-2800-gtnt.txt'.format(number_of_mag)

with open(src_file_930) as src, open(dest_file_930, 'a') as dest:
    lines = src.readlines()
    for line in lines:
        if line.startswith('ip address 10.0.0.2'):
            line = line.replace('10.0.0.2', ce_ip)
            dest.write(line)
        elif line.startswith('peer 10.0.0.1'):
            line = line.replace('10.0.0.1', pe_ip)
            dest.write(line)
        else:
            dest.write(line)

