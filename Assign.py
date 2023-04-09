# downpayment = 40,000
# closingcosts = 3,000
# Total investment =50,000
# profit 390 * 12 = 4,680



class prop_rents:
    def __init__(self, purchase_price, rent_, operating_expenses, vacancy_rate, loan_terms):
        self.purchase_price = purchase_price
        self.rent_ = rent_
        self.operating_expenses = operating_expenses
        self.vacancy_rate = vacancy_rate
        self.loan_terms = loan_terms
        self.reha_budget = {'repairscost': 7000,}
        
        self.calculate_roi()
        
    def calculate_roi(self):
        total_rent = self.rent_ * (1 - self.vacancy_rate)
        monthly_cashflow = total_rent - self.operating_expenses
        annual_cashflow = monthly_cashflow * 12
        total_cash_invested = self.purchase_price - self.loan_terms['downpayment'] + self.loan_terms['closingcosts'] + self.reha_budget ['repairscost']
        self.roi = (annual_cashflow / total_cash_invested) * 100

props = prop_rents(purchase_price=200000, 
                           rent_=2000, 
                           operating_expenses=860, 
                           vacancy_rate=0.0, 
                           loan_terms={'downpayment': 40000, 'closingcosts': 3000})

print("ROI for this property is {:.2f}%".format(props.roi))








