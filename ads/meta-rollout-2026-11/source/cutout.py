import sys, numpy as np
from PIL import Image
from collections import deque
src, dst = sys.argv[1], sys.argv[2]
im = np.asarray(Image.open(src).convert('RGB')).astype(np.float32)
h, w, _ = im.shape
lum = im.mean(2); sat = im.max(2) - im.min(2)
cand = (lum > 150) & (sat < 22)
reg = np.zeros((h, w), bool); q = deque()
for y in range(h):
    for x in (0, w - 1):
        if cand[y, x] and not reg[y, x]: reg[y, x] = True; q.append((y, x))
for x in range(w):
    for y in (0, h - 1):
        if cand[y, x] and not reg[y, x]: reg[y, x] = True; q.append((y, x))
while q:
    y, x = q.popleft()
    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < h and 0 <= nx < w and cand[ny, nx] and not reg[ny, nx]:
            reg[ny, nx] = True; q.append((ny, nx))
alpha = np.full((h, w), 255.0)
a_bg = np.clip((244 - lum) * 2.6, 0, 150); a_bg[a_bg < 10] = 0
alpha[reg] = a_bg[reg]
rgb = im.copy(); rgb[reg] = [24, 30, 48]
out = np.dstack([rgb, alpha]).astype(np.uint8)
img = Image.fromarray(out, 'RGBA'); img = img.crop(img.getbbox()); img.save(dst)
print(dst, img.size)
