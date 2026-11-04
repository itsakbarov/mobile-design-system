"""Render the README's original visual examples from Custom UI Design System tokens.

Run from any directory: python examples/render.py
Requires Pillow. No network, downloaded artwork, or bundled fonts are used.
These are reference illustrations, not screenshots of a native component library.
"""
from pathlib import Path
from functools import lru_cache
import json
import math
import random
import re

from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
SCALE = 2
SPEC = (ROOT / 'CUSTOM_UI_DESIGN_SYSTEM.md').read_text(encoding='utf-8')
TOKENS = json.loads(re.search(r'```json\n(.*?)\n```', SPEC, re.S).group(1))
COLORS = TOKENS['color']


@lru_cache(maxsize=100)
def font(size, weight='regular', scale=SCALE):
    candidates = {
        'regular': ['C:/Windows/Fonts/segoeui.ttf', '/System/Library/Fonts/SFNS.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'],
        'medium': ['C:/Windows/Fonts/seguisb.ttf', '/System/Library/Fonts/SFNS.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'],
        'bold': ['C:/Windows/Fonts/segoeuib.ttf', '/System/Library/Fonts/SFNS.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'],
    }
    for filename in candidates[weight]:
        if Path(filename).exists():
            return ImageFont.truetype(filename, round(size * scale))
    return ImageFont.load_default()


def rgba(color):
    if isinstance(color, tuple):
        return color
    value = color.lstrip('#')
    if len(value) == 6:
        value += 'FF'
    return tuple(int(value[i:i+2], 16) for i in range(0, 8, 2))


