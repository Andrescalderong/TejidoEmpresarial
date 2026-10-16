"""Inserta en el DOCX los números de página calculados (a partir del PDF de LibreOffice) como resultado almacenado de los campos PAGEREF del
índice y de las listas de figuras y de tablas, de modo que Word los muestre sin actualizar campos (Word los recalcula al imprimir o al pulsar F9).
Uso: python3 18_toc_cache.py <docx> <pdf>"""
import sys, re, json, zipfile, subprocess, shutil, os
docx, pdf = sys.argv[1], sys.argv[2]
meta = json.load(open(os.path.join(os.path.dirname(docx), "toc_entradas.json")))
ids = [e["id"] for e in meta["entries"]] + [e["id"] for e in meta["figList"]] + [e["id"] for e in meta["tabList"]]
txt = subprocess.run(["pdftotext", "-f", "3", "-l", "16", "-layout", pdf, "-"], capture_output=True, text=True).stdout
lines = [re.sub(r"\s+", " ", l).strip() for l in txt.replace("\f", "\n").split("\n") if l.strip()]
SKIP = {"Contenido", "Lista de figuras", "Lista de tablas"}
logical, pend = [], False
for l in lines:
    if len(logical) >= len(ids): break                         # el índice es lo primero que aparece
    if l in SKIP: continue
    m = re.search(r"(\d{1,4})$", l)
    if re.fullmatch(r"\d{1,4}", l):
        if pend: logical.append(int(l)); pend = False      # número en línea propia tras una entrada larga
        continue                                           # si no, es el número de página del encabezado
    if m and re.search(r"[\.…]\s*\.?\s*\d{1,4}$", l): logical.append(int(m.group(1))); pend = False
    else: pend = True
print("entradas del índice leídas del PDF:", len(logical), "esperadas:", len(ids))
if len(logical) < len(ids): sys.exit("no coincide el número de entradas; no se modifica el DOCX")
pages = dict(zip(ids, logical[:len(ids)]))
tmp = docx + ".tmp"
with zipfile.ZipFile(docx) as zi, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
    for it in zi.infolist():
        data = zi.read(it.filename)
        if it.filename == "word/document.xml":
            s = data.decode("utf8")
            def rep(m):
                i = m.group(2); n = pages.get(i)
                if n is None: return m.group(0)
                return f'{m.group(1)}PAGEREF {i}</w:instrText><w:fldChar w:fldCharType="separate"/><w:t>{n}</w:t><w:fldChar w:fldCharType="end"/>'
            s, k = re.subn(r'(<w:fldChar w:fldCharType="begin" w:dirty="true"/><w:instrText xml:space="preserve">)PAGEREF (\S+?)</w:instrText><w:fldChar w:fldCharType="end"/>', rep, s)
            print("campos con resultado almacenado:", k)
            # docx-js asigna w:id="1" a todos los marcadores: se renumeran de forma única y se empareja cada fin con su inicio
            cnt = [0]; stack = []
            def bm(m):
                if m.group(1) == "Start":
                    cnt[0] += 1; stack.append(cnt[0]); return f'<w:bookmarkStart w:name="{m.group(2)}" w:id="{cnt[0]}"/>'
                return f'<w:bookmarkEnd w:id="{stack.pop() if stack else 1}"/>'
            s = re.sub(r'<w:bookmark(Start) w:name="([^"]+)" w:id="\d+"/>|<w:bookmark(End) w:id="\d+"/>', lambda m: bm(m) if m.group(1) else (f'<w:bookmarkEnd w:id="{stack.pop() if stack else 1}"/>'), s)
            print("marcadores renumerados:", cnt[0]); data = s.encode("utf8")
        zo.writestr(it, data)
shutil.move(tmp, docx)
