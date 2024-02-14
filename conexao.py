import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# 1. CREATE TABLE
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# 2. INSERT
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1,"Chico",27,"Artes")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2,"Maria",30,"Medicina")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3,"Jose",20,"Administração")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4,"Lucas",26,"Estatística")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5,"Debora",31,"Letras")')

# 3. SELECT
#dados = cursor.execute('SELECT * FROM alunos')
#for alunos in dados:
#    print(alunos)

#dados = cursor.execute('SELECT nome,idade FROM alunos WHERE idade>20')
#for alunos in dados:
#    print(alunos)

#dados = cursor.execute('SELECT nome FROM alunos WHERE curso = "Letras" ORDER BY nome')
#for alunos in dados:
#    print(alunos)

#dados = cursor.execute('SELECT COUNT(*) FROM alunos')
#for alunos in dados:
#    print(alunos)

# 4. UPDATE e DELET
#cursor.execute('UPDATE alunos SET idade = 18 WHERE nome = "Chico"')
#cursor.execute('DELETE FROM alunos WHERE id=5')

# 5. 
#cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')

#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(1,"Jaqueline",25,1000)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(2,"Vinicios",27,7000)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(3,"Carla",45,9000)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(4,"Beatriz",21,2300)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(5,"Felipe",33,27300)')

# 6.
#dados = cursor.execute('SELECT nome,idade FROM clientes WHERE idade>30')
#for clientes in dados:
#    print(clientes)

#dados = cursor.execute('SELECT AVG(saldo) FROM clientes')
#for clientes in dados:
#    print(clientes)

#dados = cursor.execute('SELECT nome,saldo FROM clientes ORDER BY saldo DESC LIMIT 1')
#for clientes in dados:
#    print(clientes)

#dados = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
#for clientes in dados:
#    print(clientes)

# 7.
#cursor.execute('UPDATE clientes SET saldo = 18000 WHERE nome = "Carla"')
#cursor.execute('DELETE FROM clientes WHERE id=4')

# 8.
#cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor INT, FOREIGN KEY (cliente_id) REFERENCES clientes(id));')

#cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES(1,"Café",5.00)')
#cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES(2,"Biscoito",10.00)')
#cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES(3,"Pastel",6.99)')
#cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES(4,"Suco de laranja",4.50)')

#dados = cursor.execute('''
#    SELECT c.nome, co.produto, co.valor 
#    FROM clientes AS c 
#    JOIN compras AS co ON c.id = co.cliente_id
#''')

#for compras in dados:
#    print(compras)

# como eu tinha excluido um cliente por id, o comando acima não puxou todos os cliente_id, tive que renomear o id 5 para id 4, do nome do cliente Felipe
#cursor.execute('UPDATE clientes SET id = 4 WHERE nome = "Felipe"')

conexao.commit()
conexao.close