class Canvas:
    def __init__(self, w, h, background, scale=SCALE):
        self.w, self.h, self.s = w, h, scale
        self.im = Image.new('RGBA', (round(w * scale), round(h * scale)), rgba(background))
        self.d = ImageDraw.Draw(self.im)

    def box(self, value):
        return tuple(round(v * self.s) for v in value)

    def rect(self, box, fill, radius=0, outline=None, width=1):
        fill_color=rgba(fill) if fill else None
        if fill_color and fill_color[3]==0: fill_color=None
        self.d.rounded_rectangle(self.box(box), radius=round(radius*self.s), fill=fill_color, outline=rgba(outline) if outline else None, width=round(width*self.s))

    def circle(self, x, y, r, fill=None, outline=None, width=1):
        self.d.ellipse(self.box((x-r, y-r, x+r, y+r)), fill=rgba(fill) if fill else None, outline=rgba(outline) if outline else None, width=max(1, round(width*self.s)))

    def line(self, points, fill, width=1):
        self.d.line([tuple(round(v*self.s) for v in p) for p in points], fill=rgba(fill), width=max(1, round(width*self.s)), joint='curve')

    def text(self, x, y, value, size, fill, weight='regular', anchor='lt', max_width=None):
        f = font(size, weight, self.s)
        if max_width is not None:
            actual = self.d.textlength(value, font=f) / self.s
            if actual > max_width + 1:
                raise ValueError(f'Text exceeds {max_width}: {value!r} ({actual:.1f})')
        self.d.text((round(x*self.s), round(y*self.s)), value, fill=rgba(fill), font=f, anchor=anchor)

    def paragraph(self, x, y, value, size, fill, line_height, max_width, weight='regular'):
        cursor = y
        for para in value.split('\n'):
            line = ''
            for word in para.split():
                trial = f'{line} {word}'.strip()
                if self.d.textlength(trial, font=font(size, weight, self.s)) / self.s > max_width and line:
                    self.text(x, cursor, line, size, fill, weight)
                    cursor += line_height
                    line = word
                else:
                    line = trial
            self.text(x, cursor, line, size, fill, weight, max_width=max_width)
            cursor += line_height
        return cursor

    def icon(self, name, x, y, size, color, width=1.7):
        q = size / 24
        def pts(*points):
            return [(x + a*q, y + b*q) for a, b in points]
        def ln(*points):
            self.line(pts(*points), color, width*q)
        def ci(a,b,r,filled=False):
            self.circle(x+a*q,y+b*q,r*q,color if filled else None,None if filled else color,width*q)
        def rr(a,b,c,d,r=0,filled=False):
            self.rect((x+a*q,y+b*q,x+c*q,y+d*q),color if filled else '#00000000',r*q,None if filled else color,width*q)
        if name == 'plus': ln((12,5),(12,19)); ln((5,12),(19,12))
        elif name == 'check': ln((5,12),(10,17),(19,7))
        elif name == 'close': ln((6,6),(18,18)); ln((18,6),(6,18))
        elif name == 'search': ci(10.5,10.5,6.5); ln((15.5,15.5),(20,20))
        elif name == 'back': ln((14,5),(7,12),(14,19))
        elif name == 'chevron': ln((9,6),(15,12),(9,18))
        elif name == 'arrow': ln((12,19),(12,5)); ln((6,11),(12,5),(18,11))
        elif name == 'home': ln((3,11),(12,3),(21,11)); ln((5,10),(5,21),(10,21),(10,15),(14,15),(14,21),(19,21),(19,10))
        elif name == 'library':
            rr(3,4,8,21,1); rr(10,4,15,21,1); ln((18,5),(22,20))
        elif name == 'activity': ln((2,13),(6,13),(9,6),(14,19),(17,11),(22,11))
        elif name == 'person': ci(12,8,4); self.d.arc(self.box((x+4*q,y+13*q,x+20*q,y+27*q)),180,360,fill=rgba(color),width=round(width*q*self.s))
        elif name == 'folder': ln((3,7),(3,20),(21,20),(21,7),(12,7),(9,4),(3,4),(3,7))
        elif name == 'bookmark': ln((6,3),(18,3),(18,21),(12,17),(6,21),(6,3))
        elif name == 'bell': ln((5,17),(6,9),(8,5),(12,4),(16,5),(18,9),(19,17),(5,17)); ln((10,21),(14,21))
        elif name == 'more':
            for a in (5,12,19): ci(a,12,1.5,True)
        elif name == 'pause': rr(6,5,9,19,1,True); rr(15,5,18,19,1,True)
        elif name == 'play': self.d.polygon([tuple(round(v*self.s) for v in p) for p in pts((8,4),(20,12),(8,20))], fill=rgba(color))
        elif name in ('previous','next'):
            if name == 'next':
                self.d.polygon([tuple(round(v*self.s) for v in p) for p in pts((5,5),(15,12),(5,19))],fill=rgba(color)); ln((18,5),(18,19))
            else:
                self.d.polygon([tuple(round(v*self.s) for v in p) for p in pts((19,5),(9,12),(19,19))],fill=rgba(color)); ln((6,5),(6,19))
        elif name == 'heart':
            ln((12,20),(3,11),(3,7),(5,4),(9,4),(12,7),(15,4),(19,4),(21,7),(21,11),(12,20))
        elif name == 'headphones':
            self.d.arc(self.box((x+4*q,y+3*q,x+20*q,y+20*q)),180,360,fill=rgba(color),width=round(width*q*self.s)); rr(3,11,7,20,2); rr(17,11,21,20,2)
        elif name == 'shuffle': ln((3,6),(7,6),(17,18),(21,18)); ln((17,15),(21,18),(17,21)); ln((3,18),(7,18),(17,6),(21,6)); ln((17,3),(21,6),(17,9))
        elif name == 'repeat': ln((4,10),(4,6),(19,6),(19,10)); ln((16,3),(20,6),(16,9)); ln((20,14),(20,18),(5,18),(5,14)); ln((8,15),(4,18),(8,21))
        elif name == 'sparkle': ln((12,2),(14.5,9.5),(22,12),(14.5,14.5),(12,22),(9.5,14.5),(2,12),(9.5,9.5),(12,2))
        elif name == 'mail': rr(3,5,21,19,3); ln((3,7),(12,13),(21,7))
        elif name == 'lock': rr(5,10,19,21,3); self.d.arc(self.box((x+8*q,y+2*q,x+16*q,y+15*q)),180,360,fill=rgba(color),width=round(width*q*self.s)); ci(12,15,1,True)
        elif name == 'link': ln((9,15),(15,9)); ln((7,16),(5,18),(2,18),(1,15),(1,12),(7,6),(10,6),(12,8)); ln((12,16),(14,18),(17,18),(23,12),(23,9),(21,6),(18,6),(16,8))
        elif name == 'copy': rr(8,8,21,21,3); ln((4,16),(3,16),(3,3),(16,3),(16,4))
        elif name == 'trash': ln((4,6),(20,6)); ln((8,6),(8,3),(16,3),(16,6)); ln((6,6),(7,21),(17,21),(18,6)); ln((10,10),(10,17)); ln((14,10),(14,17))
        elif name == 'alert': ci(12,12,9); ln((12,7),(12,13)); ci(12,17,1,True)
        elif name == 'check-circle': ci(12,12,10); ln((7,12),(11,16),(17,8))
        elif name == 'clock': ci(12,12,9); ln((12,6),(12,12),(16,14))
        else: raise ValueError(name)

    def paste(self, im, x, y, w=None, h=None, radius=None):
        if isinstance(im, Canvas): im = im.im
        w = w or im.width/self.s
        h = h or im.height/self.s
        tile = im.resize((round(w*self.s),round(h*self.s)),Image.Resampling.LANCZOS)
        if radius is not None:
            mask = Image.new('L',tile.size,0)
            ImageDraw.Draw(mask).rounded_rectangle((0,0,tile.width-1,tile.height-1),radius=round(radius*self.s),fill=255)
            tile.putalpha(mask)
        self.im.alpha_composite(tile,(round(x*self.s),round(y*self.s)))

    def save(self,path,full_resolution=False):
        path=ASSETS/path
        path.parent.mkdir(parents=True,exist_ok=True)
        im=self.im.convert('RGB')
        if not full_resolution:
            im=im.resize((round(self.w),round(self.h)),Image.Resampling.LANCZOS)
        im.save(path,optimize=True)
        return path


