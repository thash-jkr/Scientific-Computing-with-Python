class Category:

    def __init__(self, obj):
        self.obj = obj
        self.ledger = []
        self.bal = 0

    def __str__(self):
        star_left = (30 - len(self.obj)) // 2
        star_right = 30 - (star_left + len(self.obj))
        head = star_left * '*' + self.obj + star_right * '*' + '\n'
        body = ""
        for dic in self.ledger:
            descr = dic["description"]
            am = str("%.2f" % dic["amount"])
            if len(descr) > 23:
                descr = descr[:23]
            if len(am) > 7:
                am = am[:7]
            space = 30 - (len(descr) + len(am))
            body += descr + (space * " ") + am + "\n"
        body += f"Total: {self.bal}"
        return head + body

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.bal += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.bal -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.bal

    def transfer(self, amount, bud_cat):
        if self.check_funds(amount):
            with_desc = f'Transfer to {bud_cat.obj}'
            depo_desc = f'Transfer from {self.obj}'
            self.withdraw(amount, with_desc)
            bud_cat.deposit(amount, depo_desc)
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.bal >= amount:
            return True
        return False


def create_spend_chart(categories):
    items = len(categories)
    if items == 0:
        return 'No categories provided'
    chart = 'Percentage spent by category\n'
    data = list()
    lines = 0
    total = 0.00

    for cat in categories:
        if lines < len(cat.obj):
            lines = len(cat.obj)

        spent = 0.00
        for wit in cat.ledger:
            if wit['amount'] < 0:
                spent += wit['amount']
        total += spent
        data.append([cat.obj, abs(spent)])

    total = abs(total)

    for d in data:
        percent = d[1] / total * 100
        d[1] = percent

    for n in reversed(range(11)):
        n = n * 10
        num = str(n)
        line = str()
        if num == '0':
            line += ' '
        if num != '100':
            line += ' '
        line += num + '|'

        for d in data:
            if n < d[1]:
                line += ' o '
            else:
                line += '   '

        chart += line + ' \n'

    chart += '    -'
    for n in range(items):
        chart += '---'

    for n in range(lines):
        chart += '\n    '
        for d in data:
            try:
                chart += ' ' + d[0][n] + ' '
            except:
                chart += '   '
        chart += ' '

    return chart
