# from sys import stderr
from functools import reduce
import re

def debug(*args):
    print(*args, file=stderr)

s = input()

multiples_re = ['(?={})'.format(str(i * 2019)) for i in range(200000) if i != 0]
print(multiples_re)
# multiples_re = ['(?=2019)', '(?=4038)', '(?=6057)', '(?=8076)', '(?=10095)', '(?=12114)', '(?=14133)', '(?=16152)', '(?=18171)', '(?=20190)', '(?=22209)', '(?=24228)', '(?=26247)', '(?=28266)', '(?=30285)', '(?=32304)', '(?=34323)', '(?=36342)', '(?=38361)', '(?=40380)', '(?=42399)', '(?=44418)', '(?=46437)', '(?=48456)', '(?=50475)', '(?=52494)', '(?=54513)', '(?=56532)', '(?=58551)', '(?=60570)', '(?=62589)', '(?=64608)', '(?=66627)', '(?=68646)', '(?=70665)', '(?=72684)', '(?=74703)', '(?=76722)', '(?=78741)', '(?=80760)', '(?=82779)', '(?=84798)', '(?=86817)', '(?=88836)', '(?=90855)', '(?=92874)', '(?=94893)', '(?=96912)', '(?=98931)', '(?=100950)', '(?=102969)', '(?=104988)', '(?=107007)', '(?=109026)', '(?=111045)', '(?=113064)', '(?=115083)', '(?=117102)', '(?=119121)', '(?=121140)', '(?=123159)', '(?=125178)', '(?=127197)', '(?=129216)', '(?=131235)', '(?=133254)', '(?=135273)', '(?=137292)', '(?=139311)', '(?=141330)', '(?=143349)', '(?=145368)', '(?=147387)', '(?=149406)', '(?=151425)', '(?=153444)', '(?=155463)', '(?=157482)', '(?=159501)', '(?=161520)', '(?=163539)', '(?=165558)', '(?=167577)', '(?=169596)', '(?=171615)', '(?=173634)', '(?=175653)', '(?=177672)', '(?=179691)', '(?=181710)', '(?=183729)', '(?=185748)', '(?=187767)', '(?=189786)', '(?=191805)', '(?=193824)', '(?=195843)', '(?=197862)', '(?=199881)']
result = sum(map(len, map(lambda re_pattern: re.findall(re_pattern, s), multiples_re)))

# print(result)


# echo "1817181712114" | python3 d.py && echo "14282668646" | python3 d.py && echo "2119" | python3 d.py