def button(c,x,y,w,label,p,kind='primary',icon=None,h=None):
    h = h or TOKENS['size']['controlMinHeight']
    bg,fg=p['action'],p['onAction']
    if kind=='secondary': bg,fg=p['surfaceInset'],p['textPrimary']
    elif kind=='disabled': bg,fg=p['disabledSurface'],p['disabledText']
    elif kind=='quiet': bg,fg=p['canvas'],p['textSecondary']
    elif kind=='danger': bg,fg=p['dangerText'],p['dangerSurface']
    c.rect((x,y,x+w,y+h),bg,TOKENS['radius']['surface'])
    if icon:
        c.icon(icon,x+16,y+(h-20)/2,20,fg)
        c.text(x+44,y+h/2,label,14,fg,'medium',anchor='lm',max_width=w-56)
    else:
        c.text(x+w/2,y+h/2,label,14,fg,'medium',anchor='mm',max_width=w-20)


def badge(c,x,y,label,p,kind='info',icon=None):
    fg=p[kind+'Text']; bg=p[kind+'Surface']
    tw=c.d.textlength(label,font=font(14,'medium',c.s))/c.s
    w=tw+24+(26 if icon else 0)
    c.rect((x,y,x+w,y+32),bg,8)
    if icon: c.icon(icon,x+10,y+7,18,fg)
    c.text(x+(36 if icon else 12),y+16,label,14,fg,'medium',anchor='lm')
    return w


def switch(c,x,y,p,on=True):
    c.rect((x,y,x+48,y+28),p['action'] if on else p['controlBorder'],14)
    c.circle(x+(34 if on else 14),y+14,10,p['onAction'] if on else p['surface'])


def status_bar(c,p):
    c.text(26,20,'9:41',14,p['textPrimary'],'medium')
    for i,h in enumerate((4,7,10,13)):
        c.rect((302+i*4,22+13-h,304+i*4,35),p['textPrimary'],1)
    c.d.arc(c.box((323,20,338,35)),210,330,fill=rgba(p['textPrimary']),width=3*c.s)
    c.d.arc(c.box((327,24,334,32)),210,330,fill=rgba(p['textPrimary']),width=2*c.s)
    c.circle(330.5,33,1.2,p['textPrimary'])
    c.rect((346,23,368,34),'#00000000',3,p['textSecondary'],1)
    c.rect((348,25,364,32),p['textPrimary'],1)
    c.rect((369,26,371,31),p['textSecondary'],1)


def home_indicator(c,p):
    c.rect((145,832,245,836),p['textPrimary'],2)


def nav(c,y,p,active='Library'):
    c.rect((0,y,390,y+88),p['surface'])
    c.line(((0,y),(390,y)),p['divider'])
    for i,(label,ic) in enumerate((('Home','home'),('Library','library'),('Activity','activity'),('Profile','person'))):
        x=24+i*85.5
        fg=p['accentText'] if label==active else p['textSecondary']
        if label==active: c.rect((x+17,y+8,x+68,y+40),p['selectedSurface'],16)
        c.icon(ic,x+30.5,y+12,24,fg)
        c.text(x+42.75,y+48,label,14,fg,'medium' if label==active else 'regular',anchor='mt')


