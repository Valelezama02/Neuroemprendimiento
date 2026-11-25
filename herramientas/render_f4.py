"""F4 Editorial: página de texto en ventana redondeada, con zoom/desplazamiento y resaltado amarillo.
Uso: python3 render_f4.py config.json salida.mp4
config: {"texto": "...", "resaltes": ["frase 1", "frase 2"], "credito": "...", "duracion": 15,
         "fuente": "ruta.ttf", "tam": 58}
Sin logo ni marca de agua (regla de la cuenta).
"""
import json, sys, subprocess, os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
cfg = json.load(open(sys.argv[1])); out = sys.argv[2]
W, H, FPS = 1080, 1920, 30
DUR = cfg.get('duracion', 15)
font = ImageFont.truetype(cfg.get('fuente', os.path.join(HERE, 'brand', 'EBGaramond-Regular.ttf')), cfg.get('tam', 58))
PAPER = (239, 233, 221); INK = (28, 26, 24); YEL = (255, 222, 60)

# ---------- maquetación de la página ----------
PW, MARGIN = 1000, 55
words = cfg['texto'].split()
sp = font.getlength(' '); lh = int(font.size * 1.5)
lines, cur, curw = [], [], 0
for w in words:
    wl = font.getlength(w)
    if cur and curw + sp + wl > PW - 2 * MARGIN:
        lines.append(cur); cur, curw = [w], wl
    else:
        curw = curw + (sp if cur else 0) + wl; cur.append(w)
lines.append(cur)
PH = MARGIN * 2 + lh * len(lines)
boxes = []  # (palabra, x0, y0, x1, y1)
for li, ln in enumerate(lines):
    y = MARGIN + li * lh
    total = sum(font.getlength(w) for w in ln)
    gap = sp if li == len(lines) - 1 or len(ln) == 1 else (PW - 2 * MARGIN - total) / (len(ln) - 1)
    x = MARGIN
    for w in ln:
        wl = font.getlength(w); boxes.append((w, x, y, x + wl, y + lh)); x += wl + gap

def find(phrase):
    p = phrase.split(); n = len(p)
    norm = lambda s: s.strip('.,;:¡!¿?«»"').lower()
    for i in range(len(boxes) - n + 1):
        if all(norm(boxes[i + k][0]) == norm(p[k]) for k in range(n)):
            return list(range(i, i + n))
    raise SystemExit(f'No encontré la frase en el texto: {phrase}')
hl = [find(p) for p in cfg['resaltes']]

text_layer = Image.new('RGBA', (PW, PH), (0, 0, 0, 0))
d = ImageDraw.Draw(text_layer)
for w, x0, y0, x1, y1 in boxes:
    d.text((x0, y0 + lh * 0.12), w, font=font, fill=INK)
paper = Image.new('RGB', (PW, PH), PAPER)

def center_of(idx):
    xs = [boxes[i][1] for i in idx] + [boxes[i][3] for i in idx]
    ys = [boxes[i][2] for i in idx] + [boxes[i][4] for i in idx]
    return PW / 2, (min(ys) + max(ys)) / 2  # centrado horizontal: líneas completas a la vista

# ---------- ventana ----------
WX0, WY0, WX1, WY1, R = 60, 380, 1020, 1540, 70
WW, WH = WX1 - WX0, WY1 - WY0
mask = Image.new('L', (WW, WH), 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, WW - 1, WH - 1], R, fill=255)
shade = Image.new('L', (WW, WH), 0)
for yy in range(WH):  # oscurecer arriba/abajo para centrar la lectura
    t = abs(yy - WH / 2) / (WH / 2)
    shade.paste(int(170 * max(0, t - 0.35) / 0.65), (0, yy, WW, yy + 1))
black = Image.new('RGB', (WW, WH), (0, 0, 0))
cred_font = ImageFont.truetype(os.path.join(HERE, 'brand', 'Oswald-Medium.ttf'), 30)

# ---------- línea de tiempo ----------
ease = lambda t: 0.5 - 0.5 * math.cos(math.pi * max(0, min(1, t)))
c0 = center_of(hl[0]); c1 = center_of(hl[1]) if len(hl) > 1 else c0
wide = (PW / 2, c0[1])
# (t_inicio, t_fin, centro_ini, centro_fin, zoom_ini, zoom_fin)
keys = [(0, 2.2, wide, c0, 0.8, 0.9), (2.2, 8.0, c0, (c0[0], c0[1] + 20), 0.9, 0.94),
        (8.0, 9.4, (c0[0], c0[1] + 20), c1, 0.94, 0.9), (9.4, DUR, c1, (c1[0], c1[1] + 15), 0.9, 0.95)]
sweeps = [(2.6, 4.0, hl[0])] + ([(9.6, 11.0, hl[1])] if len(hl) > 1 else [])

def cam(t):
    for a, b, ca, cb, za, zb in keys:
        if t <= b:
            e = ease((t - a) / (b - a)); return (ca[0] + (cb[0] - ca[0]) * e, ca[1] + (cb[1] - ca[1]) * e, za + (zb - za) * e)
    return keys[-1][3][0], keys[-1][3][1], keys[-1][5]

ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS),
                       '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p',
                       '-movflags', '+faststart', out], stdin=subprocess.PIPE)
N = int(DUR * FPS)
for f in range(N):
    t = f / FPS
    page = paper.copy(); hd = ImageDraw.Draw(page)
    for a, b, idx in sweeps:
        if t < a: continue
        p = min(1, (t - a) / (b - a)); xs0 = boxes[idx[0]][1]; total = sum(boxes[i][3] - boxes[i][1] for i in idx)
        budget = p * total
        for i in idx:
            w, x0, y0, x1, y1 = boxes[i]; seg = min(budget, x1 - x0)
            if seg <= 0: break
            nxt = boxes[i + 1][1] if i + 1 in idx and boxes[i + 1][2] == y0 and seg >= x1 - x0 else x0 + seg
            hd.rectangle([x0 - 6, y0 + lh * 0.18, nxt + 6, y1 - lh * 0.08], fill=YEL)
            budget -= (x1 - x0)
    page.paste(text_layer, (0, 0), text_layer)
    cx, cy, z = cam(t)
    cw, ch = WW / z, WH / z
    box = (int(cx - cw / 2), int(cy - ch / 2), int(cx + cw / 2), int(cy + ch / 2))
    crop = page.crop(box).resize((WW, WH), Image.LANCZOS)  # fuera de la página queda negro
    crop = Image.composite(black, crop, shade)
    frame = Image.new('RGB', (W, H), (0, 0, 0)); frame.paste(crop, (WX0, WY0), mask)
    if cfg.get('credito'):
        fd = ImageDraw.Draw(frame); tw = fd.textlength(cfg['credito'], font=cred_font)
        fd.text(((W - tw) / 2, WY1 + 40), cfg['credito'], font=cred_font, fill=(200, 200, 200))
    fade = min(1, t / 0.4, (DUR - t) / 0.5)
    if fade < 1: frame = Image.blend(Image.new('RGB', (W, H)), frame, max(0, fade))
    ff.stdin.write(frame.tobytes())
ff.stdin.close(); ff.wait()
print('ok', out, DUR)
