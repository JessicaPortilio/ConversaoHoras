def converter(hora, minuto):
	if hora == 24:
		print(f"{hora - 24}:{minuto} A.M")
	elif hora > 12:
		print(f"{hora - 12}:{minuto} P.M")
	else:
		print(f"{hora}:{minuto} A.M")


hora = 0
while True:
	hora, minuto = map(int, input().split(":"))
	if hora == -1:
		break
	#hora, minuto = input().split(":")
	converter(hora, minuto)