def artwork(w,h,variant='tide'):
    c=Canvas(w,h,'#17142D')
    # Original procedural artwork. Gradients belong to the artwork, not UI text.
    px=c.im.load()
    for y in range(c.im.height):
        yy=y/c.im.height
        for x in range(c.im.width):
            xx=x/c.im.width
            glow=max(0,1-math.sqrt((xx-.68)**2+(yy-.3)**2)*1.6)
            if variant=='tide':
                r=int(18+49*glow+9*yy); g=int(21+30*glow+8*yy); b=int(43+75*glow)
            else:
                r=int(222+18*yy);g=int(220+15*yy);b=int(242+7*yy)
            px[x,y]=(r,g,b,255)
    c.d=ImageDraw.Draw(c.im)
    rng=random.Random(17)
    if variant=='tide':
        for i in range(15):
            k=i/14
            box=(-w*.3+i*w*.02,h*.22+i*h*.024,w*1.7-i*w*.015,h*1.6+i*h*.01)
            col=(round(100+110*k),round(130+70*k),round(180+50*k),255)
            c.d.arc(c.box(box),192,312,fill=col,width=max(1,round(w*.018*c.s)))
        for _ in range(45):
            x,y=rng.random()*w,rng.random()*h*.65
            c.circle(x,y,.5,'#D6C9FF')
        if w>200:
            c.text(w*.09,h*.1,'AMBIENT SERIES',w*.035,'#E5DEFF','medium')
            c.text(w*.09,h*.205,'After',w*.12,'#FFFFFF','medium')
            c.text(w*.09,h*.337,'the tide',w*.12,'#FFFFFF','medium')
    else:
        ink='#6E56CF' if variant=='notes' else '#36707C'
        for i in range(5):
            if variant=='notes':
                c.rect((w*.12+i*10,h*.18+i*5,w*.7+i*10,h*.8+i*4),'#00000000',8,ink,1)
            else:
                c.circle(w*.63,h*.55,12+i*10,None,ink,1)
    return c


def screen_library():
    p=COLORS['light']; c=Canvas(390,844,p['canvas'])
    status_bar(c,p)
    c.text(24,78,'Library',28,p['textPrimary'],'medium')
    c.rect((318,70,366,118),p['surface'],16)
    c.icon('plus',330,82,24,p['textPrimary'])
    c.text(24,119,'Good ideas, kept close.',17,p['textSecondary'])
    c.rect((24,161,366,213),p['surface'],12,p['controlBorder'])
    c.icon('search',40,175,24,p['textSecondary'])
    c.text(76,187,'Search collections',17,p['textSecondary'],anchor='lm')
    c.rect((24,237,366,293),p['surfaceInset'],16)
    c.rect((28,241,137,289),p['selectedSurface'],12)
    for x,label,fg in ((82,'All',p['accentText']),(195,'Saved',p['textSecondary']),(308,'Shared',p['textSecondary'])):
        c.text(x,265,label,14,fg,'medium',anchor='mm')
    c.text(24,328,'Collections',20,p['textPrimary'],'medium')
    c.text(366,333,'See all',14,p['accentText'],'medium',anchor='rt')
    for x,title,n,art in ((24,'Product notes','18 saved items','notes'),(201,'Everyday UI','12 saved items','ui')):
        c.rect((x,369,x+165,566),p['surface'],16)
        c.paste(artwork(141,92,art),x+12,381,141,92,12)
        c.text(x+16,491,title,17,p['textPrimary'],'medium',max_width=133)
        c.text(x+16,525,n,14,p['textSecondary'],max_width=133)
    c.text(24,603,'Recently saved',20,p['textPrimary'],'medium')
    c.rect((24,647,72,695),p['accentSurface'],12)
    c.icon('bookmark',36,659,24,p['accentText'])
    c.text(88,649,'A calmer onboarding',17,p['textPrimary'],'medium',max_width=240)
    c.text(88,678,'Interface · 2 hours ago',14,p['textSecondary'])
    c.icon('chevron',344,659,20,p['textSecondary'])
    c.icon('check-circle',25,716,16,p['successText'])
    c.text(49,716,'All changes synced',12,p['textSecondary'])
    nav(c,756,p)
    home_indicator(c,p)
    return c


def screen_player():
    p=COLORS['dark']; c=Canvas(390,844,p['canvas'])
    status_bar(c,p)
    for x,ic in ((24,'back'),(318,'more')):
        c.rect((x,69,x+48,117),p['surfaceRaised'],16)
        c.icon(ic,x+12,81,24,p['textPrimary'])
    c.text(195,93,'Now playing',14,p['textSecondary'],'medium',anchor='mm')
    c.paste(artwork(342,342),24,145,342,342,32)
    c.text(24,525,'After the tide',28,p['textPrimary'],'medium',max_width=280)
    c.text(24,568,'Ambient collection · 2026',17,p['textSecondary'])
    c.icon('heart',333,531,24,p['textPrimary'])
    c.rect((24,617,366,621),p['divider'],2)
    c.rect((24,617,171,621),p['action'],2)
    c.circle(171,619,5,p['action'])
    c.text(24,634,'1:42',12,p['textSecondary'])
    c.text(366,634,'−2:18',12,p['textSecondary'],anchor='rt')
    for cx,ic in ((48,'shuffle'),(119,'previous'),(271,'next'),(342,'repeat')):
        c.icon(ic,cx-12,687,24,p['textSecondary'] if ic in ('shuffle','repeat') else p['textPrimary'])
    c.circle(195,699,32,p['action'])
    c.icon('pause',180,684,30,p['onAction'])
    c.rect((24,764,366,816),p['surfaceRaised'],26)
    c.icon('headphones',42,780,20,p['textSecondary'])
    c.text(78,790,'Listening on headphones',14,p['textSecondary'],anchor='lm')
    c.icon('chevron',334,780,20,p['textSecondary'])
    home_indicator(c,p)
    return c


