+ 우분투에서 실행하기
+ 프로젝트 디렉토리 생성
'''
Bash
sudo mkdir ~/projectACL
cd ~/projectACL
'''
 
+ 가상환경 생성
'''
Bash
sudo apt update
sudo apt install -y python3.10-venv python3-pip

python3 -m venv py310b
source py310b/bin/activate
'''

+ scapy 패키지 설치
'''
Bash
sudo python3 -m pip install scapy
'''

+ 메인 애플리케이션
'''
Bash
sudo vi ~/projectACL/main.py
'''

+ 메인 애플리케이션 실행
'''
Bash
sudo python3 main.py
'''


### 우분투에 미니콘다 설치하기
+ 우분투에 파이썬을 설치하는 것은 다소 번거로움
+ 왜냐하면 소스를 내려받아 컴파일해야 하기 때문
+ 따라서, 미니콘다 배포파일을 다운로드해서 설치할 것을 추천 !!

''' bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-py311_25.11.1-1-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh

'''

'''bash
ubuntu@ubuntu:~$ mkdir -p ~/miniconda3
ubuntu@ubuntu:~$ wget https://repo.anaconda.com/miniconda/Miniconda3-py311_25.11.1-1-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
--2025-12-23 06:22:12--  https://repo.anaconda.com/miniconda/Miniconda3-py311_25.11.1-1-Linux-x86_64.sh
Resolving repo.anaconda.com (repo.anaconda.com)... 104.16.32.241, 104.16.191.158, 2606:4700::6810:bf9e, ...
Connecting to repo.anaconda.com (repo.anaconda.com)|104.16.32.241|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 155144821 (148M) [application/octet-stream]
Saving to: ‘/home/ubuntu/miniconda3/miniconda.sh’

/home/ubuntu/minicond 100%[========================>] 147.96M  91.0MB/s    in 1.6s

2025-12-23 06:22:14 (91.0 MB/s) - ‘/home/ubuntu/miniconda3/miniconda.sh’ saved [155144821/155144821]

ubuntu@ubuntu:~$ bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
PREFIX=/home/ubuntu/miniconda3
Unpacking bootstrapper...
Unpacking payload...

Installing base environment...

Preparing transaction: ...working... done
Executing transaction: ...working... done
installation finished.
ubuntu@ubuntu:~$
ubuntu@ubuntu:~$ rm ~/miniconda3/miniconda.sh
ubuntu@ubuntu:~$


'''

vi ~/.bashrc

### 맨마지막 줄에 다음 내용 추가
export PATH="$HOME/miniconda3/bin:$PATH"

### 변경사항 시스템에 적용
source ~/.bashrc

### 콘다 버전 확인
conda --version

### 콘다 자동 base 환경 비활성화하고 확인
conda config --set auto_activate_base false
conda config --show auto_activate


### 
'''basy 

CondaToSNonInteractiveError: Terms of Service have not been accepted for the following channels. Please accept or remove them before proceeding:
- https://repo.anaconda.com/pkgs/main
- https://repo.anaconda.com/pkgs/r

To accept these channels' Terms of Service, run the following commands:
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r

For information on safely removing channels from your conda configuration,
please see the official documentation:

    https://www.anaconda.com/docs/tools/working-with-conda/channels


### 가상환경 생성전 다음 명령 먼저 실행
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r


### 그런 다음 아래 명령으로 가상환경 생성 및 활성화
conda create -y -n py311 python=3.11
source activate py311

'''
'''bash
pip install --upgrade pip
pip install scapy

mkdir ~/projectACL
cd ~/projectACL

vi main.py
sudo ~/miniconda3/envs/py311/bin/python main.py

'''

'''bash
### py311 가상환경에서 나감
conda deactivate
'''
























