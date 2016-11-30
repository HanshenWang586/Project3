import pygame
from pygame.locals import*
pygame.mixer.pre_init(32000,-16,2,2**9)
pygame.init()
pygame.mixer.set_num_channels(6)

import time, math, random, os

def Lerp(a, b, p):
  return(a+(b-a)*p)

def Lerp_lists(a,b,p):
    new_list=[]
    index=0
    while True:
        info = Lerp(a[index], b[index], p)
        new_list.append(info)
        index+=1
        if index>len(a)-1 or index>len(b)-1:
            break
    return new_list



class Sequencer(object):
  def __init__(self,world):
    self.world = world

    self.left_sounds=[]
    self.right_sounds=[]
    self.miss_sound=pygame.mixer.Sound("BeatMiss.ogg")
    for x in range(5):
      self.left_sounds.append(pygame.mixer.Sound("H_PaddleImpact"+str(x+1)+".ogg"))
      self.right_sounds.append(pygame.mixer.Sound("H_PaddleImpact"+str(x+1)+".ogg"))
    self.prev_sound=random.randint(0,4)

  def get_sound(self):
    new_list=range(5)
    new_list.remove(self.prev_sound)
    sound = random.choice(new_list)
    self.prev_sound=sound
    return sound

  def play_sound(self, s, left=True):
    v=0.3#volume
    if left:
      chn = self.left_sounds[s].play()
      if chn: chn.set_volume(0.75*v,0.25*v)
    else:
      chn = self.right_sounds[s].play()
      if chn: chn.set_volume(0.25*v,0.75*v)

  def miss(self):
    print ("MISSED!")
    self.miss_sound.play()
    

class Score(object):
  def __init__(self, world):
    self.world = world
    self.score=0
    self.prev_score=0

    self.concecutive=0

    self.font=[]
    self.places=10
    for x in xrange(10):
      self.font.append(pygame.image.load("font/"+str(x)+".png"))
      self.font[-1].convert_alpha()
    self.set_image()

  def update(self):
    if self.score!=self.prev_score:
      self.set_image()
      self.prev_score=self.score

  def set_image(self):
    #SCORE
    self.score_image=pygame.Surface([40*self.places-10,40])
    self.score_image.convert_alpha()
    self.score_image.set_colorkey([0,0,0])

    score = str(self.score)
    score = score[max(0,len(score)-self.places):]
    score = "0"*(self.places-len(score))+score
    for x in xrange(self.places):#number of places on the score
      place=10**(self.places-x)
      index=int(score[x])
      self.score_image.blit(self.font[index], [x*40,0])

    #STREAK
    self.streak_image=pygame.Surface([40*3-10,40])
    self.streak_image.convert_alpha()
    self.streak_image.set_colorkey([0,0,0])

    conc = str(self.concecutive)
    conc = conc[max(0,len(conc)-3):]
    conc = "0"*(3-len(conc))+conc
    for x in xrange(3):#3 being the number of places on the streak
      place=10**(3-x)
      index=int(conc[x])
      self.streak_image.blit(self.font[index], [x*40,0])

    #FPS
    #self.fps_image=pygame.Surface([40*3-10,40])
    #self.fps_image.convert_alpha()
    #self.fps_image.set_colorkey([0,0,0])

    #fps = str(int(self.world.clock.get_fps()))
    #fps = fps[max(0,len(fps)-3):]
    #fps = "0"*(3-len(fps))+fps
    #for x in xrange(3):#3 being the number of places on the streak
    #  place=10**(3-x)
    #  index=int(fps[x])
    #  self.fps_image.blit(self.font[index], [x*40,0])
    

  def add_score(self):
    self.concecutive+=1
    self.score+=self.concecutive
    self.set_image()

  def reset_streak(self):
    self.concecutive/=2
    self.set_image()
    self.world.seq.miss()

  def render(self):
    rect = self.score_image.get_rect(topleft=[10,10])
    self.world.rects.append(rect)
    self.world.screen.blit(self.score_image, rect)

    rect = self.streak_image.get_rect(topleft=[10,self.world.screen_size[1]-10-40])
    self.world.rects.append(rect)
    self.world.screen.blit(self.streak_image, rect)

    #rect = self.fps_image.get_rect(topright=[self.world.screen_size[0]-10,10])
    #self.world.rects.append(rect)
    #self.world.screen.blit(self.fps_image, rect)


