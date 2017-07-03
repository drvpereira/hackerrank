for _ in range(int(input())):
	n = int(input())
	passwords = list(input().split(' '))
	login_attempt = input()

	aux = login_attempt[:]

	for passwd in passwords:
		if len(aux) > 0 and login_attempt.find(passwd) != -1:
			login_attempt = login_attempt.replace(passwd, passwd + ' ')
			aux = aux.replace(passwd, '')

	if len(aux) == 0:
		print(login_attempt)
	else:
		print('WRONG PASSWORD')