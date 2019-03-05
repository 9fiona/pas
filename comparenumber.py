"""
2019.03.04 PAS; Python Add Study 제출용 과제
num1, num2, num3는 임의의 숫자로 입력
최종 출력문
print("%d > %d > %d" % (num1, num2, num3)
클래스 생성하고
전역변수로 num1, num2, num3 선언
생성자로 num1, num2, num3를 객체생성시 매개변수로 값을 받아
크기비교하는 부분 함수 1개
출력부분 함수1개
"""


class RandomNumber:
	n1 = 0
	n2 = 0
	n3 = 0
	
	def __init__(self, num1, num2, num3):
		self.n1 = num1
		self.n2 = num2
		self.n3 = num3
	
	def num_msg(self):
		print('서로 다른 숫자 세 개(', self.n1, ', ', self.n2, ', ', self.n3, ')를 비교합니다.')


class CompareNumber(RandomNumber):
	def __init__(self, num1, num2, num3):
		self.n1 = num1
		self.n2 = num2
		self.n3 = num3
	
	def num_com(self):
		if self.n1 > self.n2:  # num1 > num2
			if self.n1 > self.n3:  # num1 > num2, num1 > num3
				if self.n2 > self.n3:  # num1 > num2 > num3
					print("%d > %d > %d" % (self.n1, self.n2, self.n3))
				else:  # num1 > num3 > num2
					print("%d > %d > %d" % (self.n1, self.n3, self.n2))
			else:  # num3 > num1 > num2
				print("%d > %sd > %d" % (self.n3, self.n1, self.n2))
		else:  # num2 > num1
			if self.n2 > self.n3:  # num2 > num3
				if self.n1 > self.n3:  # num2 > num1 > num3
					print("%d > %d > %d" % (self.n2, self.n1, self.n3))
				else:  # num2 > num3 > num1
					print("%d > %d > %d" % (self.n2, self.n3, self.n1))
			else:  # num3 > num2 > num1
				print("%d > %d > %d" % (self.n3, self.n2, self.n1))


number3 = CompareNumber(23, 54, 33)
number3.num_com()
