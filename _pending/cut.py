import sys,numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as ndi
U='/mnt/user-data/uploads/'
sets=[('cosmos','7c840b76',.80),('scarab','06206afa',.80),('elem','613be246',.80),('neonx','21a8f5c5',1),('micro','e94dd428',.70),('orrery','29bea53a',.84),('smile','1468fd21',1),('zakh','d3e8e5d7',1),('yaqut','45cf98df',1),('crown','655c2165',1)]
S=Image.new('RGB',(4*130,10*130),'#3a0f1c')
for row,(k,f,inner) in enumerate(sets):
    im=Image.open(U+f+'-image.jpg').convert('RGB'); a=np.asarray(im).astype(int)
    bgc=np.median(np.concatenate([a[:8].reshape(-1,3),a[-8:].reshape(-1,3)]),0)
    fg=(np.abs(a-bgc).max(-1)>45); fg=ndi.binary_opening(fg,np.ones((5,5)))
    col=fg.sum(0)>fg.shape[0]*.08
    runs=[];x=0
    while x<len(col):
        if col[x]:
            x0=x
            while x<len(col) and col[x]: x+=1
            if x-x0>40: runs.append((x0,x))
        x+=1
    assert len(runs)==4,(k,runs)
    for j,((x0,x1),c) in enumerate(zip(runs,'rgyb')):
        sub=fg[:,x0:x1]; ys=np.where(sub.any(1))[0]
        R=(x1-x0)/2; cx=(x0+x1)/2; cy=ys.min()+R
        r=R*inner*0.97
        box=(int(cx-r),int(cy-r),int(cx+r),int(cy+r)); t=im.crop(box).resize((480,480),Image.LANCZOS).convert('RGBA')
        m=Image.new('L',(480,480),0); ImageDraw.Draw(m).ellipse((2,2,477,477),fill=255); t.putalpha(m)
        if inner<1:
            d=ImageDraw.Draw(t); d.ellipse((4,4,475,475),outline=(232,190,100,255),width=16); d.ellipse((4,4,475,475),outline=(120,80,20,255),width=4)
        t=t.resize((160,160),Image.LANCZOS); t.save(f'{k}_{c}.png')
        S.paste(t.resize((120,120)),(j*130+5,row*130+5),t.resize((120,120)))
S.save('/tmp/lpsheet.png')
