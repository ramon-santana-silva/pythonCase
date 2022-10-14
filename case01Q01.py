"""Questão 1 - Uma empresa te enviou 3 listas, uma representa a largura, outra representa a altura e
    a terceira representa a área em m2 de determinado terreno, todas estão ordenadas entretanto tem alguns
    valores faltantes que precisam ser preenchidos, preencha os valores faltantes:
    Todos os terrenos dessa empresa são retangulares e você pode utilizar a fórmula abaixo:
    a = b. h (área = largura * altura)
    Utilize as listas abaixo:
    area = [200,'null',720,1500,1000,275,'null',1200,2400,'null']
    altura = ['null',30,40,30,10,25,33,'null',12,20]
    largura = [20,20,'null',50,100,'null',30,100,200,10]"""
area = [200,'null',720,1500,1000,275,'null',1200,2400,'null']
altura = ['null',30,40,30,10,25,33,'null',12,20]
largura = [20,20,'null',50,100,'null',30,100,200,10]

for k,v in enumerate(area):
    #print(f'Na posição {k}valor: {v}')
    if v=='null':
        valor_faltante =largura[k]*altura[k]
        #print(valor_faltante)
        area.insert(k,valor_faltante)
        area.remove('null')
print(f'os valores da lista Area={area}')
print("")
for k,v in enumerate(altura):
    #print(f'Na posição {k}valor: {v}')
    if v=='null':
        valor_faltante =area[k]/largura[k]
        #print(valor_faltante)
        altura.insert(k,valor_faltante)
        altura.remove('null')
print(f'os valores da lista altura={altura}')
print("")
for k,v in enumerate(largura):
    #print(f'Na posição {k}valor: {v}')
    if v=='null':
        valor_faltante =area[k]/altura[k]
        #print(valor_faltante)
        largura.insert(k,valor_faltante)
        largura.remove('null')
print(f'os valores da lista largura={largura}')
print("")
