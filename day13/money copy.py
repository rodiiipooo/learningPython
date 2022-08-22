

class Money():

    def hours(summary):
        pass

    def salary(summary):
        pass


money = Money()


def money():
    answer = ""
    while answer == "":
        answer = input(
            "Will you be inputting a salary offer or an hourly wage offer?: ")
    if answer == "hourly":
        rate = ""
        hours = ""
        while rate == "" & hours == "":
            rate = int(input("What will your hourly compensation be?: "))
            hours = int(
                input("how many hours do you expect to work per week?: "))
        dailyPay, weeklyPay = rate * hours / 5, dailyPay * 5,
        summary = [(dailyPay, ), (weeklyPay, ), (monthlyPay, ), (yearlyPay, )]
        print(summary)

    else:
        rate = ""
        hours = ""
        while rate == "" & hours == "":
            rate = int(input("What will your salary compensation be?: "))
            hours = int(
                input("how many hours do you expect to work per week?: "))
        summary = [(dailyPay, ), (weeklyPay, ), (monthlyPay, ), (yearlyPay, )]
        print(summary)


money()
