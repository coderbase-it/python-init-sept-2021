import cgitb
cgitb.enable()

print('Content-type: text/html')

name = "Pierre"

print(f"""
<html>
<head> <title> Titre de la page
</title> </head>
<body>
Mon nom est {name}
</body>
</html>
""")