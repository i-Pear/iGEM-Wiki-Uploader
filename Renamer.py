import os

a = []
b = []
c = []
jscss = []

mathjs = ""
with open(r"D:\mathjs.txt") as file:
    lines = file.readlines()
    for i in lines:
        mathjs = mathjs + i

with open(r"C:\Users\ipear\Desktop\c.txt") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        c.append(lines[i][:-1])

with open(r"C:\Users\ipear\Desktop\jscss.txt") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        jscss.append(lines[i][:-1])

with open(r"C:\Users\ipear\Desktop\out.txt") as file:
    lines = file.readlines()
    for i in range(len(lines) // 2):
        a.append(lines[i * 2][:-1])
        b.append(lines[i * 2 + 1][:-1])

a.append("<head>")
b.append(
    '<head>' + '\n' + '<script src="https://2019.igem.org/Team:NEU_CHINA/pos-js?action=raw&ctype=text/javascript"> </script>')

for root, dirs, files in os.walk("G:\igem_page2"):
    for file in files:

        # !!! Ignoring all except html
        #if not file.endswith(".html"):
        #    continue

        if not (file.endswith(".css") or file.endswith(".html") or file.endswith(".js")):
            continue

        print("Running on " + file)
        path = os.path.join(root, file)
        with open(path, encoding='utf-8') as filex:
            lines = filex.readlines()

        for i in range(len(lines)):

            for j in range(len(c)):
                lines[i] = lines[i].replace(c[j], '')
            for j in range(len(a)):
                lines[i] = lines[i].replace(a[j], b[j])
            for j in range(len(jscss)):
                if jscss[j].endswith(".js"):
                    lines[i] = lines[i].replace(jscss[j], (jscss[j]).replace('.', '-')[
                                                          :-3] + "-js?action=raw&ctype=text/javascript")
                else:
                    lines[i] = lines[i].replace(jscss[j],
                                                (jscss[j]).replace('.', '-')[:-4] + "-css?action=raw&ctype=text/css")
            lines[i] = lines[i].replace("<p", "<div")
            lines[i] = lines[i].replace("/p>", "/div>")
            lines[i] = lines[i].replace("</body>", mathjs)

        with open(path, "w", encoding='utf-8') as filex:
            filex.writelines(lines)

        if file.endswith(".css"):
            os.rename(path, path.replace('.', '-')[:-4] + "-css")
        if file.endswith(".js"):
            os.rename(path, path.replace('.', '-')[:-3] + "-js")
