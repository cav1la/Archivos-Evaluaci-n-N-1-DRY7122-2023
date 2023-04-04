aclNum = int(input("Que numero de ACL necesita? "))
if aclNum >= 1 and aclNum <= 99:
	print("Es una ACL de tipo Estandar.")
elif aclNum>=100 and aclNum <= 199:
	print("Es una ACL de tipo Extendida.")
else:
	print("El número ingresado no corresponde a una lista de acceso conocido")
