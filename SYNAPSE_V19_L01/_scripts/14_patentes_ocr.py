"""OCR parcial de las patentes de la carpeta 'Patentes ' (PDF escaneados de Lens.org).
Páginas leídas por patente: portada, 2-33 (hojas de dibujos), últimas 14 (reivindicaciones) y una de cada 20 entre la 40 y el inicio de las reivindicaciones.
Requiere: pip install rapidocr-onnxruntime; poppler (pdftoppm, pdfinfo). Salida: patentes/_ocr_texto/<tag>_p<n>.txt (lectura por columnas).
Uso: OMP_NUM_THREADS=1 python3 14_patentes_ocr.py  (≈15 páginas/min con 4 procesos)"""
import sys, os, re, glob, subprocess
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(__file__))
from synlib import L
SRC = os.path.join(os.path.dirname(L), "Patentes ")
OUT = f"{L}/patentes/_ocr_texto"; os.makedirs(OUT, exist_ok=True)

def tag(pdf):
    b = os.path.basename(pdf)[:-4].split("_")
    return b[0] + b[1] + ("_" + b[2] + "_" + b[3] if b[1] == "2022" else "")

def ocr_page(pdf, pg):
    out = f"{OUT}/{tag(pdf)}_p{pg}.txt"
    if os.path.exists(out): return
    from rapidocr_onnxruntime import RapidOCR
    import cv2
    global ENG
    try: ENG
    except NameError: ENG = RapidOCR()
    base = out[:-4]
    subprocess.run(["pdftoppm", "-f", str(pg), "-l", str(pg), "-r", "150", "-gray", "-png", pdf, base], check=True)
    png = glob.glob(base + "-*.png")[0]
    res, _ = ENG(png); W = cv2.imread(png, 0).shape[1]; lines = []
    if res:
        def grp(rs):
            rs = sorted(rs, key=lambda r: (r[0][0][1], r[0][0][0])); o = []; cur = None; buf = []
            for r in rs:
                y = round(r[0][0][1] / 16)
                if cur is None or y == cur: buf.append(r[1])
                else: o.append(" ".join(buf)); buf = [r[1]]
                cur = y
            if buf: o.append(" ".join(buf))
            return o
        span = [r for r in res if (r[0][1][0] - r[0][0][0]) > 0.55 * W]; rest = [r for r in res if r not in span]
        Lc = [r for r in rest if (r[0][0][0] + r[0][1][0]) / 2 < W / 2]; Rc = [r for r in rest if (r[0][0][0] + r[0][1][0]) / 2 >= W / 2]
        lines = grp(span) + ["[col 1]"] + grp(Lc) + ["[col 2]"] + grp(Rc)
    open(out, "w").write("\n".join(lines)); os.remove(png)

def paginas(pdf):
    n = int([l for l in subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout.split("\n") if l.startswith("Pages")][0].split()[1])
    return n, sorted(set([1] + list(range(2, min(n, 34))) + list(range(max(2, n - 13), n + 1)) + list(range(40, n - 13, 20))))

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "--una":
    ocr_page(sys.argv[2], int(sys.argv[3])); sys.exit()
if __name__ == "__main__":
    jobs = []
    for pdf in sorted(glob.glob(f"{SRC}/*.pdf")):
        n, pgs = paginas(pdf); jobs += [(pdf, p) for p in pgs]
    # los procesos de OCR se lanzan por separado para limitar los hilos de onnx (OMP_NUM_THREADS=1)
    with ThreadPoolExecutor(4) as ex: list(ex.map(lambda j: subprocess.run([sys.executable, __file__, "--una", j[0], str(j[1])]), jobs))
