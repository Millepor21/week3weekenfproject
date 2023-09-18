# How to calculate ROI: for $200,000 property
# Four Boxes:
# income: rental = $2,000, laundry = $0, storage = $0, misc = $0: Total Monthly Income == $2,000
# expenses: tax = $150, insurence = $100, utilities = $0, hoa = $0, lawn/snow = $0, vacancy = $100, repairs = $100, capital expenditure = $100, property manage = $200, mortgage = $860: Total Monthly Expenses == $1610
# cash flow: income = $2,000 - expenses = $1,610: Total Monthly Cashflow == $390
# Cash on Cash ROI: down payment = $40,000, closing costs = $3,000, rehab budjet = $7,000, misc other = $0, total investment = $50,000, $390 * 12 = $4,680, anual cash flow /total investment = 4680/50000 = 9.36%: Cash on Cash ROI == 9.36%

class calcRoi:

    def __init__(self,prop_income=0,prop_expenses=0,prop_cash_flow=0,cash_on_cash_roi=0,annual_cash_flow=0,total_investment=0):
        self.prop_income = prop_income
        self.prop_expenses = prop_expenses
        self.prop_cash_flow = prop_cash_flow
        self.cash_on_cash_roi = cash_on_cash_roi
        self.annual_cash_flow = annual_cash_flow
        self.total_investment = total_investment

    def income(self):
        self.prop_income = input('Please enter your total monthly income for your property in digits and whole numbers only: ')
        if self.prop_income.isdigit():
            return self.prop_income
        else:
            return print('Please enter a valid digit and whole numbers only response.')
    
    def expenses(self):
        self.prop_expenses = input('Please enter your total monthly expenses for your property in digits and whole numbers only: ')
        if self.prop_expenses.isdigit():
            return self.prop_expenses
        else:
            return print('Please enter a valid digit and whole numbers only response.')
        
    def cash_flow(self):
        self.prop_cash_flow = int(self.prop_income) - int(self.prop_expenses)
        return self.prop_cash_flow
    
    def c_on_c_roi(self):
        self.annual_cash_flow = self.prop_cash_flow * 12
        print(f'Your annual cash flow is ${self.annual_cash_flow}')
        self.total_investment = input('Please enter the total ammount of money you\'ve invested in the property in digits and whole numbers only: ')
        if self.total_investment.isdigit():    
            self.cash_on_cash_roi = self.annual_cash_flow / int(self.total_investment)
        else: 
            return print('Please enter a valid digit and whole numbers only response.')
    
    def driver(self):
        loop_choice = 'yes'
        while loop_choice == 'yes':
            loop_choice = input('\nAre you ready to input your statistics that are needed to calculate your roi? [yes] or [no]: ').lower()
            if loop_choice == 'no':
                print('Thanks for using calcRoi!')
                continue
            elif loop_choice == 'yes':
                self.income()
                self.expenses()
                print(f'Your income is ${self.prop_income} and your expenses are ${self.prop_expenses}')
                self.cash_flow()
                print(f'Your monthly cash flow is ${self.prop_cash_flow}')
                self.c_on_c_roi()
                print('\n\nYour property:')
                print('=' * 25)
                print(f'\nIncome: ${self.prop_income}\nExpenses: ${self.prop_expenses}\nMonthly Cash Flow: ${self.prop_cash_flow}\nAnnual Cash Flow: ${self.annual_cash_flow}\nTotal Investment: ${self.total_investment}\nCash on Cash ROI: {self.cash_on_cash_roi*100}%')

            else:
                print('Please input either "yes" or "no" exactly' )
                loop_choice = 'yes'
                continue

Porter = calcRoi()
Porter.driver()