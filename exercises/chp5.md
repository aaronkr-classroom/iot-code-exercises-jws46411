3 다음 조건으로 클래스와 그 클래스를 사용하는 프로그램을 만드세요. [조건 1] 클래스 만들기
  ->

  class SayDays:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def is_leap_year(self):
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        else:
            return False

    def month_days(self):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year():
            days[1] = 29
        return days

    def days(self):
        mdays = self.month_days()
        total = 0
        for i in range(self.month - 1):
            total += mdays[i]
        total += self.day
        return total

    def days_left(self):
        if self.is_leap_year():
            return 366 - self.days()
        else:
            return 365 - self.days()

    def weekday(self):
        y = self.year
        m = self.month
        d = self.day

        if m == 1 or m == 2:
            m += 12
            y -= 1

        k = y % 100
        j = y // 100

        return (d + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7

    def weekday_name(self):
        names = ["토요일", "일요일", "월요일", "화요일", "수요일", "목요일", "금요일"]
        return names[self.weekday()]
