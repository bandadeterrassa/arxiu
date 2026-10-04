import html
E=html.escape
ICON={
 'user':'<circle cx="12" cy="8" r="3.6"/><path d="M5 20c1.2-3.6 4-5.4 7-5.4s5.8 1.8 7 5.4"/>',
 'plus':'<path d="M12 5v14M5 12h14"/>',
 'search':'<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4 4"/>',
 'shelf':'<path d="M5 4h4v16H5zM10 4h4v16h-4zM15.5 5l3.5 1-3 14-3.5-1"/>',
 'cal':'<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/>',
 'check':'<path d="M9 6h11M9 12h11M9 18h11M4 6l1 1 2-2M4 12l1 1 2-2M4 18l1 1 2-2"/>',
 'sliders':'<path d="M4 7h10M18 7h2M4 17h4M12 17h8"/><circle cx="16" cy="7" r="2"/><circle cx="10" cy="17" r="2"/>',
 'filter':'<path d="M4 6h16M7 12h10M10 18h4"/>',
}
def ico(n,cls='ico'): return f'<svg class="{cls}" viewBox="0 0 24 24">{ICON[n]}</svg>'
def tabbar(first, badge=True):
    t=[(first,'shelf'),('Projectes','cal'),('Per revisar','check'),('Ajustos','sliders')]
    s='<nav class="tabbar glass" data-system data-float>'
    for i,(l,ic) in enumerate(t):
        b='<span class="badge">26</span>' if (l=='Per revisar' and badge) else ''
        s+=f'<div class="tab{" on" if i==0 else ""}">{b}{ico(ic)}{l}</div>'
    return s+'</nav>'
def top(btncls=''):
    return f'''<div class="top"><div class="brand"><img src="../logo.png" alt="">Banda de Terrassa</div>
      <div class="tools"><div class="gbtn glass">{ico("user")}</div><div class="gbtn add" aria-label="Registra una obra">{ico("plus")}</div></div></div>'''

# real pieces
A=[('A Christmas Festival','Leroy Anderson','ok'),('A Klezmer Karnival','Philip Sparke','ok'),
   ('A Town with an Ocean View','Joe Hisaishi','bad'),('ABBA Gold','arr. R. Sebregts','ok'),
   ('Adagio','Tomaso Albinoni','ok'),('Aida – Acte II','Giuseppe Verdi','ok'),
   ('Aladdin','Alan Menken','ok'),('All That Jazz','John Kander','bad'),
   ('Also sprach Zarathustra','Richard Strauss','ok'),('Amarcord','Nino Rota','rev'),
   ('Amazing Grace','Tradicional','ok'),('American Patrol','F. W. Meacham','warn'),
   ('Amparito Roca','Jaime Texidor','ok'),('Antarctica','Carl Wittrock','ok')]
B=[('Bailando','Enrique Iglesias','ok'),('Ball de Gegants','Tradicional','ok'),('Barcelona','Freddie Mercury','warn'),
   ('Bella ciao','Tradicional','ok'),('Bohemian Rhapsody','Freddie Mercury','bad'),('Bolero','Maurice Ravel','ok'),('Bolivar','Eros Ramazzotti','ok')]
STLABEL={'ok':'Completa','bad':'Falten parts','warn':'Sense verificar','rev':'Cal revisar'}

# ---------- 1 · Prestatgeria ----------
widths=[50,44,58,46,42,54,48,56,52,44,46,50,58,46]
tones=['#102A43','#1E3A5F','#29486F','#163250','#33557F','#0E2238']
def spines(lst,off=0):
    s=''
    for i,(t,c,st) in enumerate(lst):
        w=widths[(i+off)%len(widths)]; h=[188,176,196,182,170,192][(i+off)%6]
        bg=tones[(i+off)%len(tones)]
        if t in ('Adagio','Bolero'): bg='#F4EEE4'
        dark='color:#102A43' if bg=='#F4EEE4' else ''
        s+=f'<div class="spine {st}{" paper" if dark else ""}" style="width:{w}px;height:{h}px;background:{bg}"><span class="sp-t" style="line-height:{w}px;{dark}">{E(t)}</span><i class="lab"></i></div>'
    return s
