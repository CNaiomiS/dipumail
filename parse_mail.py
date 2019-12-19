fp = open('diputados.txt', encoding="ISO-8859-1")	
fd = open('test.txt')
text =  fd.read()
for line in fp.readlines():
	info = line.split(';');
	last_name = info[0].split(' ')[0]
	correo = info[1]
	sexo = info[2]
	if last_name in ('Alessandri', 'Cruz-Coke','Sabat','Torrealba'):
		print(last_name)
		continue
	if sexo == 'M':
		est = 'Estimado Diputado'
	else:
		est = 'Estimada Diputada'


	intro = est + ' ' + last_name

	msg = intro +'\n\n'+ text

print(msg)

