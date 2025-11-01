def c_to_f(temp):
    return (temp * 9/5) + 32

celsius = [0.1, 10.0, 20.0, 30.0, 40.0, 50.0]

farienheit = map(c_to_f,celsius)
for i in farienheit:
    print(i)