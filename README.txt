Name : F0x_CheckT.py
File Size : 6981 Bytes
File MD5 : EDCC3D9E3D6D041CA205E7AE6C90E58B
File SHA1 : 337DA8C667B158C38A127B323F0FA830D88A6F0D
File SHA-256 : A6F5631241F70B73DC083B9D469C5B8E1C1C677D1115CE1317E0995D4034CA36

간단한 컴퓨터 정보와 온도를 체크할 수 있는 파이썬 스크립트입니다.
[ ! ] 동작 제대로 안되요... pythonnet.clr의 오류인지.. DLL의 버전 호환성 문제인지.. 동작이 잘 안됩니다.
백업을 목적으로 올린것이니 학습 용도로 쓰세여

# 확인 가능 한 것들...

>>> Computer Name
>>> Ip addr
>>> OS Version
>>> OS Name
>>> Processor
>>> Count of CPU core

>>> CPU Temperature, species of core..(with temperature)
>>> GPU Temperature, name, version, species of core(with temperature)
>>> HDD Temperature
>>> SSD Temperature

의존성 폴더에 들어가 있는 것들은 온도 확인에 필요한 dll 파일들입니다.
# CPUThermometerlib.dll
# OpenHardwareMonitorLib.dll

2개 전부 필요한 것인데, 첫번째 것이 x86용입니다.
개발자 Michael Moller라는 사람인데, 해당 파일을 x86버전만을 개발해서 배포했어여...ㅆㅂ
그런지라.. 32bit 운영체제에서 관리자 권한으로 f0x_CheckT를 실행하면 아마....아마? 실행 될겁니다.