def screen_assistant():
    p=COLORS['dark']; c=Canvas(390,844,p['canvas'])
    status_bar(c,p)
    c.icon('back',26,82,24,p['textPrimary'])
    c.text(195,78,'Writing assistant',17,p['textPrimary'],'medium',anchor='mt')
    c.text(195,103,'Writing partner',12,p['textSecondary'],anchor='mt')
    c.icon('more',338,82,24,p['textPrimary'])
    c.rect((61,156,366,236),p['surfaceRaised'],16)
    c.paragraph(77,173,'Help me simplify this\nonboarding.',17,p['textPrimary'],24,273)
    c.rect((24,281,60,317),p['accentSurface'],12)
    c.icon('sparkle',32,289,20,p['accentText'])
    c.text(76,287,'A clearer first step',20,p['textPrimary'],'medium',max_width=290)
    c.paragraph(24,345,"Start with the user's goal. Ask for\none useful detail, then let them\ntry the product.",17,p['textPrimary'],26,342)
    for i,label in enumerate(('One clear next action','Permissions when needed','Progress you can return to')):
        y=456+i*44
        c.icon('check',24,y+1,20,p['accentText'])
        c.text(60,y,label,17,p['textPrimary'],max_width=306)
    c.text(24,612,'Here is a shorter opening…',17,p['accentText'],max_width=342)
    c.text(24,663,'You can stop and keep this draft.',14,p['textSecondary'])
    c.rect((16,747,374,811),p['surfaceRaised'],32,p['controlBorder'])
    c.icon('plus',34,767,24,p['textSecondary'])
    c.text(78,779,'Ask a follow-up',17,p['textSecondary'],anchor='lm')
    c.circle(340,779,20,p['action'])
    c.rect((333,772,347,786),p['onAction'],3)
    home_indicator(c,p)
    return c


def header(c,title,subtitle,p,theme):
    c.text(56,49,title,35,p['textPrimary'],'medium')
    c.text(56,105,subtitle,17,p['textSecondary'])
    c.rect((1000,54,1144,96),p['surfaceRaised'],21,p['divider'])
    c.circle(1023,75,5,p['action'])
    c.text(1040,75,theme,14,p['textPrimary'],'medium',anchor='lm')
    c.line(((56,152),(1144,152)),p['divider'])


