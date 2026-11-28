import subprocess, sys, os, numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as ndi
def frames(path):
    d=f'/tmp/fr2_{os.path.basename(path)}'; os.makedirs(d,exist_ok=True); [os.remove(os.path.join(d,x)) for x in os.listdir(d)]
    subprocess.run(['ffmpeg','-v','error','-i',path,'-vf','fps=12,scale=iw*2:ih*2:flags=lanczos',f'{d}/%04d.png'],check=True)
    return [np.asarray(Image.open(os.path.join(d,x)).convert('RGB')).astype(int) for x in sorted(os.listdir(d))]
def proc(path,out):
    F=frames(path); RGBA=[]
    for c in F:
        mx=c.max(-1); sat=mx-c.min(-1)
        bgl=(mx>=13)&(mx<=52)&(sat<22)          # the app's grey-purple backdrop (hair/outlines are darker, ~6)
        lb,n=ndi.label(bgl); edge=set(np.unique(np.concatenate([lb[0],lb[-1],lb[:,0],lb[:,-1]])))-{0}
        bg=np.isin(lb,list(edge))
        fg=~bg; fg=ndi.binary_opening(fg,np.ones((5,5))); lb2,n2=ndi.label(fg)
        if n2:
            ar=ndi.sum(fg,lb2,range(1,n2+1)); fg=np.isin(lb2,[i+1 for i,a in enumerate(ar) if a>=ar.max()*.05])
        fg=ndi.binary_fill_holes(fg)
        ol=ndi.binary_dilation(fg,iterations=7)
        o=np.zeros(c.shape[:2]+(4,),np.uint8); o[ol]=(255,255,255,255); o[fg,:3]=c[fg]; o[fg,3]=255
        RGBA.append(o)
    U=np.stack([x[...,3]>0 for x in RGBA]).any(0); ys,xs=np.where(U); y0,y1,x0,x1=ys.min(),ys.max()+1,xs.min(),xs.max()+1
    outF=[]
    for o in RGBA:
        im=Image.fromarray(o[y0:y1,x0:x1],'RGBA'); H,W=im.height,im.width; s=344/max(H,W)
        im=im.resize((round(W*s),round(H*s)),Image.LANCZOS)
        cv=Image.new('RGBA',(360,360),(0,0,0,0)); cv.alpha_composite(im,((360-im.width)//2,(360-im.height)//2)); outF.append(cv)
    outF[0].save(out+'.webp',save_all=True,append_images=outF[1:],duration=83,loop=0,quality=78,method=4)
    outF[len(outF)//3].save(out+'_p.png')
    print(out,len(outF),os.path.getsize(out+'.webp'))
proc(sys.argv[1],sys.argv[2])