class Beat(object):
  def __init__(self, world, song, bpm, delay=0.0):
    self.world = world
    self.song = song
    self.bpm = float(bpm)
    self.delay=0.0

    self.played=False

    pygame.mixer.music.load(self.song)

    self.start_time=0.0
    self.tick_count=0.0#16 in a measure
    self.prev_tick_count=0.0
    self.beat_count=0.0#4 in a measure

  def play(self):
    self.played=True
    pygame.mixer.music.stop() 
    while not pygame.mixer.music.get_busy():
      pygame.mixer.music.play()
      self.start_time=time.time()-self.delay

  def update(self):
    if self.start_time!=0.0:
      #t = time.time()
      #dif = t-self.start_time
      dif = (pygame.mixer.music.get_pos()/1000.0)-self.delay
      self.beat_count=(self.bpm/60.0)*dif
      self.tick_count=self.beat_count*4.0
      if pygame.mixer.music.get_endevent():
        pygame.event.post(pygame.event.Event(QUIT))
      

  def render(self):
    pass



class Padel(object):
  def __init__(self, world):
    self.world = world
    self.pos = self.world.screen_size[1]/2
    self.size=125
    self.limits=[50,self.world.screen_size[1]-50]

    self.main_color=[255,100,0]
    self.color=list(self.main_color)

    self.anim = 0
    self.anim_amount = 1*self.world.framerate
    
    self.set_rect()

  def set_rect(self):
    left = 40
    
    if self.pos-(self.size/2)<self.limits[0]:
        self.rect = [left,self.limits[0],10,self.size]
    elif self.pos+(self.size/2)>self.limits[1]:
        self.rect = [left,self.limits[1]-self.size,10,self.size]
    else:
        self.rect = [left,self.pos-(self.size/2),10,self.size]

  def hit(self):
    self.anim=int(self.anim_amount)

  def update(self):
    if self.anim>0:
      self.anim -= 1
    p=self.anim/float(self.anim_amount)
    self.color = Lerp_lists([255,127,0],[255,255,255],p)
      
    self.pos = self.world.mouse_pos[1]
    """
    if len(self.world.bits)==0:
        pos = self.world.screen_size[1]/2
    else:
        try:
            b=None
            for bit in self.world.bits:
                if bit.reflected:
                    pass
                else:
                    b=bit
                    break
            if b==None:
                raise "BLA BLA BLA"
            else:
                pos = (b.height+b.rect[1])/2+b.rect[3]/2
        except:
            pos = self.world.screen_size[1]/2
    
    self.pos = Lerp(self.pos, pos, 0.9)#Lerp(0.5,0.9, math.sin(math.radians((time.time()*360)%360))))
    """
    self.set_rect()

  def render(self):
    self.world.rects.append(pygame.draw.rect(self.world.screen, self.color, self.rect))



################ BITS ##################3
    