def component_board(theme):
    p=COLORS[theme]; c=Canvas(1200,1090,p['canvas'])
    header(c,'The components, together.','Shared anatomy. Clear states. One restrained accent.',p,theme.capitalize()+' theme')
    # Two reading columns, with components on the canvas rather than a card grid.
    a,b,w=56,646,498
    c.text(a,187,'Actions',20,p['textPrimary'],'medium')
    button(c,a,231,156,'Continue',p)
    button(c,a+172,231,156,'View details',p,'secondary')
    button(c,a+344,231,154,'Cancel',p,'quiet')
    button(c,a,299,156,'Saving…',p,icon='clock')
    button(c,a+172,299,156,'Unavailable',p,'disabled')
    c.text(a,375,'Fields & validation',20,p['textPrimary'],'medium')
    c.text(a,416,'Collection name',14,p['textSecondary'],'medium')
    c.rect((a-4,440,a+w+4,500),'#00000000',16,p['focus'],2)
    c.rect((a,444,a+w,496),p['surface'],12,p['controlBorder'])
    c.text(a+16,470,'Weekend reading',17,p['textPrimary'],anchor='lm')
    caretx=a+16+c.d.textlength('Weekend reading',font=font(17,'regular',c.s))/c.s+2
    c.line(((caretx,458),(caretx,482)),p['focus'],1)
    c.text(a,525,'Email address',14,p['textSecondary'],'medium')
    c.rect((a,553,a+w,605),p['surface'],12,p['dangerText'],1.5)
    c.text(a+16,579,'alex@',17,p['textPrimary'],anchor='lm')
    c.icon('alert',a+w-38,568,22,p['dangerText'])
    c.text(a,618,'Enter a complete email address.',14,p['dangerText'])
    c.text(a,677,'Rows & choices',20,p['textPrimary'],'medium')
    for i,(title,detail,ic) in enumerate((('Design notes','18 saved items','folder'),('Notifications','Updates that matter','bell'))):
        y=724+i*92
        c.rect((a,y,a+48,y+48),p['surfaceInset'],12)
        c.icon(ic,a+12,y+12,24,p['textSecondary'])
        c.text(a+64,y+1,title,17,p['textPrimary'],'medium')
        c.text(a+64,y+29,detail,14,p['textSecondary'])
        if i==0: c.icon('chevron',a+w-27,y+13,22,p['textSecondary'])
        else: switch(c,a+w-48,y+9,p)
    c.text(b,187,'Selection',20,p['textPrimary'],'medium')
    c.rect((b,231,b+w,287),p['surfaceInset'],16)
    c.rect((b+4,235,b+164,283),p['selectedSurface'],12)
    for i,label in enumerate(('All items','Saved','Shared')):
        c.text(b+83+i*166,259,label,14,p['accentText'] if i==0 else p['textSecondary'],'medium',anchor='mm')
    c.text(b,326,'Status',20,p['textPrimary'],'medium')
    x=b
    for label,kind,ic in (('Queued','info','clock'),('Saved','success','check'),('Failed','danger','alert')):
        x+=badge(c,x,370,label,p,kind,ic)+12
    badge(c,b,418,'Needs review',p,'warning','alert')
    c.text(b,491,'Adjustments',20,p['textPrimary'],'medium')
    c.text(b,532,'Playback volume',17,p['textPrimary'])
    c.text(b+w,532,'64%',17,p['textSecondary'],'medium',anchor='rt')
    c.rect((b,578,b+w,584),p['surfaceInset'],3)
    c.rect((b,578,b+w*.64,584),p['action'],3)
    c.circle(b+w*.64,581,12,p['action'])
    c.text(b,631,'Feedback',20,p['textPrimary'],'medium')
    c.rect((b,675,b+w,755),p['surfaceRaised'],16,p['divider'])
    c.icon('check-circle',b+18,702,24,p['successText'])
    c.text(b+56,690,'Changes saved',17,p['textPrimary'],'medium')
    c.text(b+56,720,'Your collection is up to date.',14,p['textSecondary'])
    c.text(b+w-20,715,'Undo',14,p['accentText'],'medium',anchor='rm')
    c.text(b,800,'Navigation',20,p['textPrimary'],'medium')
    nav_example=Canvas(390,88,p['surface'])
    nav(nav_example,0,p)
    c.paste(nav_example,b,842,498,112,16)
    c.line(((56,982),(1144,982)),p['divider'])
    c.text(56,1015,'52',28,p['textPrimary'],'medium')
    c.text(107,1024,'control height',14,p['textSecondary'])
    c.text(326,1015,'48',28,p['textPrimary'],'medium')
    c.text(378,1024,'minimum target',14,p['textSecondary'])
    c.text(625,1015,'4–64',28,p['textPrimary'],'medium')
    c.text(703,1024,'spacing scale',14,p['textSecondary'])
    c.circle(1020,1032,12,p['action'])
    c.text(1044,1024,p['action'],14,p['textSecondary'])
    return c


def overlays_board():
    p=COLORS['light']; c=Canvas(1200,940,p['canvas'])
    header(c,'Small tasks. Complete states.','Focused overlays keep the original task in view.',p,'Light theme')
    c.text(56,187,'Verification',20,p['textPrimary'],'medium')
    c.text(646,187,'A contained action sheet',20,p['textPrimary'],'medium')
    # OTP is represented as one labeled field with a four-cell visual treatment.
    c.rect((56,237,554,704),p['surface'],28,p['divider'])
    c.rect((270,268,340,338),p['accentSurface'],22)
    c.icon('lock',291,289,28,p['accentText'])
    c.text(305,369,'Check your inbox',28,p['textPrimary'],'medium',anchor='mt')
    c.text(305,415,'Enter the code sent to alex@example.com.',14,p['textSecondary'],anchor='mt')
    for i,value in enumerate(('2','4','8','1')):
        x=135+i*88
        c.rect((x,464,x+76,536),p['surface'],12,p['dangerText'],1.5)
        c.text(x+38,500,value,28,p['textPrimary'],'medium',anchor='mm')
    c.text(305,556,'That code has expired. Request a new one.',14,p['dangerText'],anchor='mt')
    button(c,100,610,410,'Send a new code',p)
    # The scrim belongs to this example's task region, not the documentation page.
    c.rect((646,237,1144,854),p['surfaceInset'],28,p['divider'])
    c.text(674,267,'Library',28,p['textPrimary'],'medium')
    for i in range(3):
        y=324+i*62
        c.rect((674,y,711,y+37),p['divider'],8)
        c.rect((727,y+4,1050,y+13),p['divider'],4)
        c.rect((727,y+23,955,y+29),p['divider'],3)
    scrim=Image.new('RGBA',c.im.size,(0,0,0,0))
    sd=ImageDraw.Draw(scrim); sd.rounded_rectangle(c.box((646,237,1144,854)),radius=28*c.s,fill=(0,0,0,60))
    c.im.alpha_composite(scrim); c.d=ImageDraw.Draw(c.im)
    c.rect((646,470,1144,854),p['surfaceRaised'],28)
    c.rect((869,483,921,487),p['divider'],2)
    c.text(674,516,'Share collection',28,p['textPrimary'],'medium')
    c.icon('close',1098,520,22,p['textSecondary'])
    c.text(674,562,'Choose how people can access your ideas.',14,p['textSecondary'])
    for i,(label,ic) in enumerate((('Copy collection link','link'),('Invite a collaborator','person'))):
        y=611+i*72
        c.rect((674,y,722,y+48),p['surfaceInset'],12)
        c.icon(ic,686,y+12,24,p['textSecondary'])
        c.text(738,y+24,label,17,p['textPrimary'],anchor='lm',max_width=324)
        c.icon('chevron',1096,y+14,20,p['textSecondary'])
    button(c,674,779,442,'Done',p)
    c.text(56,753,'A clear recovery path',20,p['textPrimary'],'medium')
    c.paragraph(56,796,'A readable error, preserved input, and one useful next action.',17,p['textSecondary'],26,460)
    return c


