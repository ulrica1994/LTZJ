"""
ShootGame  雷霆战机
1.搭建项目  512*768
2.绘制背景
  2.1 第一区域  1.2 back背景
  2.2 第五区域  5.1 drawBack()  绘制背景
  2.3 第一区域   1.3 BackY
  2.4 第五区域   5.1 drawBack 移动背景
3.英雄机Hero
   3.1 新建父类   FlyObject()类  继承
   3.2新建子类  Hero（）类继承  FlyObject
   3.3 第五区域  绘制英雄机
   3.4 Hero类中  step函数
   3.5 第四区域  调用stepAction
   3.6 ShootGame类  4.3.1 stepAction函数
   3.7  英雄机移动
   1.第四区域
   2.将鼠标坐标点赋值给英雄机
4.子弹 Bullet
   4.1新建类Bullet 继承FlyObject
   4.2 Setting==>bulletImage
   4.3 ShootGame 第一区域  bullets[]
   4.4 第四区域   4.3.2 enterAction
       生成飞行物
   4.5  第五区域  5.3 paintBullet
   4.6 Bullet类  step类
   4.7  第四区域  4.3.1调用子弹移动函数
        step函数
   4.8 第四区域  4.3.2 修改代码
       hero.shootBy()
   4.9 第一区域
5.敌机
   5.1  新建敌机类  Airplane 类
   5.2   ShootGame  第一区  flys[]
   5.3   第四区域   4.3.2 enterAction
         flys[]  存储对象
   5.4   第五区域   5.4 绘制飞行物
         paintFly()
   5.5   敌机移动
6.爱心
   6.1 新建类  Love  继承FlyObject
   6.2  ShootGame第四区域
        4.3.2  创建飞行物  代码块区域
               产生随机量   0，20
               rx<4    产生Love
               rx>4    产生Airplane
               添加在flys列表中
    6.3  Love类中    step函数
         爱心动画以及爱心移动
         爱心走S型
7.出界处理
     7.1 ShootGame  第四区域
         新建  4.3.3 outAction
     7.2 遍历飞行物（战机 爱心）
        英雄机子弹
        调用  outOfBounds函数
    7.3  如果outOfBounds函数返回值  True
        出界   删除列表对象
    7.4  outOfBounds
        子弹return   self.y<-self.height
        爱心return    self.y>768
        敌机return    self.y>768

10.boss机
    10.1 新建boss机类
        1. step函数
        0 < y < 400
        0 < x < 512-width
    2.生命值life 100
    10.2 ShootGame第一区域
        bss = [] Boss 机的列表
    10.3 第四区域 enterAction
        1.分数生成Boss
        score % 100 ==0：
        bss. append(Boss(screen,images))
        2.频率生成Boss
        enterIndex % 100 == 0
        bss.append(Boss(screen,images))
    10.4 第五区域 paintBoss()
        绘制Boss机
    10.5 第四区域 stepAction()
        调用Boss机走一步
    10.6 第四区域 hitAction
        子弹与Boss机碰撞  消失

11.Boss机子弹
    11.1 新建BossBullet类 Boss子弹类
    11.2 第一区域 bbls = []
    11.3 第四区域 enterAction
        len(bss) > 0 and enterIndex % 200 == 0:
        shootBy()
    11.4 第五区域 paintBossBullet()
    11.5 第四区域 stepAction 移动
    11.6 子弹与英雄机碰撞
        hitAction==>添加boss子弹
        hitHero(boss子弹)

课后作业：
1.碰撞  子弹与敌机爱心碰撞消失
"""

# 搭建项目框架512*768
import pygame,sys,random
from pygame.locals import *
from LTZJ.Setting import Setting
from LTZJ.Hero import Hero
from LTZJ.Airplane import Airplane
from LTZJ.Love import Love
from LTZJ.Award import Award
from LTZJ.Enemy import Enemy
from LTZJ.Boss import Boss


# 绘制背景
# 绘制背景函数drawback()
# backY
# 在drawback()移动背景
# 英雄机
## 新建父类 FlyObject()类  继承

screen = pygame.display.set_mode((512, 768), RESIZABLE, 0)
back = pygame.image.load("img/background.png")
heroImage = []
backY = 0

# 初始化工具类
setting = Setting()


# 英雄机Hero类初始化
hero = Hero(screen, setting.heroImages)

# 英雄机子弹列表
bullets = []

# Boss子弹列表
bbls = []

# 生成飞行物频率值
enterIndex = 0


# 飞行物列表
flys = []

# 爱心列表
loves = []

# 分数
score = 0

# boss机
bss = []

# 状态变量值
START = 0
RUNNING = 1
GAMEOVER = 2
state = START

# 状态背景
stateBack = pygame.image.load("img/start.png")


def init():
    pass

def action():
    global state
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        # 是否点击鼠标

        if event.type == pygame.MOUSEBUTTONDOWN:
            # 鼠标按下的具体按键
            # 单击
            leftFlag = pygame.mouse.get_pressed()[0]
            # 双击
            rightFlag = pygame.mouse.get_pressed()[2]

            # 判断状态
            if state == START and leftFlag:
                state = RUNNING
            elif state == RUNNING and leftFlag:
                state = START


    if state == RUNNING:
        '''业务处理'''
        stepAction()

        # 调用
        enterAction()

        # 碰撞检查
        hitAction()

        # 出界业务
        outAction()
        mx, my = pygame.mouse.get_pos()
        hero.moveTo(mx, my)


