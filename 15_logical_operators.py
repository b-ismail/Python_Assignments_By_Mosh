has_high_income = False
has_good_credit = True
has_criminal_record = True

# Logicla Operators
# and
# or
# not
if not has_criminal_record:
    if has_good_credit and has_high_income:
        print(f'Eligible for loan.')

    if has_good_credit or has_high_income:
        print(f'Eligible for loan.')