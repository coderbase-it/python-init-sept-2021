import cgitb
cgitb.enable()

print('Content-type: text/html')

name = "Pierre"

print("""
<html>
<head> <title> Titre de la page
</title> </head>
<style>
h3 {color : red}
</style>
<body>
<h3> Mon nom est {name} </h3>
</body>
</html>
""")