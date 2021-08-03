import json
from collections import Counter
numMonth = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

if __name__ == '__main__':
    with open('birthdays.json', 'r') as f:
        data = json.load(f)

    months=[]

    for name, birthdaystr in data.items():
        month = birthdaystr.split('/')[0]
        months.append(numMonth[month])

    print(Counter(months))
