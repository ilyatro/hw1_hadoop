#!/usr/bin python3
import sys
import csv
header = sys.stdin.readline()
c_cum, m_cum, v_cum = 0, 0, 0
for line in sys.stdin:
    try:
        price = float(list(csv.reader([line]))[0][9])
        c, m, v = 1, price, 0
        c_cum, m_cum, v_cum = c_cum + c, (c_cum * m_cum + c * m) / (c_cum + c), (c_cum * v_cum + c * v) / (
                    c_cum + c) + c_cum * c * ((m_cum - m) / (c_cum + c)) ** 2
    except:
        pass  # print(line)
print(c_cum, m_cum, v_cum, sep='\t')