def overview(screens):
    p=COLORS['light']; c=Canvas(1440,1160,p['canvas'])
    c.text(64,48,'Made to feel connected.',35,p['textPrimary'],'medium')
    c.text(64,104,'Three applications of the same mobile design language.',17,p['textSecondary'])
    c.rect((1060,51,1376,101),p['surface'],25,p['divider'])
    c.circle(1086,76,6,p['action'])
    c.text(1105,76,'Custom UI Design System',17,p['textPrimary'],'medium',anchor='lm',max_width=251)
    labels=(('Core','A collection library'),('Media','An artwork-led player'),('Assistant','A focused writing space'))
    xs=(64,540,1016); w=360; h=w*844/390
    for x,screen,(profile,desc) in zip(xs,screens,labels):
        c.text(x,170,profile,20,p['textPrimary'],'medium')
        c.text(x,204,desc,14,p['textSecondary'])
        shadow=Image.new('RGBA',c.im.size,(0,0,0,0)); sd=ImageDraw.Draw(shadow)
        sd.rounded_rectangle(c.box((x,250,x+w,250+h)),radius=38*c.s,fill=(23,20,35,28))
        shadow=shadow.filter(ImageFilter.GaussianBlur(12*c.s)); c.im.alpha_composite(shadow)
        c.rect((x-2,238,x+w+2,238+h+4),'#DDDDE4',40)
        c.paste(screen,x,240,w,h,38)
    c.text(720,1092,'Neutral foundations. Content-led screens. One focused interaction.',17,p['textSecondary'],anchor='mt')
    return c


def share_panel(c,x,y,w,h,p,detail_opacity=1):
    c.rect((x,y,x+w,y+h),p['surfaceRaised'],28,p['divider'])
    if detail_opacity<=0: return
    layer=Canvas(c.w,c.h,'#00000000',c.s)
    layer.icon('link',x+24,y+24,24,p['accentText'])
    layer.text(x+62,y+25,'Share collection',20,p['textPrimary'],'medium')
    layer.icon('close',x+w-44,y+25,20,p['textSecondary'])
    if h>200:
        layer.text(x+24,y+81,'Bring someone into the conversation.',14,p['textSecondary'])
        for i,(label,ic) in enumerate((('Copy link','link'),('Invite someone','person'))):
            yy=y+123+i*61
            layer.rect((x+16,yy-9,x+w-16,yy+43),p['surfaceInset'],12)
            layer.icon(ic,x+29,yy+5,22,p['textSecondary'])
            layer.text(x+66,yy+16,label,17,p['textPrimary'],anchor='lm')
            layer.icon('chevron',x+w-44,yy+7,18,p['textSecondary'])
    if detail_opacity<1:
        layer.im.putalpha(layer.im.getchannel('A').point(lambda a:round(a*detail_opacity)))
    c.im.alpha_composite(layer.im);c.d=ImageDraw.Draw(c.im)


def motion_poster():
    p=COLORS['light'];c=Canvas(1200,450,p['canvas'])
    c.text(56,40,'One object, from action to detail.',28,p['textPrimary'],'medium')
    c.text(56,93,'Matched expansion · 480 ms · ease-out',17,p['textSecondary'])
    button(c,80,230,240,'Share collection',p,icon='link')
    c.line(((367,256),(450,256)),p['controlBorder'],2)
    c.line(((438,245),(450,256),(438,267)),p['controlBorder'],2)
    share_panel(c,521,155,603,241,p)
    c.text(80,325,'Compact action',14,p['textSecondary'])
    c.text(521,408,'Reduced motion: show the final state immediately or crossfade.',14,p['textSecondary'])
    return c


