def make_dict(data_str):
    dct = {}
    data_str = data_str.lstrip(' ')
    data_str = data_str.split(' ')
    for pair in data_str:
        pair = pair.split(':')
        dct[pair[0]] = pair[1]
    return dct


def check_year(y, st, en):
    if len(y) == 4:
        return check_val(y, st, en)
    return False


def check_height(h):
    unit = h[-2:]
    val = h[:-2]
    if unit == 'cm':
        return check_val(val, 150, 193)
    elif unit == 'in':
        return check_val(val, 59, 76)
    else:
        return False


def check_val(x, start, end):
    try:
        x = int(x)
        if start <= x <= end:
            return True
        else:
            return False
    except ValueError:
        return False


def check_hcl(hcl):
    if hcl[0] == '#':
        for x in hcl[1:]:
            if x not in '0123456789abcdef':
                return False
        return True
    return False


def check_ecl(ecl):
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl in colors:
        return True
    else:
        return False


def check_pid(pid):
    if len(pid) == 9:
        try:
            int(pid)
            return True
        except TypeError:
            return False
    return False


def is_pp_valid(pport, fields):
    for f in fields:
        if f not in pport:
            return False
        value = pport[f]
        if f == 'byr':
            test = check_year(value, 1920, 2002)
        elif f == 'iyr':
            test = check_year(value, 2010, 2020)
        elif f == 'eyr':
            test = check_year(value, 2020, 2030)
        elif f == 'hgt':
            test = check_height(value)
        elif f == 'hcl':
            test = check_hcl(value)
        elif f == 'ecl':
            test = check_ecl(value)
        elif f == 'pid':
            test = check_pid(value)
        else:
            test = True
        if not test:
            return False
    return True


needed_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

input_filepath = './input.txt'
passports = []
with open(input_filepath, 'r') as f_in:
    data = ''
    for line in f_in:
        line = line.strip()
        if line:
            data = data+' '+line
        else:
            passports.append(make_dict(data))
            data = ''
if data:
    passports.append(make_dict(data))

valid_pp = []
for p in passports:
    if is_pp_valid(p, needed_fields):
        valid_pp.append(p)

print(len(valid_pp))
