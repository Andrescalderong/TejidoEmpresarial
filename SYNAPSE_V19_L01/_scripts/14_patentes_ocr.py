"""OCR de las patentes de la carpeta 'Patentes ' (PDF escaneados de Lens.org) con lectura por columnas.
Modo por defecto: lectura completa (todas las páginas); con --muestreo solo portada, páginas 2-33, últimas 14 y una de cada 20.
Reanudable: omite páginas ya presentes en patentes/_ocr_texto/. Requiere rapidocr-onnxruntime y poppler (pdftoppm, pdfinfo).
Uso: RAPID_THREADS=1 python3 14_patentes_ocr.py [--muestreo] [--workers 4]   (RAPID_THREADS exige el parche local de rapidocr_onnxruntime/utils.py descrito en el README)"""
import sys, os, glob, subprocess, time
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(__file__))
from synlib import L
SRC = os.path.join(os.path.dirname(L), "Patentes "); OUT = f"{L}/patentes/_ocr_texto"; os.makedirs(OUT, exist_ok=True)
def tag(pdf):
    b = os.path.basename(pdf)[:-4].split("_"); return b[0] + b[1] + ("_" + b[2] + "_" + b[3] if b[1] == "2022" else "")
def npag(pdf): return int([l for l in subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout.split("\n") if l.startswith("Pages")][0].split()[1])
ENG = None
def work(job):
    global ENG
    pdf, pg = job; out = f"{OUT}/{tag(pdf)}_p{pg}.txt"
    if os.path.exists(out): return 0
    import cv2
    if ENG is None:
        from rapidocr_onnxruntime import RapidOCR; ENG = RapidOCR()
    base = f"/tmp/ocr_{os.getpid()}"
    subprocess.run(["pdftoppm", "-f", str(pg), "-l", str(pg), "-r", "150", "-gray", "-png", pdf, base], check=True)
    png = glob.glob(base + "-*.png")[0]; res, _ = ENG(png); W = cv2.imread(png, 0).shape[1]; lines = []
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
    tmp = out + ".tmp"; open(tmp, "w").write("\n".join(lines)); os.replace(tmp, out); os.remove(png); return 1
def paginas(n, muestreo):
    if not muestreo: return list(range(1, n + 1))
    return sorted(set([1] + list(range(2, min(n, 34)) ) + list(range(max(2, n - 13), n + 1)) + list(range(40, n - 13, 20))))
if __name__ == "__main__":
    muestreo = "--muestreo" in sys.argv; nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 4
    pdfs = sorted(glob.glob(f"{SRC}/*.pdf")); jobs = []
    for pdf in pdfs: jobs += [(pdf, p) for p in paginas(npag(pdf), muestreo) if not os.path.exists(f"{OUT}/{tag(pdf)}_p{p}.txt")]
    # intercalar patentes para que el avance sea uniforme
    import itertools, collections
    by = collections.defaultdict(list)
    for j in jobs: by[j[0]].append(j)
    jobs = [j for grp in itertools.zip_longest(*by.values()) for j in grp if j]
    print("páginas pendientes:", len(jobs), flush=True); t0 = time.time(); n = 0
    with Pool(nw) as pool:
        for r in pool.imap_unordered(work, jobs, chunksize=2):
            n += r
            if n % 50 == 0: print(f"{n}/{len(jobs)} páginas; {n/((time.time()-t0)/60):.1f} páginas/min", flush=True)
    print("DONE_FULL", flush=True)
