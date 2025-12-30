# 간단한 네크워크 패킷 스니퍼
# 차단하고 싶은 IP 설정(ACL 규칙)
# 터미널 글자 색상 지정
from pickle import REDUCE

from scapy.all import sniff, IP, TCP
import  sys

# 터미널 생상지정(ANSI Code)
# 이스케이프 시퀀스로 색상 지정 : ESC[코드m
# 8진수 33 -> 10진수 27 -> ESC, 제어명령 시작을 알림
# 91: 빨강, 92:녹색, 0:검정
# m: 색상 SGR 형식(색상,굵기,밑줄, 반전)으로 표기
RED      = "\033[91m"
GREEN    = "\033[92m"
RESET    = "\033[0m"

# 차단하고 싶은 IP 지정 (ACL)
BLOCKED_IP = "192.168.0.16"
#BLOCKED_IP = "8.8.8.8"

# 패킷이 캡쳐될때마다 호출되는 함수
def process_packet(packet):

    # 1. IP 레이어가 있는지 확인
    # 네트워크에는 IP 가 없는 패킷도 존재할 수 있음 - 주의요망!
    if packet.haslayer(IP):

        # IP 헤더에서 출발지 / 도착지 IP 주소 추출 (프로토콜 번호도 함께)
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        # 출발지 IP가 우리가 지정한 차단 IP와 같다면 경고 띄우기
        if ip_src == BLOCKED_IP:
            print(f"{RED}" + "="*50)
            print(f"[경고!!!] 차단된 IP가 감지되었습니다.")

            #TCP 계층도 있다면 포트 정보도 출력
            if packet.haslayer(TCP):
                print(f"포트벙도 : {packet[TCP].sport} -> {packet[TCP].dport} ")

            print(f"="*50 + f"{RESET}") # 색상초기화


        else:
            if packet.haslayer(TCP):
                print(f"{GREEN} [통과패킷] {ip_src} -> {ip_dst} {RESET}")



# 메인 실행 부분 - 프로그램의 시작점 (실행, 진입점)
# 현재 파일썬 파일은 직접 호출했을때만 실행되게하고
# import 했을때는 자동으로 실행되지 않게 하기 위한 코드

if __name__ == "__main__":
    print(">>> 패킷 감시를 시작합니다. (중지는 Ctrl+C)")

    # sniff 함수 호출
    # filter= 낚아챌 패킷 캡처
    # prn=process_packet: 패킷을 잡을 호출할 함수 실행
    # store=0: 잡은 패킷을 메모리에 저장하지 않음 (메모리 절약)
    #sniff(filter="ip", prn=process_packet, store=0)
    sniff(prn=process_packet, store=0)