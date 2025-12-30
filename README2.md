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

# 맨마지막 줄에 다음 내용 추가
export PATH="$HOME/miniconda3/bin:$PATH"

# 변경사항 시스템에 적용
source ~/.bashrc

# 콘다 버전 확인
conda --version

# 콘다 자동 base 환경 비활성화하고 확인
conda config --set auto_activate_base false
conda config --show auto_activate
