"""Questão 1 - Você recebeu um arquivo chamado usuarios_feedback, nesse arquivo contém o comentário,
nome, gênero e nota de usuários referente a um produto de sua empresas. Você precisa verificar quais as
palavras que mais apareceram nos comentários:
usuarios_feedback = [{'nome':'Peter','nota':9,'genero':'M','comentario':'bom demais e agil'},
 {'nome':'Joao','nota':10,'genero':'M','comentario':'agil e eficiente'},
  {'nome':'user_not_found','nota':0,'genero':'M','comentario':'Horrível'},
   {'nome':'Marta','nota':10,'genero':'F','comentario':'muito agil bom demais'},
    {'nome':'Beatriz','nota':10,'genero':'F','comentario':'rápido e eficaz'},
     {'nome':'user_not_found','nota':2,'genero':'M','comentario':'ruim'},
      {'nome':'Jéssica','nota':10,'genero':'F','comentario':'agil'},
       {'nome':'José','nota':7,'genero':'M','comentario':'ok'},
        {'nome':'Elias','nota':5,'genero':'M','comentario':'precisa melhorar'},
         {'nome':'Miriã','nota':9,'genero':'F','comentario':'foi muito agil e rápido'},
         {'nome':'Maria','nota':10,'genero':'F','comentario':'muito bom e agil'}]"""
usuarios_feedback = [{'nome':'Peter','nota':9,'genero':'M','comentario':'bom demais e agil'},
 {'nome':'Joao','nota':10,'genero':'M','comentario':'agil e eficiente'},
  {'nome':'user_not_found','nota':0,'genero':'M','comentario':'Horrível'},
   {'nome':'Marta','nota':10,'genero':'F','comentario':'muito agil bom demais'},
    {'nome':'Beatriz','nota':10,'genero':'F','comentario':'rápido e eficaz'},
     {'nome':'user_not_found','nota':2,'genero':'M','comentario':'ruim'},
      {'nome':'Jéssica','nota':10,'genero':'F','comentario':'agil'},
       {'nome':'José','nota':7,'genero':'M','comentario':'ok'},
        {'nome':'Elias','nota':5,'genero':'M','comentario':'precisa melhorar'},
         {'nome':'Miriã','nota':9,'genero':'F','comentario':'foi muito agil e rápido'},
         {'nome':'Maria','nota':10,'genero':'F','comentario':'muito bom e agil'}]
comentarios=[]
for uf in usuarios_feedback:
 #print(usuarios_feedback)
 for k,v in uf.items():
  if k=='comentario':
   #print(f'comentario:{v}')
   comentarios.append(v)
print(comentarios)
comentarios.split(' ')


