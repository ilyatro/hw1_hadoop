#!/usr/bin python3
import sys

c_cum, m_cum, v_cum = 0, 0, 0

for line in sys.stdin:
    try:
        c, m, v = [float(x) for x in line.strip().split("\t")]
        c_cum, m_cum, v_cum = c_cum + c, (c_cum * m_cum + c * m) / (c_cum + c), (c_cum * v_cum + c * v) / (c_cum + c) + \
                              c_cum * c * ((m_cum - m) / (c_cum + c)) ** 2
    except:
        pass  # print(line)
print(c_cum, m_cum, v_cum, sep='\t')