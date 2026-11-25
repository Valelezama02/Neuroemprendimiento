"""Montaje F1-V: varios clips de ejercicio en 9:16 + audio + subtitulos (sin logo ni firma).
Uso: python3 render.py config.json salida.mp4
config: {"shots":[{"src","ss","cx"}...], "shot_dur":2.5, "audio":path|null, "audio_ss":0, "body":15,
         "end":0, "subs":[{"t0","t1","text"}...], "music":path|null}
"""
import json, subprocess, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(HERE, 'brand')
cfg = json.load(open(sys.argv[1])); out = sys.argv[2]
shots = cfg['shots']; body = cfg['body']; end = cfg.get('end',0); total = body + end
n = len(shots); dur = total / n

def probe(p):
    r = subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height','-of','csv=p=0',p],capture_output=True,text=True)
    w,h = map(int, r.stdout.strip().split(',')); return w,h

inputs=[]; flt=[]
GRADE = ("eq=contrast=1.12:saturation=0.55:brightness=-0.035:gamma=0.95,"
         "colorbalance=bs=0.06:bm=0.02:rh=-0.02,unsharp=5:5:0.6")
for k,s in enumerate(shots):
    w,h = probe(s['src']); cw = int(round(h*9/16/2))*2
    x = max(0, min(w-cw, int(s['cx']*w - cw/2)))
    inputs += ['-ss', str(s['ss']), '-t', f'{dur:.3f}', '-i', s['src']]
    flt.append(f"[{k}:v]fps=30,crop={cw}:{h}:{x}:0,scale=1080:1920:flags=lanczos,{GRADE},setsar=1,trim=duration={dur:.3f},setpts=PTS-STARTPTS[s{k}]")
flt.append(''.join(f'[s{k}]' for k in range(n)) + f"concat=n={n}:v=1:a=0,vignette=PI/5[base]")
i = n
# Sin marca de agua ni firma: el logo de Instagram solo aparece al descargar desde la app.
flt.append(f"[base]fade=t=in:st=0:d=0.3,fade=t=out:st={total-0.4}:d=0.4[b3]")
# subtitulos: mayusculas, blanco, pequeños, centrados (estilo R1)
font = os.path.join(B,'Oswald-Medium.ttf')
last='b3'
for j,sub in enumerate(cfg.get('subs',[])):
    txt = sub['text'].upper().replace("\\","\\\\").replace("'", "’").replace(':','\\:').replace('%','\\%')
    lines = txt.split('\n')
    for li,line in enumerate(lines):
        y = f"(h*0.60)+{li*62}-{(len(lines)-1)*31}"
        flt.append(f"[{last}]drawtext=fontfile={font}:text='{line}':fontsize=48:fontcolor=white:"
                   f"shadowcolor=black@0.6:shadowx=0:shadowy=2:x=(w-text_w)/2:y={y}:"
                   f"enable='between(t,{sub['t0']},{sub['t1']})'[t{j}_{li}]")
        last=f't{j}_{li}'
flt.append(f"[{last}]format=yuv420p[vout]")
amap=[]
if cfg.get('audio'):
    inputs += ['-ss', str(cfg.get('audio_ss',0)), '-t', str(body), '-i', cfg['audio']]; ai=i; i+=1
    achain = f"[{ai}:a]aresample=48000,afade=t=in:d=0.05,afade=t=out:st={body-0.4}:d=0.4,apad=whole_dur={total}"
    if cfg.get('music'):
        inputs += ['-stream_loop','-1','-i', cfg['music']]; mi=i; i+=1
        flt.append(achain+"[voz]")
        flt.append(f"[{mi}:a]aresample=48000,volume=0.12,atrim=duration={total},afade=t=out:st={total-1}:d=1[mus]")
        flt.append("[voz][mus]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[aout]")
    else:
        flt.append(achain+",loudnorm=I=-14:TP=-1.5[aout]")
    amap=['-map','[aout]','-c:a','aac','-b:a','192k']
cmd=['ffmpeg','-v','error','-y',*inputs,'-filter_complex',';'.join(flt),'-map','[vout]',*amap,
     '-t',str(total),'-c:v','libx264','-preset','medium','-crf','18','-r','30','-movflags','+faststart',out]
subprocess.run(cmd,check=True)
print('ok',out,total)
