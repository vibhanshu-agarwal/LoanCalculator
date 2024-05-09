import argparse
import math

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        print("Incorrect parameters")
        exit(0)
def calculate_differentiated_payments(principal, periods, interest, payment):
    if payment is not None or interest is None or principal is None or periods is None:
        print("Incorrect parameters")
    elif principal < 0 or periods < 0 or interest < 0:
        print("Incorrect parameters")
    else:
        i = interest / 100 / 12
        total_overpayment = 0

        for month in range(1, periods + 1):
            D_m = principal / periods + i * (principal - principal * (month - 1) / periods)
            print(f"Month {month}: payment is {math.ceil(D_m)}")
            total_overpayment += math.ceil(D_m) - (principal / periods)

        print(f"\nOverpayment = {math.ceil(total_overpayment)}")


def calculate_annuity_payment(principal, periods, interest, payment):
    if interest is None:
        print("Incorrect parameters")
    elif (principal is not None and principal < 0) or (periods is not None and periods < 0) or interest < 0 or (
            payment is not None and payment < 0):
        print("Incorrect parameters")
    else:
        i = interest / 100 / 12
        if periods is None:
            n = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
            years = n // 12
            months = n % 12
            if years == 0:
                print(f"It will take {months} months to repay this loan!")
            elif years == 1 and months == 0:
                print(f"It will take 1 year to repay this loan!")
            elif years == 1:
                print(f"It will take 1 year and {months} months to repay this loan!")
            elif months == 0:
                print(f"It will take {years} years to repay this loan!")
            else:
                print(f"It will take {years} years and {months} months to repay this loan!")
            periods = math.ceil(years * 12 + months)
            # annuity_payment = math.ceil(principal * (i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
            # overpayment = math.ceil(annuity_payment * periods - principal)
            overpayment = int(payment * periods - principal)
            print(f"Overpayment = {overpayment}")
        elif principal is None:
            principal = payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
            annuity_payment = math.ceil(principal * (i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
            overpayment = math.ceil(annuity_payment * periods - principal)
            print(f"Your loan principal = {principal}")
            print(f"Overpayment = {overpayment}")
        else:
            annuity_payment = math.ceil(principal * (i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
            overpayment = math.ceil(annuity_payment * periods - principal)
            print(f"Your annuity payment = {annuity_payment}")
            print(f"Overpayment = {overpayment}")



def main():
    # parser = argparse.ArgumentParser(description="Loan calculator")
    parser = CustomArgumentParser()
    parser.add_argument("--type", choices=["annuity", "diff"], required=True,
                        help="Type of payment: 'annuity' or 'diff'")
    parser.add_argument("--principal", type=float, help="Loan principal")
    parser.add_argument("--payment", type=float, help="Monthly payment")
    parser.add_argument("--periods", type=int, help="Number of payments (months)")
    parser.add_argument("--interest", type=float, help="Annual interest rate (in percentage)")

    args = parser.parse_args()

    if args.type == "diff":
        calculate_differentiated_payments(args.principal, args.periods, args.interest, args.payment)
    elif args.type == "annuity":
        calculate_annuity_payment(args.principal, args.periods, args.interest, args.payment)
    else:
        print("Incorrect parameters.")


if __name__ == "__main__":
    main()
