# print(5)
# print(-10)
# print("z"*7)
# print(5>10)
# print(not True)
# age=5
# is_adult =age>=3
# print(str(age)+"살이다."+str(is_adult))
# print(age,"살이다.",is_adult)

# station = "사당"
# print(station,"행 열차가 들어오고 있습니다.")
# print(not(5!=3))
# print((3>0)|(7>2))

# from random import *
# print(random())
# print(int(random()*10))
# print(int(random()*10)+1)
# print(randrange(1,46))
# print(randint(1,45))

# study_day = randrange(4,29)
# print('오프라인 스터디 모임 날짜는 매월',study_day,'일로 선정되었습니다.')

# print('나는 %d살입니다.'%20)
# print('%s를 좋아함'%'과자')
# print('%s %s'%('하루','이틀'))
# print('나는 {}살'.format(20))
# print('나는 {},{}'.format('빨간','파란'))

# print('나는 {age}'.format(age=23))
# age =20
# print(f'{age}')
# print("나는 \n누구일까요?")
# print('나는"누구"')
# print("나는\"누구\"")
# print("Red Apple\rPine")
# print("RedApple\rPine")

#규칙통해서 비밀번호 생성->nav5!
# site = "http://naver.com"
# print(site[:7])#http://
# print(site[site.index('.'):])#.com
# print(site[7:site.index('.')])#naver
# print(site[7:10])#nav
# print(len(site[7:site.index('.')]))#5
# print(site[7:site.index('.')].count('e'))#1
# length = len(site[7:site.index('.')])
# count = site[7:site.index('.')].count('e')
# print(site[7:10]+str(length)+str(count)+'!')

#리스트
# subway = [0,1,2]
# subway.append(3)
# print(subway)
# subway.insert(1,5)
# print(subway)
# print(subway.pop())
# print(subway)
# print(subway.count(0))
# subway.sort()
# print(subway)
# subway.reverse()
# print(subway)
# subway.clear()
# print(subway)
# num_list =[4,9]
# subway.extend(num_list)
# print(subway)

#딕셔너리
# cabinet = {3:"유재석",100:"이효리"}
# print(cabinet[3])
# print(cabinet.get(3)) 
# print(cabinet.get(5,"사용가능")) 
# print(3 in cabinet) #True
# print(cabinet)
# del cabinet[3]
# print(cabinet)
# print(cabinet.keys())
# print(cabinet.items())
# print(cabinet.values())

#튜플
# name,age,hobby = "이효리",20,"춤"
# print(name,age,hobby)

#set. 중복 안됨.순서없음
# num1 = {0,1,2,4}
# num2 = set([1,4,5])
# print(num1 & num2)
# print(num1.intersection(num2))

# print(num1 | num2)
# print(num1.union(num2))

# print(num1 - num2)
# print(num1.difference(num2))

# num2.add(0)
# print(num2)

# num1.remove(2)
# print(num1)

#자료구조변경
# menu = {"커피","주스"}
# print(menu,type(menu))

# menu = list(menu)
# print(menu,type(menu))

# menu = tuple(menu)
# print(menu,type(menu))

# menu = set(menu)
# print(menu,type(menu))

#퀴즈
# from random import * 
# comment = list(range(1,21))
# shuffle(comment)
# winners = sample(comment,4)
# chicken = winners[0]
# coffee= winners[1:]
# print('--당첨자 발표--')
# print('치킨 당첨자: {}'.format(chicken))
# print('커피 당첨자: {}'.format(coffee))
# print('--축하합니다.--')

#if문
# weather = input('오늘 날씨 어때?')
# if weather == "비" or weather =="눈":
#     print('우산필요')
# elif weather =="미세먼지":
#     print('마스크필요')
# else:
#     print('필요없음')

#for문

