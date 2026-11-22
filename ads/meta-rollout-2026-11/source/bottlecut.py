import sys, numpy as np
from PIL import Image, ImageFilter
src, outdir = sys.argv[1], sys.argv[2]
img = Image.open(src).convert('RGB'); a = np.asarray(img).astype(np.float32)
names = ['activate', 'focus', 'calm', 'sleep']
Y0, Y1 = 462, 1660
for k, n in enumerate(names):
    xa, xb = 330 + 350 * k, 650 + 350 * k
    L = []; R = []
    for y in range(Y0, Y1):
        row = a[y, xa:xb]; lum = row.mean(1)
        bgl = np.median(lum[:12]); bgr = np.median(lum[-12:])
        dl = np.abs(lum - bgl) > 32; dr = np.abs(lum - bgr) > 32
        l = np.argmax(dl); r = len(lum) - 1 - np.argmax(dr[::-1])
        L.append(xa + l); R.append(xa + r)
    L = np.array(L, float); R = np.array(R, float)
    # body is straight: robust constant edges from the middle, keep per-row only near the base for rounding
    lm, rm = np.median(L[100:1000]), np.median(R[100:1000])
    h = Y1 - Y0; mask = np.zeros(a.shape[:2], np.float32)
    for i, y in enumerate(range(Y0, Y1)):
        l, r = lm, rm
        if i > h - 12: inset = (i - (h - 12)); l, r = lm + inset * .9, rm - inset * .9   # rounded base
        if i < 14: inset = 14 - i; l, r = lm + inset * .6, rm - inset * .6  # rounded cap top
        mask[y, int(round(l)) + 1:int(round(r))] = 1
    # strip retouch: saturated band at the left of the label
    ly0, ly1 = 880, 1570
    band = a[ly0:ly1, int(lm):int(lm) + 70]
    sat = (band.max(2) - band.min(2)).mean(0)
    cols = np.where(sat > 0.45 * sat.max())[0]
    s0, s1 = int(lm), int(lm) + 37
    # label vertical extent inside strip region: rows whose strip colour differs from glass
    cc = a[700:1600, int((lm + rm) / 2)].mean(1); rows = np.where(cc > 150)[0] + 700
    lt, lb = rows.min(), rows.max()
    for x in range(s0 + 1, s1 + 1):
        a[lt:lb + 1, x] = np.median(a[lt + 20:lb - 20, x], axis=0)
    print(n, 'label', lt, lb)
    m = Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
    rgba = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).convert('RGBA'); rgba.putalpha(m)
    box = (int(lm) - 6, Y0 - 6, int(rm) + 6, Y1 + 6)
    rgba.crop(box).save(f'{outdir}/nr-rollon-{n}-cut.png')
    a = np.asarray(img).astype(np.float32)  # reset for next bottle
    print(n, 'edges', lm, rm, 'strip', s0, s1)
