# 같은 패키지에서 모듈 파일 생성
import pack.mymod1

print("tot=", pack.mymod1.tot)
import pack_other.mymod2
print(pack_other.mymod2.hap(3,7))

# 파이썬과 상관 없는 폴더에 모듈 생성
import sys
sys.path.append(r'd:/temp')
import mymod4
print('나누기는', mymod4.nanugi(12,3))

# 파이썬 설치 폴더에 Lib 폴더에 모듈 생성
import mymod3
print(mymod3.gop(3,4))