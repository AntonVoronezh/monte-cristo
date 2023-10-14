with open('11111111111.txt') as f:
    data = f.read()

def get_chanal_data(data):
    name = data.find('a', class_='kt-widget__username')
    print(name.text)



get_chanal_data(data)