def stepAction():
    # 调用英雄机走一步
    hero.step()

    # 英雄子弹走一步
    for bt in bullets:
        bt.step()
    for fy in flys:
        fy.step()
    for lv in loves:
        lv.step()
    for bos in bss:
        bos.step()
    for bl in bbls:
        bl.step()

def enterAction():
    global enterIndex
    enterIndex += 1
    if enterIndex % 5 == 0:
        # 创建子弹添加到列表中
        bullets.extend(hero.shootBy(setting.bulletImage))

    if len(bss) > 0 and enterIndex % 40 == 0:
        for bos in bss:
            if bos.y > -bos.height:
                bbls.extend(bos.shootBy(setting.bblsImages))

    if enterIndex % 50 == 0:
        rx = random.randint(0, 20)
        if rx < 4:
            flys.append(Love(screen, setting.loveImages))
        else:
            flys.append(Airplane(screen, setting.airImages))

    if enterIndex % 200 == 0:
        bss.append(Boss(screen, setting.bossImages))

# 出界函数
def outAction():
    for fly in flys:
        if fly.outofBounds():
            flys.remove(fly)

    for bt in bullets:
        if bt.outofBounds():
            bullets.remove(bt)

    for bl in bbls:
        if bl.outofBounds():
            bbls.remove(bl)

def hitAction():
    for bt in bullets:
        hit(bt)
    for bbt in bbls:
        hitHero(bbt)

def hit(bt):
    # 设置碰撞变量
    hitIndex = -1
    # 遍历所有的飞行物
    for fly in flys:
        if fly.hitBy(bt):
            # 将碰撞的飞行物的下标给hitIndex
            hitIndex = flys.index(fly)

    global score
    if hitIndex != -1:
        fly = flys[hitIndex]
        if isinstance(fly, Enemy):
            # 敌机处理
            score += fly.getScore()

        if isinstance(fly, Award):
            # 爱心处理
            if fly.getAward() == Award.LIFE:
                # 生命值奖励
                hero.life += 10
            else:
                # 火力值奖励
                hero.doubleFire = 1000
        # 判断类型
        # 删除飞行物和子弹
        del flys[hitIndex]
        # 删除子弹
        bullets.remove(bt)

    # Boss与子弹碰撞
    hitIndex = -1
    # 遍历所有的BOSS
    for bos in bss:
        # 判断碰撞
        if bos.hitBy(bt):
            hitIndex = bss.index(bos)
    if hitIndex != -1:
        # 减少Boss生命值
        bss[hitIndex].life -= 10
        # 判断是否死亡
        if bss[hitIndex].life < 0:
            # Boss消失
            del bss[hitIndex]
        # 子弹消失
        if bullets.count(bt) > 0:
            bullets.remove(bt)


def hitHero(bbt):
    global state, stateBack
    # 碰撞英雄
    if hero.hitBy(bbt):
        hero.life -= 10
        # 消除子弹
        bbls.remove(bbt)
        if hero.life < 0:
            stateBack = pygame.image.load("img/gameover.png")
            state = GAMEOVER


def menu():
    pygame.display.set_caption("雷霆战机")
    while True:
        screen.fill((0, 0, 0))
        action()
        paint()
        pygame.display.update()

def paint():
    global state
    if state == RUNNING:
        # 绘制背景图
        paintBack()
        #绘制英雄机
        hero.blitMe()

        # 绘制英雄机子弹
        paintBullet()
        # 绘制敌机
        paintFly()
        #绘制爱心
        paintLove()

        # 绘制Boss
        paintBoss()
        # 绘制Boss子弹
        paintBossBullet()
        # 绘制状态
        paintState()
    elif state == START:
        screen.blit(stateBack, (0, 0))
    elif state == GAMEOVER:
        screen.blit(stateBack, (0, 0))

def paintBack():
    global backY
    # 修改坐标值
    backY += 1
    screen.blit(back, (0, backY))
    screen.blit(back, (0, -768 + backY))

    # 循环
    if backY > 768:
        backY = 0

# 绘制英雄机子弹
def paintBullet():
    for i in range(len(bullets)):
        bullets[i].blitMe()

def paintFly():
    for fy in flys:
        fy.blitMe()

def paintLove():
    for love in loves:
        love.blitMe()

def paintState():
    if hero.doubleFire > 0:
        firestr = "双倍"
    else:
        firestr = "单倍"
    # 字体初始化
    pygame.font.init()
    font = pygame.font.Font("simhei.ttf", 28)
    fontRead = font.render("分数：%d"%score, True, (255, 0, 0))
    screen.blit(fontRead, (100, 100))

    fontLife = font.render("生命：%d"%hero.life, True, (255, 0, 0))
    screen.blit(fontLife, (100, 150))

    fontFire = font.render(firestr, True, (255, 0, 0))
    screen.blit(fontFire, (100, 200))

def paintBoss():
    for bos in bss:
        bos.blitMe()

def paintBossBullet():
    for bl in bbls:
        bl.blitMe()


if __name__ =='__main__':
    init()
    menu()
