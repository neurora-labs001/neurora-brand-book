import sys, numpy as np
from PIL import Image, ImageFilter, ImageEnhance
from collections import deque
src, dst = sys.argv[1], sys.argv[2]
img = Image.open(src).convert('RGB')
im = np.asarray(img).astype(np.float32); h, w, _ = im.shape
lum = im.mean(2); sat = im.max(2) - im.min(2)
cand = (lum > 105) & (sat < 26)
reg = np.zeros((h, w), bool); q = deque()
for y in range(h):
    for x in (0, w - 1):
        if cand[y, x]: reg[y, x] = True; q.append((y, x))
for x in range(w):
    for y in (0, h - 1):
        if cand[y, x] and not reg[y, x]: reg[y, x] = True; q.append((y, x))
while q:
    y, x = q.popleft()
    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < h and 0 <= nx < w and cand[ny, nx] and not reg[ny, nx]:
            reg[ny, nx] = True; q.append((ny, nx))
m = Image.fromarray(((~reg) * 255).astype(np.uint8))
m = m.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
# keep only the largest blob (drop specks)
a = np.asarray(m) > 128
from scipy import ndimage
lab, n = ndimage.label(a)
if n > 1:
    sizes = ndimage.sum(a, lab, range(1, n + 1)); keep = lab == (1 + int(np.argmax(sizes)))
    keep = ndimage.binary_fill_holes(keep)
    m = Image.fromarray((np.minimum(np.asarray(m), keep * 255)).astype(np.uint8))
pop = ImageEnhance.Contrast(img).enhance(1.08); pop = ImageEnhance.Color(pop).enhance(1.12); pop = ImageEnhance.Sharpness(pop).enhance(1.25)
out = pop.convert('RGBA'); out.putalpha(m); out = out.crop(out.getbbox()); out.save(dst); print(dst, out.size)
