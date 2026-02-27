class Numbers:

    def even_odd(self, start, end):
        for n in range(start, end):
            if n%2==0:
                print(f"{n} is even")
            else:
                print(f"{n} is odd")

num = Numbers()
num.even_odd(10, 20)







































































