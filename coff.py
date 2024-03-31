print("*****************************************")
print("             coffier machin              ")
print("*****************************************")

step = 0

emptyDict = {}
with open("test.txt", 'r') as infile:
    for line in infile:
        tokens = line.strip().split('=')
        fruit = tokens[0]
        number = tokens[1]
        emptyDict[fruit] = float(number)
        
tea = emptyDict["tea"]
water = emptyDict["water"]
milk = emptyDict["milk"]
coffer = emptyDict["coffer"]

es_co = 50
cup_co = 80
lat_co = 40

def make_Espresso():
    global coffer
    global water
    if coffer <0.021 or water <0.009:
        print(" the mount is not available please make another choice")
        return 1
    coffer = round(coffer - 0.021,3)
    water = round(water -0.09,3)
    print("your ordr prise is 50 Da")
    return 2
    
def make_lattee():
    global tea
    global milk
    if tea < 0.018 or milk <0.012:
        print(" the mount is not available please make another choice")
        return 1
    milk = round(milk - 0.012,3)
    tea = round(tea - 0.018,3)
    print("your ordr prise is 40 Da")
    return 2

def make_cuppocino():
    global tea
    global water
    global milk
    if tea <0.003 or water <0.012 or milk <0.015:
        print(" the mount is not available please make another choice")
        return 1
    tea = round(tea -0.003,3)
    water = round(water -0.012,3)
    milk = round(milk -0.015,3)
    print("your ordr prise is 80 Da")
    return 2

def payment(choise,many):
    global es_co 
    global cup_co 
    global lat_co
    papers = [2000,1000,500,200,100,50,20,10,5]
    back = []
    i=0
    if choise == "ESPRESSO":
        if many == es_co:
            return 0
        while i < len(papers):
            if papers[i] <= many - es_co:
                back.append(papers[i])
                many = many - papers[i]
                i -=1 
            i += 1   
        return back
        
    elif choise =="LATTEE":
        if many == lat_co:
            return 0
        while i < len(papers):
            if papers[i] <= many - lat_co:
                back.append(papers[i])
                many = many -papers[i]
                i -= 1
            i += 1
        return back
    elif choise == "CUPPOCINO":
        if many == cup_co:
            return 0
        while i < len(papers):
            if papers[i] <= many - cup_co:
                back.append(papers[i])
                many = many -papers[i]
                i-=1
            i += 1
        return back
    
def main():
    global step
    global amounts
    while step == 0:
        x  = input("do you want to start the machine (yes/no): ").upper()
        if x == "YES":
            step = 1
        elif x == "NO":
            amounts = {"tea":round(tea,2), "water":round(water,2),"milk":round(milk,2),"coffer":round(coffer,2)}
            with open("test.txt", 'w') as out:
                for amount in amounts:
                    line = amount + '=' + str(amounts[amount]) + '\n'
                    out.write(line)
            break
        else:
            print("invalid syntex")
    
        while step ==1:
            print("the current amount is : tea = {} L water = {}L milk = {}L coffer = {}L".format(tea,water,milk,coffer))
            print("press quit to go backword\n")
            y = input("what do you want to drink(Espresso , Lattee , Cuppocino: ").upper()
            if y == "ESPRESSO":
                step = make_Espresso()
            elif y == "LATTEE":
                step = make_lattee()
            elif y== "CUPPOCINO":
                step = make_cuppocino()
            elif y == "QUIT":
                step =0

        while step == 2:
            z  = int(input("please put mony : "))
            if payment(y,z)==0:
                step =0
                print("here is your drink Good day")
            elif payment(y,z) ==[]:
                print("you paid less than coast")
            elif z == 00:
                step =1
            else:
                print("give back change is {}".format(payment(y,z)))
                step =0
                print("here is your drink Good day")

if __name__ == "__main__": 
    main()
