goods = []
features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': set()}
num = 0
while True:
    control = input("For quit press 'Q', for analytics press 'A', for continue press 'Enter': ").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'Analytics:')
        for key, value in analytics.items():
            print(f'{key[:25]}: {value}')
        continue
    for f in features.keys():
        feature_ = input(f'Input feature "{f}": ')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        if (f == 'unit'):
            analytics[f].add(features[f])
        else:
            analytics[f].append(features[f])
    goods.append((num, features))
