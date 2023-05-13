# GENERATE HTML VERSION OF TEXT FILE ##########################################################################
input = open('seeking.txt', 'r')
text = input.read()
output = open('../seeking-in-ascii.html', 'w')
output.write(f'''\
<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Jason Paul Richmond</title>

<!-- Fonts -->
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&display=swap" rel="stylesheet">

<link rel="stylesheet" href="style.css">
<body class="preContent">
  <pre>
{text}
  </pre>
</body>''')