class Bit(object):
  def __init__(self, world, tick, height):
    self.world = world
    self.tick = tick+(self.world.beat.bpm/60.0)*0.05
    self.height=height*50.0+75.0
    self.limits=[50.0,self.world.screen_size[1]-50.0]
    self.reflected=False
    self.missed=False
    self.dead=False
    self.sound=None
    self.rect=None
    self.prev_rect=None
    self.anim=0
    self.anim_amount=1*self.world.framerate
    self.main_color=[255,200,0]
    self.color=list(self.main_color)
    self.init()

  def init(self):
    pass

  def hit(self):
    self.anim=int(self.anim_amount)

  def update(self):
    if self.rect!=None:
        self.prev_rect = list(self.rect)
    self.set_rect()
    if self.anim>=0:
      p=self.anim/float(self.anim_amount)
      self.color = Lerp_lists(self.main_color,[255,255,255],p)
      self.anim -= 1
    if self.rect!=None:
      if not self.reflected and not self.missed and self.prev_rect!=None and 2*self.rect[0]-self.prev_rect[0]<=50.0:
        if (self.rect[1]+self.prev_rect[1])/2+10.0>=self.world.padel.rect[1] and (self.rect[1]+self.prev_rect[1])/2<=self.world.padel.rect[1]+self.world.padel.rect[3]:
          #it hit the padel!
          #print "hit"
          self.hit()
          self.world.score.add_score()#adds to the score
          self.world.padel.hit()#hits the padel
          self.reflected=True#reflects the bit
          s = self.world.seq.get_sound()#plays the sound
          self.sound=s
          self.world.seq.play_sound(self.sound)
        else:
          #it missed it...
          #print "missed"
          self.world.score.reset_streak()
          self.missed=True
      if self.reflected and self.rect[0]>=self.world.screen_size[0]:
        self.dead=True
        self.world.seq.play_sound(self.sound, False)
      if self.missed and self.rect[0]+10<0:
        self.dead=True

  def is_visible(self):
    wr=pygame.Rect(0,0,self.world.screen_size[0], self.world.screen_size[1])
    if pygame.Rect(self.rect).colliderect(wr):
      return True
    return False   
      
  def set_rect(self):
    n=(self.rect==None)
    if not self.reflected:
      t = self.tick-self.world.beat.tick_count
    else:
      t = self.world.beat.tick_count-self.tick
    p = t/16.0
    pos = Lerp(50.0,float(self.world.screen_size[0]),p)
    
    self.rect = [pos,self.height,10.0,10.0]
    self.correct_rect()

  def correct_rect(self):
    if self.rect[1]<self.limits[0]+5:
        self.rect[1]=self.limits[0]+5
    elif self.rect[1]>self.limits[1]-5:
        self.rect[1]=self.limits[1]-5

  def render(self):
    if self.is_visible():
      #if self.rect!=None and self.prev_rect==None:
      self.world.rects.append(pygame.draw.rect(self.world.screen, self.color, self.rect))
      """
      elif self.rect!=None and self.prev_rect!=None:
        MinX=min(self.rect[0], self.prev_rect[0])
        MinY=min(self.rect[1], self.prev_rect[1])
        MaxX=max(self.rect[0]+self.rect[2], self.prev_rect[0]+self.prev_rect[2])
        MaxY=max(self.rect[1]+self.rect[3], self.prev_rect[1]+self.prev_rect[3])
        MaxWidth=max(self.rect[2],self.rect[3],self.prev_rect[2],self.prev_rect[3])
        self.world.rects.append([MinX-2,MinY-2,MaxX-MinX+4,MaxY-MinY+4])
        pygame.draw.rect(self.world.screen, self.color, self.rect)
        self.world.rects.append(pygame.draw.line(self.world.screen,
                                                    self.color,
                                                    [self.rect[0]+self.rect[2]/2,self.rect[1]+self.rect[3]/2],
                                                    [self.prev_rect[0]+self.prev_rect[2]/2,self.prev_rect[1]+self.prev_rect[3]/2],
                                                    MaxWidth))
      """
class BounceBit1(Bit):
  def init(self):
    self.main_color=[0,200,200]

  def set_rect(self):
    n=(self.rect==None)
    if not self.reflected:
      t = self.tick-self.world.beat.tick_count
    else:
      t = self.world.beat.tick_count-self.tick
    p = t/16.0
    x = Lerp(50.0,float(self.world.screen_size[0]),p)
    Hb= float(self.height)
    y = Lerp(self.world.screen_size[1]-60.0,Hb,abs(math.cos(math.radians(90.0*p*4))))
    self.rect = [x,y,10.0,10.0]
    self.correct_rect()
    

class BounceBit2(Bit):
  def init(self):
    self.main_color=[0,200,200]

  def set_rect(self):
    n=(self.rect==None)
    if not self.reflected:
      t = self.tick-self.world.beat.tick_count
    else:
      t = self.world.beat.tick_count-self.tick
    p = t/16.0
    x = Lerp(50.0,self.world.screen_size[0],p)
    Hb= float(self.height)
    y = Lerp(50.0,Hb,abs(math.cos(math.radians(90.0*p*4))))
    self.rect = [x,y,10.0,10.0]
    self.correct_rect()


