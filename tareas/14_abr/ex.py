maleta = 22 
def cot(maleta):
    if maleta < 10:
            return 0
    if maleta >= 10 and maleta <= 20:
            return 200
    if maleta > 20:
            return 500
    
res = cot(maleta)
print(res)
