# scapy
# 파이썬 기반 강력한 패킷 조작 라이블러리(패킷 스니퍼/분석도구)
# 네트워크 패킷을 캡쳐, 생성, 수정, 전송, 분석 할 수 있음
from itertools import count

# 본 프로젝트의 주제
# 패킷 스니핑 & 필터링 및 로드 분석 구현
# 네트워크에 흐르는 패킷을 실시간으로 켭쳐하고 조건에 따라 필터링
# 조건 (특정 IP, 포트, 프로토콜)에 따라 필터링 [나중에 + 로그기능 + 전송]

from scapy.all import sniff
from scapy.all import IP, ICMP, send

sniff(count = 5)

# tcp만 츨력
#sniff(filter="tcp", prn=lambda x: print(x))

# 패킷 5개 캡쳐후 출력
#sniff(filter="tcp",count = 5, prn=lambda x: print(x))

from scapy.all import IP, ICMP, send

#ICMP 패킷 하나 생성하고 전송
packet = IP(dst='8.8.8.8') / ICMP()

for _ in range(1):
    send(packet)

# 패킷 구조 확인
packet.show()