class WaveBit1(Bit):
  def init(self):
    self.main_color=[255,0,255]

  def set_rect(self):
    n=(self.rect==None)
    t = self.tick-self.world.beat.tick_count
    p = t/16.0
    if not self.reflected:
      x = Lerp(50.0,self.world.screen_size[0],p)
    else:
      x = Lerp(50.0,self.world.screen_size[0],-p)
    Hb= float(self.height)
    y = Hb+Lerp(0,50,math.sin(math.radians(180*p*4)))
    self.rect = [x,y,10.0,10.0]
    self.correct_rect()


class WaveBit2(Bit):
  def init(self):
    self.main_color=[255,0,255]

  def set_rect(self):
    n=(self.rect==None)
    t = self.tick-self.world.beat.tick_count
    p = t/16.0
    if not self.reflected:
      x = Lerp(50.0,self.world.screen_size[0],p)
    else:
      x = Lerp(50.0,self.world.screen_size[0],-p)
    Hb= float(self.height)
    y = Hb+Lerp(0,50,math.sin(math.radians(180*p*4+180)))
    self.rect = [x,y,10.0,10.0]
    self.correct_rect()
      
class BlinkBit(Bit):
  def init(self):
    self.main_color=[0,255,0]

  def is_visible(self):
    wr=pygame.Rect(0,0,self.world.screen_size[0], self.world.screen_size[1])
    if pygame.Rect(self.rect).colliderect(wr) and self.world.beat.beat_count%1<0.5:
      return True
    return False
  

class PadelBit1(Bit):
  def init(self):
    self.main_color=[255,255,255]

  def set_rect(self):
    n=(self.rect==None)
    if n:
      self.rect=[1000,0,10,10]
      
    if not self.reflected:
      t = self.tick-self.world.beat.tick_count
    else:
      t = self.world.beat.tick_count-self.tick
    p = t/16.0
    x = Lerp(50.0,float(self.world.screen_size[0]),p)
    Hb= float(self.height)
    if self.is_visible():
      y = Lerp(self.rect[1],self.world.padel.rect[1]+self.world.padel.rect[3]/2,(3.0/self.world.framerate))
    else:
      y = Hb
    self.rect = [x,y,10.0,10.0]
    self.correct_rect()
      

class PadelBit2(Bit):
  def init(self):
    self.main_color=[255,255,255]

  def set_rect(self):
    n=(self.rect==None)
    if n:
      self.rect=[1000,0,10,10]
    if not self.reflected:
      t = self.tick-self.world.beat.tick_count
    else:
      t = self.world.beat.tick_count-self.tick
    p = t/16.0
    x = Lerp(50.0,float(self.world.screen_size[0]),p)
    Hb= float(self.height)
    y = Lerp(self.rect[1],self.height+(self.height-(self.world.padel.rect[1]+self.world.padel.rect[3]/2))-5,(3.0/self.world.framerate))
    self.rect = [x,y,10.0,10.0]
    self.correct_rect()


class FastBit(Bit):
  def init(self):
    self.main_color=[100,255,100]

  def set_rect(self):
    n=(self.rect==None)
    if not self.reflected:
      t = self.tick-self.world.beat.tick_count
    else:
      t = self.world.beat.tick_count-self.tick
    p = t/16.0
    x = Lerp(50.0,float(self.world.screen_size[0])*2,p)
    Hb= float(self.height)
    self.rect = [x,Hb,10.0,10.0]
    self.correct_rect()




##########################################################

