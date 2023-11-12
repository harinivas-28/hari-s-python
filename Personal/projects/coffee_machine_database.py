data={
    'Latte':{
        'Milk':300,
        'water':50,
        'powder':100,
        'Cost':270
    },
    'Expresso':{
        'Milk':250,
        'water':50,
        'powder':75,
        'Cost':220
    },
    'Cappucino':{
        'Milk':230,
        'water':70,
        'powder':70,
        'Cost':190
    }
}
machine_data={
    'Milk':550,
    'water':120,
    'powder':145,
}
Rupees={
    '5 Rs':0,
    '10 Rs':0,
    '20 Rs':0
}
def total_balance():
    balance=0
    for i in Rupees:
        if i=='5 Rs':
            balance+=5*Rupees[i]
        elif i=='10 Rs':
            balance+=10*Rupees[i]
        elif i=='20 Rs':
            balance+=20*Rupees[i]
    return balance