def cubic_ease(progress):
    # Solve x(t) for the token's cubic-bezier(.22, 1, .36, 1).
    x1,y1,x2,y2=TOKENS['motion']['easeOut']
    lo,hi=0.,1.
    for _ in range(22):
        t=(lo+hi)/2
        x=3*(1-t)**2*t*x1+3*(1-t)*t*t*x2+t**3
        if x<progress: lo=t
        else: hi=t
    t=(lo+hi)/2
    return 3*(1-t)**2*t*y1+3*(1-t)*t*t*y2+t**3


def motion_frame(progress):
    p=COLORS['light'];c=Canvas(1000,480,p['canvas'],1)
    c.text(48,36,'From one action to its details.',28,p['textPrimary'],'medium')
    c.text(48,82,'The object keeps its origin as the surface expands.',17,p['textSecondary'])
    e=cubic_ease(progress)
    w=240+(650-240)*e;h=52+(270-52)*e
    x=(1000-w)/2;y=260-(h-52)/2
    if progress<.001:
        button(c,x,y,w,'Share collection',p,icon='link',h=h)
    else:
        def blend(a,b,t): return tuple(round(v+(u-v)*t) for v,u in zip(rgba(a),rgba(b)))
        bg=blend(p['action'],p['surfaceRaised'],e)
        c.rect((x,y,x+w,y+h),bg,16+12*e,p['divider'] if e>.8 else None)
        def lum(col):
            values=[v/255 for v in rgba(col)[:3]]
            values=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in values]
            return sum(v*k for v,k in zip(values,(.2126,.7152,.0722)))
        def contrast(col):
            a,b=sorted((lum(col),lum(bg)))
            return (b+.05)/(a+.05)
        fg=max((p['onAction'],p['textPrimary']),key=contrast)
        c.icon('link',x+16+8*e,y+16+8*e,20+4*e,fg)
        c.text(x+44+18*e,y+26+10*e,'Share collection',14+6*e,fg,'medium',anchor='lm')
        if progress>.3:
            # Content appears only after its enclosing surface has room.
            layer=Canvas(1000,480,'#00000000',1)
            layer.icon('close',x+w-44,y+25,20,p['textSecondary'])
            layer.text(x+24,y+81,'Bring someone into the conversation.',14,p['textSecondary'])
            for i,(label,ic) in enumerate((('Copy link','link'),('Invite someone','person'))):
                yy=y+123+i*61
                layer.rect((x+16,yy-9,x+w-16,yy+43),p['surfaceInset'],12)
                layer.icon(ic,x+29,yy+5,22,p['textSecondary'])
                layer.text(x+66,yy+16,label,17,p['textPrimary'],anchor='lm')
                layer.icon('chevron',x+w-44,yy+7,18,p['textSecondary'])
            alpha=min(1,(progress-.3)/.4)
            layer.im.putalpha(layer.im.getchannel('A').point(lambda a:round(a*alpha)))
            c.im.alpha_composite(layer.im)
    return c.im.convert('RGB')


def render_motion():
    # Each transition is exactly the 480ms signature token. Pause time is explanatory.
    phases=[(0,1200)] + [(i/12,40) for i in range(1,13)] + [(1,1500)] + [(1-i/12,40) for i in range(1,13)] + [(0,800)]
    images=[motion_frame(v) for v,_ in phases]
    # One palette prevents frame-to-frame color flicker. 128 colors keeps the GIF small.
    strip=Image.new('RGB',(1000,len(images)*480))
    for i,im in enumerate(images):strip.paste(im,(0,i*480))
    palette=strip.quantize(colors=128,method=Image.Quantize.MEDIANCUT)
    frames=[im.quantize(palette=palette,dither=Image.Dither.NONE) for im in images]
    frames[0].save(ASSETS/'matched-expansion.gif',save_all=True,append_images=frames[1:],duration=[d for _,d in phases],loop=0,optimize=True,disposal=2)


def main():
    ASSETS.mkdir(parents=True,exist_ok=True)
    screens=[screen_library(),screen_player(),screen_assistant()]
    for name,screen in zip(('library','player','assistant'),screens): screen.save(Path('screens')/(name+'.png'),full_resolution=True)
    overview(screens).save(Path('custom-ui-overview.png'))
    for theme in ('light','dark'):component_board(theme).save(Path('components-'+theme+'.png'))
    overlays_board().save(Path('forms-and-overlays.png'))
    motion_poster().save(Path('matched-expansion-still.png'))
    render_motion()
    for p in sorted(ASSETS.rglob('*')):
        if p.is_file(): print(f'{p.relative_to(ROOT)}: {p.stat().st_size:,} bytes')


if __name__=='__main__': main()
