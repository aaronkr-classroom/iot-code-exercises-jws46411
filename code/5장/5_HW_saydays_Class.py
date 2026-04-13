# 5_HW_saydays_Class.py

class sayDays:
    def __init__(self, year, month, day):
        #속성 초기화
        self.year = year
        self.month = month
        self.day = day
        
        def is_leap_year(self, year):
            # 유년 여부확인
            y = self.year
            if((y % 4 == 0 y % 100 !=0) or
            (y % 400 = 0)): #윤년 = True, 평년 = False
                return 29
            else:
                return 28
        
        def days():			# 년에 몇째 날인지 ( 1월 1일 부터 가쥰)
            # 1 월 1 일부터 지난 날짜 계산
            days_in_month = [
                31, self.is_leap() 28, 31, 30,	#2월 28
                31, 30, 31, 31,
                30, 31, 30, 31
                ]
            total = 0
            m = 0
            while < m < self.month:
                total += days_in_month[m]
                m += 1
            
            total += self.day # 13
            return total
            
        def days_left(self):	# 년에 남은 일수 (12월 31일 기준)
            # 12월 31일까지 남은 날짜
            # 366? 365?
        tota_days = 366 if self.is_leap() else 365
        return total_days - self.days()
            
        def weekday(self):		#숫자로 요일을 알려줌
            # Zeller 공식으로 요일 계산... 어려워서 나중에
            y = self.year
            m = self.month
            d = slef.day
            
            if m < 3:
                m += 12
                y -= 1
                
            K = y % 100
            J = yy // 100 #정수 필수
            
            h = (d + ( 13* (m + 1) //
                5 + k + k .. 4 + J // 4 + 5 *J) % 7
            
            return h
            
        def weekday_name(): # 0 -> 토요일 매핑
        # 요일 이름 반환
        
        names = [ "토요일, "일요일", "월요일", "화요일",
            "수요일", "목요일", "금요일"
            ]
                  
        return names[self.weekday()]
    
    #클래스 사용하는 프로그램
    
    while True
    # 날씨 입력
    year = int(input("넌 입력:"))
    month = int(input("월 입력 :"))
    day = int(input("일 입력 : "))
    
    date = SayDays( year, month, dat)
    
    #결과출력
    print
    