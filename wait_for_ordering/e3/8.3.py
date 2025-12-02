Sale2019=[['华为',34.3], ['vivo',18.5],['OPPO',18.6], ['小米',12.3], ['Apple',8.6],['魅族',1.8], ['三星',1.5], ['联想',0.8], ['中兴',0.6]]

Sale2018=[['华为',30.5], ['vivo',19.1],['OPPO',19.5], ['小米',12.3], ['Apple',13.5],['魅族',2.4], ['三星',1.5], ['金立',1.2]]

Sale2019Dic=dict(Sale2019)

Sale2018Dic=dict(Sale2018)
SaleKey=set(Sale2019Dic.keys()-Sale2018Dic.keys())

print(SaleKey)