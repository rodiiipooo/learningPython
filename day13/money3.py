class Money():

    # def analysis(x):
    #    expenses = int(input(
    #        "how many necessary expenses do you have per month? (food/utilities/hygenics/etc): "))
    #    if expenses != 0:
    #        pass
    #    else:
    #        # function that asks amount and for what and stores said expenses
    #       pass
    #    debts = input("do you have any short or long term debts?: ")
    #    credit = input("what is your total available credit?: ")
    #    vacation = input(
    #        "would you be interested in taking vacations? (y/n): ")
    #    if vacation != 'no':
    #        # some function
    #        pass
    #    else:
    #       pass

    def earn(answer):
        print('**************************************************************************')

        if answer == "salary":
            rate = ""
            hours = ""
            while rate == "":
                rate = int(input("What will your yearly compensation be?: "))
            yearlyPay = rate
            monthlyPay = rate / 12
            weeklyPay = monthlyPay / 4
            dailyPay = weeklyPay / 5
            summary = [('daily earnings', dailyPay), ('weekly earnings', weeklyPay),
                       ('monthly earnings', monthlyPay), ('yearly earnings', yearlyPay)]
            print(
                '**************************************************************************')
            for summary in summary:
                print(summary)
            ans = input("would you like an earnings analysis? (y/n): ")
            if ans != "y":
                print("ok! Goodbye!")
            else:
                # analysis(summary)
                pass

        else:
            rate = ""
            hours = ""
            while rate == "":
                rate = int(input("What will your hourly compensation be?: "))
                hours = int(
                    input("how many hours do you expect to work per week?: "))
            dailyPay = hours / 5 * rate
            weeklyPay = dailyPay * 5
            monthlyPay = weeklyPay * 4
            yearlyPay = monthlyPay * 12
            summary = [('daily earnings', dailyPay), ('weekly earnings', weeklyPay),
                       ('monthly earnings', monthlyPay), ('yearly earnings', yearlyPay)]
            print(
                '**************************************************************************')
            for summary in summary:
                print(summary)
            ans = input("would you like an earnings analysis? (y/n): ")
            if ans != "y":
                print("ok! Goodbye!")
            else:
                # analysis(summary)
                pass


money = Money()