class World(object):
  def __init__(self):
    #SET UP __INIT__
      self.screen_size = (800,600)#(1200,600)
      os.environ['SDL_VIDEO_CENTERED'] = '1'
      self.screen = pygame.display.set_mode(self.screen_size, FULLSCREEN|SRCALPHA, 16)
      while not pygame.display.get_active():
        time.sleep(0.1)
      pygame.display.set_caption("PY.TRIP BEAT","PY.TRIP BEAT")
    
      self.clock = pygame.time.Clock()
      self.framerate=60

      self.bg_color = [0,0,0]
      self.screen.fill(self.bg_color)

      #SET UP ENTITIES
      self.reset()
      self.run()
      
  def reset(self):
      self.padel = Padel(self)
      self.score = Score(self)
      self.beat = Beat(self, "song.ogg", 120.0)
      self.seq=Sequencer(self)

      self.paused=False
      
      self.bits=[]

      self.load_bits()
      
      time.sleep(1)
      
      self.beat.play()


  def load_bits(self):
    
    f = file("info.txt")

    l=f.readline()
    y=0
    while l!="":
      print (len(l))
      for x in xrange(len(l)):
        t=float(x)+32#time when the bit is hit
        h=float(y)#the bits height when hit
        
        if l[x]=="a":
          self.bits.append(Bit(self,t,h))
        elif l[x]=="B":
          self.bits.append(BounceBit1(self,t,h))
        elif l[x]=="b":
          self.bits.append(BounceBit2(self,t,h))
        elif l[x]=="c":
          self.bits.append(WaveBit1(self,t,h))
        elif l[x]=="C":
          self.bits.append(WaveBit2(self,t,h))
        elif l[x]=="d":
          self.bits.append(BlinkBit(self,t,h))
        elif l[x]=="e":
          self.bits.append(PadelBit1(self,t,h))
        elif l[x]=="E":
          self.bits.append(PadelBit2(self,t,h))
        elif l[x]=="f":
          self.bits.append(FastBit(self,t,h))
        
      l=f.readline()
      y+=1
    
    """
    for x in xrange(128):
        p=(x/float(64))
        difficulty=int(Lerp(1,16,p))
        choice = list("_"*(16-difficulty)+"@"*difficulty)
        random.shuffle(choice)
        for y in xrange(16):
            if choice[y]=="@":
                h=random.randint(1,8)
                t=float(x*16+y)+32#time when the bit is hit
                pick = random.choice(list("abBcCdEef"))
                if pick=="a":
                  self.bits.append(Bit(self,t,h))
                elif pick=="B":
                  self.bits.append(BounceBit1(self,t,h))
                elif pick=="b":
                  self.bits.append(BounceBit2(self,t,h))
                elif pick=="c":
                  self.bits.append(WaveBit1(self,t,h))
                elif pick=="C":
                  self.bits.append(WaveBit2(self,t,h))
                elif pick=="d":
                  self.bits.append(BlinkBit(self,t,h))
                elif pick=="e":
                  self.bits.append(PadelBit1(self,t,h))
                elif pick=="E":
                  self.bits.append(PadelBit2(self,t,h))
                elif pick=="f":
                  self.bits.append(FastBit(self,t,h))
    """

  def run(self):
      # RUN MAIN LOOP
      while True:
        self.clock.tick(self.framerate)
        self.events = pygame.event.get()
        self.keys=pygame.key.get_pressed()
        self.mouse_pos=pygame.mouse.get_pos()
        self.mouse_but = pygame.mouse.get_pressed()
        self.rects=[]


        #UPDATE
        #self.score.set_image()#only for framerate
        
        if pygame.mouse.get_focused():#if the player is focused
          if self.mouse_pos[0]!=self.screen_size[0]/2:
            pygame.mouse.set_pos([self.screen_size[0]/2,self.mouse_pos[1]])
            self.mouse_pos=pygame.mouse.get_pos()
          if self.paused:
            print ("--- unpausing ---")
            pygame.mixer.music.unpause()
            self.paused=False
          pygame.mouse.set_visible(False)
        else:
          if not self.paused:
            print ("--- pausing ---")
            self.paused=True
            pygame.mixer.music.pause()
            pygame.mouse.set_visible(True)
          
        self.padel.update()
        self.score.update()
        self.beat.update()
        x=len(self.bits)-1
        while x>=0:
          bit = self.bits[x]
          bit.update()
          if bit.dead:
            self.bits.pop(x)
          x-=1


        #RENDER
        for bit in self.bits:
          bit.render()
        self.padel.render()
        self.score.render()

        pygame.display.flip()

        self.screen.fill([0,0,0])

        #for rect in self.rects:
        #  self.screen.fill(self.bg_color, rect)
        
        #img = pygame.Surface([self.screen_size[0], self.screen_size[1]])
        #img.convert_alpha()
        #img.set_alpha(64.0*(60.0/self.framerate))#200
        
        #self.screen.blit(img,[0,0])


        #EVENT HANDLER UPDATE
        for event in self.events:
          if event.type==KEYDOWN or event.type==QUIT:
            if event.type==QUIT or event.key==K_ESCAPE:
                pygame.quit()
                return
           
            if event.type==KEYDOWN and event.key==114:
                self.reset()


world = World()

    
    