d1=f'''<section class="screen e1" data-name="1-prestatgeria" data-time="19:42">
 <div class="body">
  {top()}
  <div class="hero"><h1>Armari<br>0P2</h1><p class="sub"><b>539</b> obres<br>en 26 prestatges</p></div>
  <div class="search">{ico("search")}<span>Títol, autor, projecte…</span></div>
  <div class="shelves" data-scrolls>
    <div class="shelf"><div class="shlab">A<small>58</small></div><div class="row" data-bleed>{spines(A[:9])}</div></div>
    <div class="shelf"><div class="shlab">B<small>31</small></div><div class="row" data-bleed>{spines(B,3)}</div></div>
  </div>
 </div>
 {tabbar('Armari')}
</section>'''

# ---------- 2 · Cartell ----------
def plist(lst):
    s=''
    for t,c,st in lst:
        stamp=f'<span class="stamp {st}">{STLABEL[st]}</span>' if st!='ok' else ''
        s+=f'<div class="pr"><div class="pt">{E(t)}</div><div class="pc">{E(c)}{stamp}</div></div>'
    return s
d2=f'''<section class="screen e2" data-name="2-cartell" data-time="12:05">
 <svg class="bigA" viewBox="0 0 300 300" aria-hidden="true"><path d="M30 290 L130 10 L190 10 L290 290 L222 290 L202 228 L118 228 L98 290 Z M135 176 L185 176 L160 96 Z" fill="rgba(20,17,12,.07)" fill-rule="evenodd"/></svg>
 <div class="body">
  {top()}
  <h1>Què<br>toquem?</h1>
  <div class="search">{ico("search")}<span>Busca entre 539 obres</span></div>
  <div class="next"><span class="k">Pròxim</span><span>Concert de Nadal · 20 de desembre</span></div>
  <div class="plist" data-scrolls>{plist([A[0],A[2],A[4],A[7],A[9],A[11]])}</div>
 </div>
 {tabbar('Obres')}
</section>'''

# ---------- 3 · Pentagrama ----------
def staff(lst):
    s=''
    for t,c,st in lst:
        s+=f'<div class="sr {st}"><svg class="note" viewBox="0 0 26 20"><ellipse cx="13" cy="10" rx="9" ry="6.2" transform="rotate(-22 13 10)"/></svg><div class="tx"><div class="t">{E(t)}</div><div class="c">{E(c)}{" · <b>"+STLABEL[st]+"</b>" if st!="ok" else ""}</div></div></div>'
    return s
keys=''.join(f'<span class="k{" on" if L=="A" else ""}">{L}</span>' for L in 'ABCDEFGHIJ')
d3=f'''<section class="screen e3" data-name="3-pentagrama" data-theme="dark" data-time="21:30">
 <div class="body">
  {top()}
  <h1>Repertori</h1><p class="sub">539 obres · llegides d'esquerra a dreta, de la A a la Z</p>
  <div class="search">{ico("search")}<span>Títol, autor, projecte…</span></div>
  <div class="score" data-scrolls>{staff([A[0],A[1],A[2],A[4],A[7],A[9],A[11],A[12]])}</div>
  <div class="piano" data-float>{keys}</div>
 </div>
 {tabbar('Repertori')}
</section>'''

css=open('explore2.css').read()
open('explore2.html','w').write(f'''<!doctype html><html lang="ca"><head><meta charset="utf-8"><title>Exploració 2 · Arxiu</title>
<link rel="stylesheet" href="kit/device.css"><link rel="stylesheet" href="fonts/fonts.css"><style>{css}</style></head><body>
{d1}{d2}{d3}
<script src="kit/device.js"></script></body></html>''')
print('ok')
