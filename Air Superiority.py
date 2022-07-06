#------------------------------------------------------------------------------#
# Name: Air Superiority.py                                                     #
# Purpose: Single player, 2D adventure game                                    #
#                                                                              #
# Author: Gyulumyan.M                                                          #
#                                                                              #
# Created: 18/06/19                                                            #
#------------------------------------------------------------------------------#
# Tips and Tricks:                                                             #
# - Stay away from enemies, always time your shots properly                    #
# - Stay on the sides of the game when fighting the first and seond behemoth,  #
#   they will have a hard time hitting you from here                           #
# - Hit as many planes with the secondary of level 3 to get a lot of points    #
# - Fly on the top left for the final level to avoid being hit by the behemoth #
# - Bombs fall vertically on level 4, so hit the behemoth with all of them     #
#------------------------------------------------------------------------------#
import pygame

pygame.init()

# Game General Settings
# Start Up
size = (1000,740)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Air Superiority")
clock = pygame.time.Clock()
second_behemoth_logic = False
# Primary and Secondary Weapons
shoot = False
fire = False
# Health Systems
player_hp = 10.0
behemoth_hp = 50.0
secondary_count = 5
# Main Page and Introduction
end = False
main_end = False
intro_end = False
controls_end = False
# Level 1
lvl_1_intro_end = False
lvl_1_start = False
lvl_1_end = False
# Level 2
lvl_2_intro_end = False
lvl_2_start = False
lvl_2_end = False
# Level 3
lvl_3_intro_end = False
lvl_3_start = False
lvl_3_end = False
# Level 4
lvl_4_intro_end = False
lvl_4_start = False
lvl_4_end = False
# Ending
ending_intro_end = False
ending_end = False
# Points and Victories Count
lvl_points = 0
total_points = 0
lvl_victories = 0
total_victories = 0


# Colors
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)


# Load Images
# Player
red_baron = pygame.image.load("textures/player/red_baron.png")
red_baron_rev = pygame.image.load("textures/player/red_baron_rev.png")
spitfire = pygame.image.load("textures/player/spitfire.png")
spitfire_rev = pygame.image.load("textures/player/spitfire_rev.png")
saber = pygame.image.load("textures/player/sabre.png")
saber_rev = pygame.image.load("textures/player/sabre_rev.png")
pak_fa = pygame.image.load("textures/player/pak_fa.png")
pak_fa_rev = pygame.image.load("textures/player/pak_fa_rev.png")
# Enemy
sopwith = pygame.image.load("textures/enemy/sopwith.png")
sopwith_rev = pygame.image.load("textures/enemy/sopwith_rev.png")
airship = pygame.image.load("textures/enemy/airship.png")
airship_rev = pygame.image.load("textures/enemy/airship_rev.png")
bf_109 = pygame.image.load("textures/enemy/bf-109.png")
bf_109_rev = pygame.image.load("textures/enemy/bf-109_rev.png")
junker_88 = pygame.image.load("textures/enemy/junkers_88.png")
junker_88_rev = pygame.image.load("textures/enemy/junkers_88_rev.png")
mig_15 = pygame.image.load("textures/enemy/mig_15.png")
mig_15_rev = pygame.image.load("textures/enemy/mig_15_rev.png")
f_35 = pygame.image.load("textures/enemy/f_35.png")
f_35_rev = pygame.image.load("textures/enemy/f_35_rev.png")
warship = pygame.image.load("textures/enemy/warship.png")
warship_rev = pygame.image.load("textures/enemy/warship_rev.png")
# Player Level Plane
lvl_1_plane = red_baron
lvl_2_plane = spitfire
lvl_3_plane = saber
lvl_4_plane = pak_fa
# Enemy Level Plane
# Level 1
enemy = sopwith
lvl_1_plane_enemy = sopwith
lvl_1_plane_enemy_2 = sopwith
lvl_1_plane_enemy_3 = sopwith
behemoth = airship
# Level 2
lvl_2_plane_enemy = bf_109
lvl_2_plane_enemy_2 = bf_109
lvl_2_plane_enemy_3 = bf_109
behemoth_2 = junker_88
# Level 3
lvl_3_plane_enemy = mig_15
lvl_3_plane_enemy_2 = mig_15
lvl_3_plane_enemy_3 = mig_15
lvl_3_plane_enemy_4 = mig_15
lvl_3_plane_enemy_5 = mig_15
lvl_3_plane_enemy_6 = mig_15
# Level 4
lvl_4_plane_enemy = f_35
lvl_4_plane_enemy_2 = f_35
lvl_4_plane_enemy_3 = f_35
lvl_4_plane_enemy_4 = f_35
behemoth_3 = warship
# Other
# Icons
red_baron_icon = pygame.image.load("textures/other/red_baron_icon.png")
spitfire_icon = pygame.image.load("textures/other/spitfire_icon.png")
sabre_icon = pygame.image.load("textures/other/f_86_sabre_icon.png")
su_57_icon = pygame.image.load("textures/other/su_57_icon.png")
icon = red_baron_icon
# Player Weapons
player_projectile = pygame.image.load("textures/other/projectile.png")
player_projectile_rev = pygame.image.load("textures/other/projectile_rev.png")
player_primary = pygame.image.load("textures/other/bullet.png")
player_primary_rev = pygame.image.load("textures/other/bullet_rev.png")
# Pages, Buttons, and Status
main_title = pygame.image.load("textures/other/air_superiority.png")
intro_title = pygame.image.load("textures/other/intro_title.png")
controls_title = pygame.image.load("textures/other/controls_title.png")
red_baron_intro_page = pygame.image.load("textures/other/red_baron_intro_page.png")
background_1 = pygame.image.load("textures/other/sky1.png")
battle_of_britain_intro_page = pygame.image.load("textures/other/battle_of_britain_intro_page.png")
background_2 = pygame.image.load("textures/other/sky2.png")
fortunate_son_intro_page = pygame.image.load("textures/other/fortunate_son_intro_page.png")
background_3 = pygame.image.load("textures/other/sky3.png")
baltic_brawl_intro_page = pygame.image.load("textures/other/baltic_brawl_intro_page.png")
background_4 = pygame.image.load("textures/other/sky4.png")
button = pygame.image.load("textures/other/button.png")
status_bar = pygame.image.load("textures/other/background.png")
# Player Weapons Set Variables
bomb = player_projectile
bullet = player_primary


# Load Sounds
# Songs
german = pygame.mixer.Sound("sounds/songs/German March.wav")
british = pygame.mixer.Sound("sounds/songs/British March.wav")
american = pygame.mixer.Sound("sounds/songs/American March.wav")
russian = pygame.mixer.Sound("sounds/songs/Russian March.wav")
cruel_angels_thesis = pygame.mixer.Sound("sounds/songs/Cruel Angel's Thesis.wav")
ending = pygame.mixer.Sound("sounds/songs/ending.wav")
# Sound FX
bang = pygame.mixer.Sound("sounds/sound fx/bang.wav")
explosion = pygame.mixer.Sound("sounds/sound fx/explosion.wav")


# Load Fonts
bertholdr_mainzer_fraktur = pygame.font.Font("fonts/Bertholdr Mainzer Fraktur.ttf", 25)
bertholdr_mainzer_fraktur_titles = pygame.font.Font("fonts/Bertholdr Mainzer Fraktur.ttf", 50)
bertholdr_mainzer_fraktur_titles_mega = pygame.font.Font("fonts/Bertholdr Mainzer Fraktur.ttf", 80)
bertholdr_mainzer_fraktur_little = pygame.font.Font("fonts/Bertholdr Mainzer Fraktur.ttf", 15)
helvetica_standard = pygame.font.Font("fonts/Helvetica.ttf", 15)


# Score System
scores_sheet = open("scores.txt","a+")
scores = scores_sheet.readlines()
scores_list = []
high_score = int(0)
for number in scores:
    number = number.rstrip("\n")
    scores_list.append(int(number))
for item in scores_list:
    if item > high_score:
        high_score = int(item)


# Coordinates and Speed
# Player Coordinates
player_x = 0
player_y = 0
# Enemy Coordinates
enemy_x = 600
enemy_y = 0
enemy_2_x = 200
enemy_2_y = 500
enemy_3_x = 400
enemy_3_y = 200
enemy_4_x = 400
enemy_4_y = 200
enemy_5_x = 100
enemy_5_y = 300
enemy_6_x = 700
enemy_6_y = 400
behemoth_x = 100
behemoth_y = 300
# Bomb Coordinates
bomb_x = 0
bomb_y = 0
# Primary Bullet Coordinates
primary_x = 0
primary_y = 0
# Player Speed
player_speed_x = 0
player_speed_y = 0
# Enemy Speed
enemy_speed_x = 0
enemy_speed_y = 0
enemy_2_speed_x = 0
enemy_2_speed_y = 0
enemy_3_speed_x = 0
enemy_3_speed_y = 0
enemy_4_speed_x = 0
enemy_4_speed_y = 0
enemy_5_speed_x = 0
enemy_5_speed_y = 0
enemy_6_speed_x = 0
enemy_6_speed_y = 0
behemoth_speed_x = 35
behemoth_speed_y = 10
# Bomb Speed
bomb_speed_x = 0
bomb_speed_y = 0
# Primary Speed
primary_speed_x = 0
primary_speed_y = 0


# Draw and Logic Functions
def drawPlayerPlane(player_plane,x,y):
     screen.blit(player_plane,[x,y])

def drawEnemyPlane(enemy,enemy_plane_pos_x,enemy_plane_pos_y,enemy_plane_speed_x,plane,plane_rev,health,points):
    # Swith Enemy Plane Picture
    if enemy_plane_speed_x <= 0:
        enemy = plane_rev
        screen.blit(enemy,[enemy_plane_pos_x,enemy_plane_pos_y])
    if enemy_plane_speed_x >= 0:
        enemy = plane
        screen.blit(enemy,[enemy_plane_pos_x,enemy_plane_pos_y])
    # Enemy Attack
    if enemy == plane:
        if (player_x - 600 <= enemy_plane_pos_x  and player_x >= enemy_plane_pos_x ) and (player_y + 82 <= enemy_plane_pos_y + 82 and player_y + 82 >= enemy_plane_pos_y + 82):
                bang.play()
                health -= 1.0
                points -= 10
    if enemy == plane_rev:
        if (enemy_plane_pos_x - 600 <= player_x and enemy_plane_pos_x >= player_x ) and (player_y + 82 <= enemy_plane_pos_y + 82 and player_y + 82 >= enemy_plane_pos_y + 82):
                bang.play()
                health -= 1.0
                points -= 10
    return (enemy,enemy_plane_pos_x,enemy_plane_pos_y,enemy_plane_speed_x,plane,plane_rev,health,points)

def enemyPlaneLogic(enemy_plane_pos_x,enemy_plane_pos_y,enemy_plane_speed_x,enemy_plane_speed_y):
    # Enemy Plane Movement
    enemy_plane_pos_x += enemy_plane_speed_x
    enemy_plane_pos_y += enemy_plane_speed_y
    if enemy_plane_pos_x >= 920:
        enemy_plane_speed_x *= -1
    if enemy_plane_pos_x <= 0:
        enemy_plane_speed_x *= -1
    if enemy_plane_pos_y >= 560 or enemy_plane_pos_y <= 0:
        enemy_plane_speed_y *= -1
    return (enemy_plane_pos_x,enemy_plane_pos_y,enemy_plane_speed_x,enemy_plane_speed_y)

def drawBehemoth(boss,pos_x,pos_y,speed_x,pic,pic_rev):
    # Switch Behemoth Picture
    if speed_x <= 0:
        boss = pic_rev
        screen.blit(boss,[pos_x,pos_y])
    if speed_x >= 0:
        boss = pic
        screen.blit(boss,[pos_x,pos_y])

def behemothLogic(boss,pos_x,pos_y,speed_x,speed_y,pic,pic_rev,hp,enemy_hp,level,secondary,primary,primary_pos_x,bomb_pos_x,primary_pos_y,bomb_pos_y):
    # Behemoth Movement
    pos_x += speed_x
    pos_y += speed_y
    if pos_x >= 648:
        speed_x *= -1
    if pos_x <= 0:
        speed_x *= -1
    if pos_y >= 501 or pos_y <= 0:
        speed_y *= -1
    # Behemoth Primary Attack
    if (player_x >= pos_x and player_x <= pos_x + 352) and (player_y >= pos_y and player_y <= pos_y + 99):
        bang.play()
        hp -= 0.50
    # Behemoth Hit With Secondary
    if (bomb_pos_x >= pos_x and bomb_pos_x <= pos_x + 352) and (bomb_pos_y >= pos_y and bomb_pos_y <= pos_y + 99):
        bomb_pos_x = -10
        bomb_pos_y = -10
        bomb_speed_x = 0
        bomb_speed_y = 0
        explosion.play()
        secondary = False
        enemy_hp -= 10.0
    # Behemoth Hit With Primary
    if (primary_pos_x >= pos_x and primary_pos_x <= pos_x + 352) and (primary_pos_y >= pos_y and primary_pos_y <= pos_y + 99):
        primary_pos_x = -10
        primary_pos_y = -10
        primary_speed_x = 0
        primary_speed_y = 0
        explosion.play()
        primary = False
        enemy_hp -= 5.0
    # Behemoth Death
    if enemy_hp <= -5.0:
        level = True
    # Behemoth Secondary (level 2 and 4 only)
    if second_behemoth_logic == True:
        if ((player_x - 600 <= pos_x + 99 and player_x >= pos_x + 99) and (player_y + 99 <= pos_y + 99 and player_y + 99 >= pos_y + 99)) \
        or ((player_x + 600 >= pos_x + 99 and player_x <= pos_x + 99) and (player_y + 99 >= pos_y + 99 and player_y + 99 <= pos_y + 99)):
            hp -= 0.5
            bang.play()
        if ((player_y + 600 >= pos_y + 99 and player_y + 99 <= pos_y + 99) and (player_x + 99 >= pos_x + 200 and player_x <= pos_x + 200)) \
        or ((player_y - 600 <= pos_y + 99 and player_y + 99 >= pos_y + 99) and (player_x + 99 >= pos_x + 200 and player_x <= pos_x + 200)):
            hp -= 0.25
            bang.play()
    return (boss,pos_x,pos_y,speed_x,speed_y,pic,pic_rev,hp,enemy_hp,level,secondary,primary,primary_pos_x,bomb_pos_x,primary_pos_y,bomb_pos_y)

def drawStatus():
    screen.blit(status_bar,[0,600])
    screen.blit(icon,[500,620])
    player_health = bertholdr_mainzer_fraktur.render("Health: " + str(player_hp), True, red)
    player_lvl_points = bertholdr_mainzer_fraktur.render("Lvl Points: " + str(lvl_points), True, red)
    player_lvl_victories = bertholdr_mainzer_fraktur.render("Lvl Victories: " + str(lvl_victories), True, red)
    secondary_ct = bertholdr_mainzer_fraktur.render("Secondary Count: " + str(secondary_count), True, red)
    boss_health = bertholdr_mainzer_fraktur.render("Behemoth Health: " + str(behemoth_hp), True, red)
    points_total = bertholdr_mainzer_fraktur.render("Total Points: " + str(total_points), True, red)
    victories_totel = bertholdr_mainzer_fraktur.render("Total Victories: " + str(total_victories), True, red)
    screen.blit(player_health,[790,610])
    screen.blit(player_lvl_points,[790,640])
    screen.blit(player_lvl_victories,[790,670])
    screen.blit(secondary_ct,[790,700])
    screen.blit(boss_health,[100,610])
    screen.blit(points_total,[100,640])
    screen.blit(victories_totel,[100,670])

def drawButton(x,y):
    screen.blit(button,[x,y])


# Player Intro Song
cruel_angels_thesis.play()

# Game Start
while not end:
    # Title Page
    while not main_end:
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                main_end = True
                intro_end = True
                controls_end = True
                lvl_1_intro_end = True
                lvl_1_end = True
                lvl_2_intro_end = True
                lvl_2_end = True
                lvl_3_intro_end = True
                lvl_3_end = True
                lvl_4_intro_end = True
                lvl_4_end = True
                ending_intro_end = True
                ending_end = True
                end = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Go to Introduction Page
                if (mouse_x >= 700 and mouse_x <= 900) and (mouse_y >= 650 and mouse_y <= 700):
                    main_end = True
        screen.blit(main_title,[0,0,1000,740])
        drawButton(700,650)
        pygame.display.flip()
        clock.tick(10)

    # Introduction Page
    while not intro_end:
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                intro_end = True
                controls_end = True
                lvl_1_intro_end = True
                lvl_1_end = True
                lvl_2_intro_end = True
                lvl_2_end = True
                lvl_3_intro_end = True
                lvl_3_end = True
                lvl_4_intro_end = True
                lvl_4_end = True
                ending_intro_end = True
                ending_end = True
                end = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Go to Controls Page
                if (mouse_x >= 700 and mouse_x <= 900) and (mouse_y >= 650 and mouse_y <= 700):
                    intro_end = True
        # All Game Introduction Text and Display
        introduction = bertholdr_mainzer_fraktur_titles_mega.render("Air Superiority", True, red)
        description = helvetica_standard.render("Air superiority is a historically", True, red)
        description_2 = helvetica_standard.render("fictional adventure game designed", True, red)
        description_3 = helvetica_standard.render("around you piloting the most iconic", True, red)
        description_4 = helvetica_standard.render("fighter planes to have ever existed. Fly through", True, red)
        description_5 = helvetica_standard.render("four historic settings, each with their own unique ", True, red)
        description_6 = helvetica_standard.render("enemies, bosses, and difficulty.", True, red)
        description_7 = helvetica_standard.render("You will have 10 health, each plane takes", True, red)
        description_8 = helvetica_standard.render("one shot to destroy, but the boss/behemoth has 50 health,", True, red)
        description_9 = helvetica_standard.render("your primary will deal 5 damage, seconday 10, but you only have 5", True, red)
        description_10 = helvetica_standard.render("shots. Shooting enemy planes with the primary delivers 100 points, secondaries", True, red)
        description_11 = helvetica_standard.render("150. You will be able to progress to the next level after the behemoth is defeated.", True, red)
        description_12 = helvetica_standard.render("The highscore to beat is " + str(high_score), True, red)
        screen.blit(intro_title,[0,0])
        screen.blit(introduction,[440,50])
        screen.blit(description,[10,400])
        screen.blit(description_2,[10,420])
        screen.blit(description_3,[10,440])
        screen.blit(description_4,[10,460])
        screen.blit(description_5,[10,480])
        screen.blit(description_6,[10,500])
        screen.blit(description_7,[10,520])
        screen.blit(description_8,[10,540])
        screen.blit(description_9,[10,560])
        screen.blit(description_10,[10,580])
        screen.blit(description_11,[10,600])
        screen.blit(description_12,[10,640])
        drawButton(700,650)
        pygame.display.flip()
        clock.tick(10)

    # Controls Page
    while not controls_end:
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                controls_end = True
                lvl_1_intro_end = True
                lvl_1_end = True
                lvl_2_intro_end = True
                lvl_2_end = True
                lvl_3_intro_end = True
                lvl_3_end = True
                lvl_4_intro_end = True
                lvl_4_end = True
                ending_intro_end = True
                ending_end = True
                end = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Go to Level 1 Intro Page
                if (mouse_x >= 700 and mouse_x <= 900) and (mouse_y >= 650 and mouse_y <= 700):
                    controls_end = True
                    cruel_angels_thesis.stop()
        # All Controls Page Texts
        controls = bertholdr_mainzer_fraktur_titles.render("Controls", True, black)
        w = helvetica_standard.render("w = up", True, black)
        a = helvetica_standard.render("a = left", True, black)
        s = helvetica_standard.render("s = down", True, black)
        d =  helvetica_standard.render("d = right", True, black)
        space = helvetica_standard.render("space = fire primary", True, black)
        b  = helvetica_standard.render("b = fire secondary bomb", True, black)
        q  = helvetica_standard.render("q = start level", True, black)
        e  = helvetica_standard.render("e = restart level", True, black)
        esc  = helvetica_standard.render("esc = skip level", True, black)
        screen.blit(controls_title,[0,0,1000,740])
        screen.blit(controls,[400,40])
        screen.blit(w,[100,100])
        screen.blit(a,[100,120])
        screen.blit(s,[100,140])
        screen.blit(d,[100,160])
        screen.blit(space,[100,180])
        screen.blit(b,[100,200])
        screen.blit(q,[100,220])
        screen.blit(e,[100,240])
        screen.blit(esc,[100,260])
        drawButton(700,650)
        pygame.display.flip()
        clock.tick(10)

    # Level One Intro Page
    while not lvl_1_intro_end:
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                lvl_1_intro_end = True
                lvl_1_end = True
                lvl_2_intro_end = True
                lvl_2_end = True
                lvl_3_intro_end = True
                lvl_3_end = True
                lvl_4_intro_end = True
                lvl_4_end = True
                ending_intro_end = True
                ending_end = True
                end = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Go to Level 1
                if (mouse_x >= 700 and mouse_x <= 900) and (mouse_y >= 650 and mouse_y <= 700):
                    lvl_1_intro_end = True
        screen.blit(red_baron_intro_page,[0,0])
        drawButton(700,650)
        pygame.display.flip()
        clock.tick(10)

    # Level One
    while not lvl_1_end:
        """
        All Game Events Under Here
        """
        icon = red_baron_icon
        bomb_x_pos = player_x
        bomb_y_pos = player_y
        primary_x_pos = player_x
        primary_y_pos = player_y
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                lvl_1_end = True
                lvl_2_intro_end = True
                lvl_2_end = True
                lvl_3_intro_end = True
                lvl_3_end = True
                lvl_4_intro_end = True
                lvl_4_end = True
                ending_intro_end = True
                ending_end = True
                end = True
            # All Keybaord Movement
            # Key Down
            elif event.type == pygame.KEYDOWN:
                # Skip Level 1
                if event.key == pygame.K_ESCAPE:
                    lvl_1_end = True
                    german.stop()
                # Start Level 1
                elif event.key == pygame.K_q and lvl_1_start == False:
                    german.play()
                    player_speed_x = 5
                    enemy_speed_x = 10
                    enemy_speed_y = 10
                    enemy_2_speed_x = 10
                    enemy_2_speed_y = 10
                    enemy_3_speed_x = 10
                    enemy_3_speed_y = 10
                    lvl_1_start = True
                    behemoth_x = 100
                    behemoth_y = 300
                    behemoth_speed_x = 35
                    behemoth_speed_y = 10
                # Restart Level
                elif event.key == pygame.K_e:
                    german.stop()
                    player_hp = 10.0
                    behemoth_hp = 50.0
                    player_speed_x = 0
                    player_speed_y = 0
                    player_x = 0
                    player_y = 0
                    enemy_x = 600
                    enemy_y = 0
                    enemy_speed_x = 0
                    enemy_speed_y = 0
                    enemy_2_x = 200
                    enemy_2_y = 500
                    enemy_2_speed_x = 0
                    enemy_2_speed_y = 0
                    enemy_3_x = 400
                    enemy_3_y = 200
                    enemy_3_speed_x = 0
                    enemy_3_speed_y = 0
                    lvl_1_plane = red_baron
                    lvl_1_plane_enemy = sopwith
                    lvl_1_plane_enemy_2 = sopwith
                    lvl_1_plane_enemy_3 = sopwith
                    lvl_victories = 0
                    lvl_1_start = False
                    shoot = False
                    fire = False
                    lvl_victories = 0
                    lvl_points = 0
                    secondary_count = 5
                    behemoth_x = 100
                    behemoth_y = 300
                    behemoth_speed_x = 0
                    behemoth_speed_y = 0
                # Player Movement
                elif event.key == pygame.K_w and lvl_1_start == True:
                    player_speed_y = -20
                elif event.key == pygame.K_s and lvl_1_start == True:
                    player_speed_y = 20
                elif event.key == pygame.K_a and lvl_1_start == True:
                    player_speed_x = -20
                    lvl_1_plane = red_baron_rev
                elif event.key == pygame.K_d and lvl_1_start == True:
                    player_speed_x = 20
                    lvl_1_plane = red_baron
                # Shooting Primary
                elif event.key == pygame.K_SPACE and fire == False and lvl_1_start == True:
                    if lvl_1_plane == red_baron:
                        bullet = player_primary
                        fire = True
                        primary_x = primary_x_pos
                        primary_y = primary_y_pos
                        primary_speed_x = 100
                        primary_speed_y = 0
                        bang.play()
                    elif lvl_1_plane == red_baron_rev:
                        bullet = player_primary_rev
                        fire = True
                        primary_x = primary_x_pos
                        primary_y = primary_y_pos
                        primary_speed_x = -100
                        primary_speed_y = 0
                        bang.play()
                # Shooting Secondary
                elif event.key == pygame.K_b and shoot == False and lvl_1_start == True and secondary_count > 0:
                    secondary_count -= 1
                    if lvl_1_plane == red_baron:
                        bomb = player_projectile
                        shoot = True
                        bomb_x = bomb_x_pos
                        bomb_y = bomb_y_pos
                        bomb_speed_x = 25
                        bomb_speed_y = 10
                        bang.play()
                    elif lvl_1_plane == red_baron_rev:
                        bomb = player_projectile_rev
                        shoot = True
                        bomb_x = bomb_x_pos
                        bomb_y = bomb_y_pos
                        bomb_speed_x = -25
                        bomb_speed_y = 10
                        bang.play()
            # Player Movement (Key Up)
            elif event.type == pygame.KEYUP and lvl_1_start == True:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player_speed_y = 0
                elif event.key == pygame.K_d:
                    player_speed_x = 5
                elif event.key == pygame.K_a:
                    player_speed_x = -5
                elif event.key == pygame.K_SPACE:
                    fire = True
                elif event.key == pygame.K_b:
                    shoot = True
        """
        All Events Above Here
        All Game Logic Under Here
        """
        # Player, Enemy, and Entity Movement
        # Player Movement
        player_x += player_speed_x
        player_y += player_speed_y
        # Player Movement Limit
        if player_x >= 920:
            player_x = 920
        if player_x <= 0:
            player_x = 0
        if player_y >= 560:
            player_y = 560
        if player_y <= 0:
            player_y = 0
        # Primary Fire Movement
        primary_x += primary_speed_x
        primary_y += primary_speed_y
        # Primary Fire Movement Limit
        if primary_x >= 1000 or primary_x <= 0:
            fire = False
        # Primary Fire Hitting Enemies
        if (primary_x >= enemy_x and primary_x <= enemy_x + 80) and (primary_y >= enemy_y - 40 and primary_y <= enemy_y + 40):
            enemy_speed_x = 0
            enemy_speed_y = 0
            enemy_x = 2000
            enemy_y = 2000
            fire = False
            lvl_victories += 1
            lvl_points += 100
            explosion.play()
        if (primary_x >= enemy_2_x and primary_x <= enemy_2_x + 80) and (primary_y >= enemy_2_y - 40 and primary_y <= enemy_2_y + 40):
            enemy_2_speed_x = 0
            enemy_2_speed_y = 0
            enemy_2_x = 2000
            enemy_2_y = 2000
            fire = False
            lvl_victories += 1
            lvl_points += 100
            explosion.play()
        if (primary_x >= enemy_3_x and primary_x <= enemy_3_x + 80) and (primary_y >= enemy_3_y - 40 and primary_y <= enemy_3_y + 40):
            enemy_3_speed_x = 0
            enemy_3_speed_y = 0
            enemy_3_x = 2000
            enemy_3_y = 2000
            fire = False
            lvl_victories += 1
            lvl_points += 100
            explosion.play()
        # Secondary Fire Movement
        bomb_x += bomb_speed_x
        bomb_y += bomb_speed_y
        # Secondary Fire Movement Limit
        if bomb_x >= 1000 or bomb_x <= 0 or bomb_y >= 570:
            shoot = False
        # Secondary Hitting Enemies
        if (bomb_x >= enemy_x and bomb_x <= enemy_x + 80) and (bomb_y >= enemy_y - 40 and bomb_y <= enemy_y + 40):
            enemy_speed_x = 0
            enemy_speed_y = 0
            enemy_x = 2000
            enemy_y = 2000
            shoot = False
            lvl_victories += 1
            lvl_points += 150
            explosion.play()
        if (bomb_x >= enemy_2_x and bomb_x <= enemy_2_x + 80) and (bomb_y >= enemy_2_y - 40 and bomb_y <= enemy_2_y + 40):
            enemy_2_speed_x = 0
            enemy_2_speed_y = 0
            enemy_2_x = 2000
            enemy_2_y = 2000
            shoot = False
            lvl_victories += 1
            lvl_points += 150
            explosion.play()
        if (bomb_x >= enemy_3_x and bomb_x <= enemy_3_x + 80) and (bomb_y >= enemy_3_y - 40 and bomb_y <= enemy_3_y + 40):
            enemy_3_speed_x = 0
            enemy_3_speed_y = 0
            enemy_3_x = 2000
            enemy_3_y = 2000
            shoot = False
            lvl_victories += 1
            lvl_points += 150
            explosion.play()
        # Player Health System
        if player_hp <= 0.0:
            german.stop()
            player_speed_x = 0
            player_speed_y = 0
            player_x = 0
            player_y = 0
            enemy_x = 600
            enemy_y = 0
            enemy_speed_x = 0
            enemy_speed_y = 0
            enemy_2_x = 200
            enemy_2_y = 500
            enemy_2_speed_x = 0
            enemy_2_speed_y = 0
            enemy_3_x = 400
            enemy_3_y = 200
            enemy_3_speed_x = 0
            enemy_3_speed_y = 0
            lvl_1_plane = red_baron
            lvl_1_plane_enemy = sopwith
            lvl_1_plane_enemy_2 = sopwith
            lvl_1_plane_enemy_3 = sopwith
            lvl_1_start = False
            shoot = False
            fire = False
            player_hp = 10.0
            behemoth_hp = 50.0
            lvl_victories = 0
            lvl_points = 0
            secondary_count = 5
            behemoth_x = 100
            behemoth_y = 300
            behemoth_speed_x = 0
            behemoth_speed_y = 0
        """
        All Game Logic Above Here
        All Drawing Under Here
        """
        screen.blit(background_1,[0,0])
        # Enemy Plane 1
        drawEnemyPlane(lvl_1_plane_enemy,enemy_x,enemy_y,enemy_speed_x,sopwith,sopwith_rev,player_hp,lvl_points)
        player_hp = drawEnemyPlane(lvl_1_plane_enemy,enemy_x,enemy_y,enemy_speed_x,sopwith,sopwith_rev,player_hp,lvl_points)[6]
        lvl_points = drawEnemyPlane(lvl_1_plane_enemy,enemy_x,enemy_y,enemy_speed_x,sopwith,sopwith_rev,player_hp,lvl_points)[7]
        enemy_x = enemyPlaneLogic(enemy_x,enemy_y,enemy_speed_x,enemy_speed_y)[0]
        enemy_y = enemyPlaneLogic(enemy_x,enemy_y,enemy_speed_x,enemy_speed_y)[1]
        enemy_speed_x = enemyPlaneLogic(enemy_x,enemy_y,enemy_speed_x,enemy_speed_y)[2]
        enemy_speed_y = enemyPlaneLogic(enemy_x,enemy_y,enemy_speed_x,enemy_speed_y)[3]
        # Enemy Plane 2
        drawEnemyPlane(lvl_1_plane_enemy_2,enemy_2_x,enemy_2_y,enemy_2_speed_x,sopwith,sopwith_rev,player_hp,lvl_points)
        player_hp = drawEnemyPlane(lvl_1_plane_enemy_2,enemy_2_x,enemy_2_y,enemy_2_speed_x,sopwith,sopwith_rev,player_hp,lvl_points)[6]
        lvl_points = drawEnemyPlane(lvl_1_plane_enemy_2,enemy_2_x,enemy_2_y,enemy_2_speed_x,sopwith,sopwith_rev,player_hp,lvl_points)[7]
        enemy_2_x = enemyPlaneLogic(enemy_2_x,enemy_2_y,enemy_2_speed_x,enemy_2_speed_y)[0]
        enemy_2_y = enemyPlaneLogic(enemy_2_x,enemy_2_y,enemy_2_speed_x,enemy_2_speed_y)[1]
        enemy_2_speed_x = enemyPlaneLogic(enemy_2_x,enemy_2_y,enemy_2_speed_x,enemy_2_speed_y)[2]
        enemy_2_speed_y = enemyPlaneLogic(enemy_2_x,enemy_2_y,enemy_2_speed_x,enemy_2_speed_y)[3]
        # Enemy Plane 3
        drawEnemyPlane(lvl_1_plane_enemy_3,enemy_3_x,enemy_3_y,enemy_3_speed_x,sopwith,sopwith_rev,player_hp,lvl_points)
        player_hp = drawEnemyPlane(lvl_1_plane_enemy_3,enemy_3_x,enemy_3_y,enemy_3_speed_x,sopwith,sopwith_rev,player_hp,lvl_points)[6]
        lvl_points = drawEnemyPlane(lvl_1_plane_enemy_3,enemy_3_x,enemy_3_y,enemy_3_speed_x,sopwith,sopwith_rev,player_hp,lvl_points)[7]
        enemy_3_x = enemyPlaneLogic(enemy_3_x,enemy_3_y,enemy_3_speed_x,enemy_3_speed_y)[0]
        enemy_3_y = enemyPlaneLogic(enemy_3_x,enemy_3_y,enemy_3_speed_x,enemy_3_speed_y)[1]
        enemy_3_speed_x = enemyPlaneLogic(enemy_3_x,enemy_3_y,enemy_3_speed_x,enemy_3_speed_y)[2]
        enemy_3_speed_y = enemyPlaneLogic(enemy_3_x,enemy_3_y,enemy_3_speed_x,enemy_3_speed_y)[3]
        # Player Plane
        drawPlayerPlane(lvl_1_plane,player_x,player_y)
        # Behemoth
        if lvl_victories >= 3:
            drawBehemoth(behemoth,behemoth_x,behemoth_y,behemoth_speed_x,airship,airship_rev)
            behemoth = behemothLogic(behemoth,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,airship,airship_rev,player_hp,behemoth_hp,lvl_1_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[0]
            behemoth_x = behemothLogic(behemoth,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,airship,airship_rev,player_hp,behemoth_hp,lvl_1_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[1]
            behemoth_y = behemothLogic(behemoth,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,airship,airship_rev,player_hp,behemoth_hp,lvl_1_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[2]
            behemoth_speed_x = behemothLogic(behemoth,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,airship,airship_rev,player_hp,behemoth_hp,lvl_1_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[3]
            behemoth_speed_y = behemothLogic(behemoth,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,airship,airship_rev,player_hp,behemoth_hp,lvl_1_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[4]
            airship = behemothLogic(behemoth,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,airship,airship_rev,player_hp,behemoth_hp,lvl_1_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[5]
            airship_rev = behemothLogic(behemoth,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,airship,airship_rev,player_hp,behemoth_hp,lvl_1_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[6]
            player_hp = behemothLogic(behemoth,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,airship,airship_rev,player_hp,behemoth_hp,lvl_1_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[7]
            behemoth_hp = behemothLogic(behemoth,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,airship,airship_rev,player_hp,behemoth_hp,lvl_1_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[8]
            lvl_1_end = behemothLogic(behemoth,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,airship,airship_rev,player_hp,behemoth_hp,lvl_1_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[9]
            shoot = behemothLogic(behemoth,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,airship,airship_rev,player_hp,behemoth_hp,lvl_1_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[10]
            fire = behemothLogic(behemoth,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,airship,airship_rev,player_hp,behemoth_hp,lvl_1_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[11]
            primary_x = behemothLogic(behemoth,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,airship,airship_rev,player_hp,behemoth_hp,lvl_1_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[12]
            bomb_x = behemothLogic(behemoth,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,airship,airship_rev,player_hp,behemoth_hp,lvl_1_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[13]
            primary_y = behemothLogic(behemoth,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,airship,airship_rev,player_hp,behemoth_hp,lvl_1_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[14]
            bomb_y = behemothLogic(behemoth,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,airship,airship_rev,player_hp,behemoth_hp,lvl_1_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[15]
        # Display Stats
        drawStatus()
        # Shoot and Reset Primary and Secondary Shoot
        if shoot == True:
            screen.blit(bomb,[bomb_x,bomb_y])
        if fire == True:
            screen.blit(bullet,[primary_x,primary_y])
        # End of Level 1
        if lvl_1_end == True:
            german.stop()
            bang.stop()
            explosion.stop()
        """
        All Drawing Above Here
        Ending Under Here
        """
        pygame.display.flip()
        clock.tick(10)
    # Level Two Intro
    while not lvl_2_intro_end:
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                lvl_2_intro_end = True
                lvl_2_end = True
                lvl_3_intro_end = True
                lvl_3_end = True
                lvl_4_intro_end = True
                lvl_4_end = True
                ending_intro_end = True
                ending_end = True
                end = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Set Level 2 Variables and Go to it
                if (mouse_x >= 700 and mouse_x <= 900) and (mouse_y >= 650 and mouse_y <= 700):
                    total_points += lvl_points
                    total_victories += lvl_victories
                    player_hp = 10.0
                    behemoth_hp = 50.0
                    player_speed_x = 0
                    player_speed_y = 0
                    player_x = 0
                    player_y = 0
                    enemy_x = 300
                    enemy_y = 100
                    enemy_speed_x = 0
                    enemy_speed_y = 0
                    enemy_2_x = 400
                    enemy_2_y = 540
                    enemy_2_speed_x = 0
                    enemy_2_speed_y = 0
                    enemy_3_x = 600
                    enemy_3_y = 200
                    enemy_3_speed_x = 0
                    enemy_3_speed_y = 0
                    lvl_2_plane = spitfire
                    lvl_2_plane_enemy = bf_109
                    lvl_2_plane_enemy_2 = bf_109
                    lvl_2_plane_enemy_3 = bf_109
                    lvl_victories = 0
                    lvl_2_start = False
                    shoot = False
                    fire = False
                    lvl_victories = 0
                    lvl_points = 0
                    secondary_count = 5
                    lvl_2_intro_end = True
                    behemoth_x = 100
                    behemoth_y = 300
                    behemoth_speed_x = 0
                    behemoth_speed_y = 0
        screen.blit(battle_of_britain_intro_page,[0,0])
        drawButton(700,650)
        pygame.display.flip()
        clock.tick(10)
    # Level Two
    while not lvl_2_end:
        """
        All Game Events Under Here
        """
        icon = spitfire_icon
        bomb_x_pos = player_x
        bomb_y_pos = player_y
        primary_x_pos = player_x
        primary_y_pos = player_y
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                lvl_2_end = True
                lvl_3_intro_end = True
                lvl_3_end = True
                lvl_4_intro_end = True
                lvl_4_end = True
                ending_intro_end = True
                ending_end = True
                end = True
            # All Keybaord Movement
            # Key Down
            elif event.type == pygame.KEYDOWN:
                # Skip Level 2
                if event.key == pygame.K_ESCAPE:
                    british.stop()
                    lvl_2_end = True
                # Start Level 2
                elif event.key == pygame.K_q and lvl_2_start == False:
                    british.play()
                    player_speed_x = 5
                    enemy_speed_x = 15
                    enemy_speed_y = 15
                    enemy_2_speed_x = 15
                    enemy_2_speed_y = 15
                    enemy_3_speed_x = 15
                    enemy_3_speed_y = 15
                    lvl_2_start = True
                    behemoth_x = 100
                    behemoth_y = 300
                    behemoth_speed_x = 35
                    behemoth_speed_y = 5
                    second_behemoth_logic = True
                # Restart Level
                elif event.key == pygame.K_e:
                    british.stop()
                    player_hp = 10.0
                    behemoth_hp = 50.0
                    player_speed_x = 0
                    player_speed_y = 0
                    player_x = 0
                    player_y = 0
                    enemy_x = 300
                    enemy_y = 100
                    enemy_speed_x = 0
                    enemy_speed_y = 0
                    enemy_2_x = 400
                    enemy_2_y = 540
                    enemy_2_speed_x = 0
                    enemy_2_speed_y = 0
                    enemy_3_x = 600
                    enemy_3_y = 200
                    enemy_3_speed_x = 0
                    enemy_3_speed_y = 0
                    lvl_2_plane = spitfire
                    lvl_2_plane_enemy = bf_109
                    lvl_2_plane_enemy_2 = bf_109
                    lvl_2_plane_enemy_3 = bf_109
                    lvl_victories = 0
                    lvl_2_start = False
                    shoot = False
                    fire = False
                    lvl_victories = 0
                    lvl_points = 0
                    secondary_count = 5
                    behemoth_x = 100
                    behemoth_y = 300
                    behemoth_speed_x = 0
                    behemoth_speed_y = 0
                # Player Movement
                elif event.key == pygame.K_w and lvl_2_start == True:
                    player_speed_y = -20
                elif event.key == pygame.K_s and lvl_2_start == True:
                    player_speed_y = 20
                elif event.key == pygame.K_a and lvl_2_start == True:
                    player_speed_x = -20
                    lvl_2_plane = spitfire_rev
                elif event.key == pygame.K_d and lvl_2_start == True:
                    player_speed_x = 20
                    lvl_2_plane = spitfire
                # Shooting Primary
                elif event.key == pygame.K_SPACE and fire == False and lvl_2_start == True:
                    if lvl_2_plane == spitfire:
                        bullet = player_primary
                        fire = True
                        primary_x = primary_x_pos
                        primary_y = primary_y_pos
                        primary_speed_x = 100
                        primary_speed_y = 0
                        bang.play()
                    elif lvl_2_plane == spitfire_rev:
                        bullet = player_primary_rev
                        fire = True
                        primary_x = primary_x_pos
                        primary_y = primary_y_pos
                        primary_speed_x = -100
                        primary_speed_y = 0
                        bang.play()
                # Shooting Secondary
                elif event.key == pygame.K_b and shoot == False and lvl_2_start == True and secondary_count > 0:
                    secondary_count -= 1
                    if lvl_2_plane == spitfire:
                        bomb = player_projectile
                        shoot = True
                        bomb_x = bomb_x_pos
                        bomb_y = bomb_y_pos
                        bomb_speed_x = 35
                        bomb_speed_y = 0
                        bang.play()
                    elif lvl_2_plane == spitfire_rev:
                        bomb = player_projectile_rev
                        shoot = True
                        bomb_x = bomb_x_pos
                        bomb_y = bomb_y_pos
                        bomb_speed_x = -35
                        bomb_speed_y = 0
                        bang.play()
            # Player Movement (Key Up)
            elif event.type == pygame.KEYUP and lvl_2_start == True:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player_speed_y = 0
                elif event.key == pygame.K_d:
                    player_speed_x = 5
                elif event.key == pygame.K_a:
                    player_speed_x = -5
                elif event.key == pygame.K_SPACE:
                    fire = True
                elif event.key == pygame.K_b:
                    shoot = True
        """
        All Events Above Here
        All Game Logic Under Here
        """
        # Player, Enemy, and Entity Movement
        # Player Movement
        player_x += player_speed_x
        player_y += player_speed_y
        # Player Movement Limit
        if player_x >= 920:
            player_x = 920
        if player_x <= 0:
            player_x = 0
        if player_y >= 560:
            player_y = 560
        if player_y <= 0:
            player_y = 0
        # Primary Fire Movement
        primary_x += primary_speed_x
        primary_y += primary_speed_y
        # Primary Fire Movement Limit
        if primary_x >= 1000 or primary_x <= 0:
            fire = False
        # Primary Fire Hitting Enemies
        if (primary_x >= enemy_x and primary_x <= enemy_x + 80) and (primary_y >= enemy_y - 40 and primary_y <= enemy_y + 40):
            enemy_speed_x = 0
            enemy_speed_y = 0
            enemy_x = 2000
            enemy_y = 2000
            fire = False
            lvl_victories += 1
            lvl_points += 100
            explosion.play()
        if (primary_x >= enemy_2_x and primary_x <= enemy_2_x + 80) and (primary_y >= enemy_2_y - 40 and primary_y <= enemy_2_y + 40):
            enemy_2_speed_x = 0
            enemy_2_speed_y = 0
            enemy_2_x = 2000
            enemy_2_y = 2000
            fire = False
            lvl_victories += 1
            lvl_points += 100
            explosion.play()
        if (primary_x >= enemy_3_x and primary_x <= enemy_3_x + 80) and (primary_y >= enemy_3_y - 40 and primary_y <= enemy_3_y + 40):
            enemy_3_speed_x = 0
            enemy_3_speed_y = 0
            enemy_3_x = 2000
            enemy_3_y = 2000
            fire = False
            lvl_victories += 1
            lvl_points += 100
            explosion.play()
        # Secondary Fire Movement
        bomb_x += bomb_speed_x
        bomb_y += bomb_speed_y
        # Secondary Fire Movement Limit
        if bomb_x >= 1000 or bomb_x <= 0 or bomb_y >= 570:
            shoot = False
        # Secondary Hitting Enemies
        if (bomb_x >= enemy_x and bomb_x <= enemy_x + 80) and (bomb_y >= enemy_y - 40 and bomb_y <= enemy_y + 40):
            enemy_speed_x = 0
            enemy_speed_y = 0
            enemy_x = 2000
            enemy_y = 2000
            shoot = False
            lvl_victories += 1
            lvl_points += 150
            explosion.play()
        if (bomb_x >= enemy_2_x and bomb_x <= enemy_2_x + 80) and (bomb_y >= enemy_2_y - 40 and bomb_y <= enemy_2_y + 40):
            enemy_2_speed_x = 0
            enemy_2_speed_y = 0
            enemy_2_x = 2000
            enemy_2_y = 2000
            shoot = False
            lvl_victories += 1
            lvl_points += 150
            explosion.play()
        if (bomb_x >= enemy_3_x and bomb_x <= enemy_3_x + 80) and (bomb_y >= enemy_3_y - 40 and bomb_y <= enemy_3_y + 40):
            enemy_3_speed_x = 0
            enemy_3_speed_y = 0
            enemy_3_x = 2000
            enemy_3_y = 2000
            shoot = False
            lvl_victories += 1
            lvl_points += 150
            explosion.play()
        # Player Health System
        if player_hp <= 0.0:
            british.stop()
            player_hp = 10.0
            behemoth_hp = 50.0
            player_speed_x = 0
            player_speed_y = 0
            player_x = 0
            player_y = 0
            enemy_x = 300
            enemy_y = 100
            enemy_speed_x = 0
            enemy_speed_y = 0
            enemy_2_x = 400
            enemy_2_y = 540
            enemy_2_speed_x = 0
            enemy_2_speed_y = 0
            enemy_3_x = 600
            enemy_3_y = 200
            enemy_3_speed_x = 0
            enemy_3_speed_y = 0
            lvl_2_plane = spitfire
            lvl_2_plane_enemy = bf_109
            lvl_2_plane_enemy_2 = bf_109
            lvl_2_plane_enemy_3 = bf_109
            lvl_victories = 0
            lvl_2_start = False
            shoot = False
            fire = False
            lvl_victories = 0
            lvl_points = 0
            secondary_count = 5
            behemoth_x = 100
            behemoth_y = 300
            behemoth_speed_x = 0
            behemoth_speed_y = 0
        """
        All Game Logic Above Here
        All Drawing Under Here
        """
        screen.blit(background_2,[0,0])
        # Enemy Plane 1
        drawEnemyPlane(lvl_2_plane_enemy,enemy_x,enemy_y,enemy_speed_x,bf_109,bf_109_rev,player_hp,lvl_points)
        player_hp = drawEnemyPlane(lvl_2_plane_enemy,enemy_x,enemy_y,enemy_speed_x,bf_109,bf_109_rev,player_hp,lvl_points)[6]
        lvl_points = drawEnemyPlane(lvl_2_plane_enemy,enemy_x,enemy_y,enemy_speed_x,bf_109,bf_109_rev,player_hp,lvl_points)[7]
        enemy_x = enemyPlaneLogic(enemy_x,enemy_y,enemy_speed_x,enemy_speed_y)[0]
        enemy_y = enemyPlaneLogic(enemy_x,enemy_y,enemy_speed_x,enemy_speed_y)[1]
        enemy_speed_x = enemyPlaneLogic(enemy_x,enemy_y,enemy_speed_x,enemy_speed_y)[2]
        enemy_speed_y = enemyPlaneLogic(enemy_x,enemy_y,enemy_speed_x,enemy_speed_y)[3]
        # Enemy Plane 2
        drawEnemyPlane(lvl_2_plane_enemy_2,enemy_2_x,enemy_2_y,enemy_2_speed_x,bf_109,bf_109_rev,player_hp,lvl_points)
        player_hp = drawEnemyPlane(lvl_2_plane_enemy_2,enemy_2_x,enemy_2_y,enemy_2_speed_x,bf_109,bf_109_rev,player_hp,lvl_points)[6]
        lvl_points = drawEnemyPlane(lvl_2_plane_enemy_2,enemy_2_x,enemy_2_y,enemy_2_speed_x,bf_109,bf_109_rev,player_hp,lvl_points)[7]
        enemy_2_x = enemyPlaneLogic(enemy_2_x,enemy_2_y,enemy_2_speed_x,enemy_2_speed_y)[0]
        enemy_2_y = enemyPlaneLogic(enemy_2_x,enemy_2_y,enemy_2_speed_x,enemy_2_speed_y)[1]
        enemy_2_speed_x = enemyPlaneLogic(enemy_2_x,enemy_2_y,enemy_2_speed_x,enemy_2_speed_y)[2]
        enemy_2_speed_y = enemyPlaneLogic(enemy_2_x,enemy_2_y,enemy_2_speed_x,enemy_2_speed_y)[3]
        # Enemy Plane 3
        drawEnemyPlane(lvl_2_plane_enemy_3,enemy_3_x,enemy_3_y,enemy_3_speed_x,bf_109,bf_109_rev,player_hp,lvl_points)
        player_hp = drawEnemyPlane(lvl_2_plane_enemy_3,enemy_3_x,enemy_3_y,enemy_3_speed_x,bf_109,bf_109_rev,player_hp,lvl_points)[6]
        lvl_points = drawEnemyPlane(lvl_2_plane_enemy_3,enemy_3_x,enemy_3_y,enemy_3_speed_x,bf_109,bf_109_rev,player_hp,lvl_points)[7]
        enemy_3_x = enemyPlaneLogic(enemy_3_x,enemy_3_y,enemy_3_speed_x,enemy_3_speed_y)[0]
        enemy_3_y = enemyPlaneLogic(enemy_3_x,enemy_3_y,enemy_3_speed_x,enemy_3_speed_y)[1]
        enemy_3_speed_x = enemyPlaneLogic(enemy_3_x,enemy_3_y,enemy_3_speed_x,enemy_3_speed_y)[2]
        enemy_3_speed_y = enemyPlaneLogic(enemy_3_x,enemy_3_y,enemy_3_speed_x,enemy_3_speed_y)[3]
        drawPlayerPlane(lvl_2_plane,player_x,player_y)
        # Get Behemoth
        if lvl_victories >= 3:
            drawBehemoth(behemoth_2,behemoth_x,behemoth_y,behemoth_speed_x,junker_88,junker_88_rev)
            behemoth = behemothLogic(behemoth_2,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,junker_88,junker_88_rev,player_hp,behemoth_hp,lvl_2_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[0]
            behemoth_x = behemothLogic(behemoth_2,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,junker_88,junker_88_rev,player_hp,behemoth_hp,lvl_2_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[1]
            behemoth_y = behemothLogic(behemoth_2,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,junker_88,junker_88_rev,player_hp,behemoth_hp,lvl_2_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[2]
            behemoth_speed_x = behemothLogic(behemoth_2,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,junker_88,junker_88_rev,player_hp,behemoth_hp,lvl_2_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[3]
            behemoth_speed_y = behemothLogic(behemoth_2,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,junker_88,junker_88_rev,player_hp,behemoth_hp,lvl_2_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[4]
            junker_88 = behemothLogic(behemoth_2,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,junker_88,junker_88_rev,player_hp,behemoth_hp,lvl_2_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[5]
            junker_88_rev = behemothLogic(behemoth_2,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,junker_88,junker_88_rev,player_hp,behemoth_hp,lvl_2_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[6]
            player_hp = behemothLogic(behemoth_2,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,junker_88,junker_88_rev,player_hp,behemoth_hp,lvl_2_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[7]
            behemoth_hp = behemothLogic(behemoth_2,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,junker_88,junker_88_rev,player_hp,behemoth_hp,lvl_2_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[8]
            lvl_2_end = behemothLogic(behemoth_2,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,junker_88,junker_88_rev,player_hp,behemoth_hp,lvl_2_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[9]
            shoot = behemothLogic(behemoth_2,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,junker_88,junker_88_rev,player_hp,behemoth_hp,lvl_2_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[10]
            fire = behemothLogic(behemoth_2,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,junker_88,junker_88_rev,player_hp,behemoth_hp,lvl_2_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[11]
            primary_x = behemothLogic(behemoth_2,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,junker_88,junker_88_rev,player_hp,behemoth_hp,lvl_2_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[12]
            bomb_x = behemothLogic(behemoth_2,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,junker_88,junker_88_rev,player_hp,behemoth_hp,lvl_2_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[13]
            primary_y = behemothLogic(behemoth_2,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,junker_88,junker_88_rev,player_hp,behemoth_hp,lvl_2_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[14]
            bomb_y = behemothLogic(behemoth_2,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,junker_88,junker_88_rev,player_hp,behemoth_hp,lvl_2_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[15]
        drawStatus()
        # Shoot and Reset Primary and Secondary Shoot
        if shoot == True:
            screen.blit(bomb,[bomb_x,bomb_y])
        if fire == True:
            screen.blit(bullet,[primary_x,primary_y])
        # End of Level 2
        if lvl_2_end == True:
            british.stop()
            bang.stop()
            explosion.stop()
        """
        All Drawing Above Here
        Ending Under Here
        """
        pygame.display.flip()
        clock.tick(10)
    # Level Three Intro
    while not lvl_3_intro_end:
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                lvl_3_intro_end = True
                lvl_3_end = True
                lvl_4_intro_end = True
                lvl_4_end = True
                ending_intro_end = True
                ending_end = True
                end = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Set Level 3 Variables and Go to it
                if (mouse_x >= 700 and mouse_x <= 900) and (mouse_y >= 650 and mouse_y <= 700):
                    total_points += lvl_points
                    total_victories += lvl_victories
                    player_hp = 10.0
                    behemoth_hp = 50.0
                    player_speed_x = 0
                    player_speed_y = 0
                    player_x = 0
                    player_y = 0
                    enemy_x = 300
                    enemy_y = 100
                    enemy_speed_x = 0
                    enemy_speed_y = 0
                    enemy_2_x = 200
                    enemy_2_y = 500
                    enemy_2_speed_x = 0
                    enemy_2_speed_y = 0
                    enemy_3_x = 600
                    enemy_3_y = 200
                    enemy_3_speed_x = 0
                    enemy_3_speed_y = 0
                    enemy_4_x = 400
                    enemy_4_y = 200
                    enemy_4_speed_x = 0
                    enemy_4_speed_y = 0
                    enemy_5_x = 100
                    enemy_5_y = 300
                    enemy_5_speed_x = 0
                    enemy_5_speed_y = 0
                    enemy_6_x = 700
                    enemy_6_y = 400
                    enemy_6_speed_x = 0
                    enemy_6_speed_y = 0
                    lvl_3_plane = saber
                    lvl_3_plane_enemy = mig_15
                    lvl_3_plane_enemy_2 = mig_15
                    lvl_3_plane_enemy_3 = mig_15
                    lvl_3_plane_enemy_4 = mig_15
                    lvl_3_plane_enemy_5 = mig_15
                    lvl_3_plane_enemy_6 = mig_15
                    lvl_victories = 0
                    lvl_3_start = False
                    shoot = False
                    fire = False
                    lvl_victories = 0
                    lvl_points = 0
                    secondary_count = 5
                    lvl_3_intro_end = True
                    behemoth_x = 100
                    behemoth_y = 300
                    behemoth_speed_x = 0
                    behemoth_speed_y = 0
        screen.blit(fortunate_son_intro_page,[0,0])
        drawButton(700,650)
        pygame.display.flip()
        clock.tick(10)
    # Level Three
    while not lvl_3_end:
        icon = sabre_icon
        bomb_x_pos = player_x
        bomb_y_pos = player_y
        primary_x_pos = player_x
        primary_y_pos = player_y
        for event in pygame.event.get():
            # Quit Level 3
            if event.type == pygame.QUIT:
                lvl_3_end = True
                lvl_4_intro_end = True
                lvl_4_end = True
                ending_intro_end = True
                ending_end = True
                end = True
            # All Keybaord Movement
            # Key Down
            elif event.type == pygame.KEYDOWN:
                # Skip Level 3
                if event.key == pygame.K_ESCAPE:
                    american.stop()
                    lvl_3_end = True
                # Start Level 3
                elif event.key == pygame.K_q and lvl_3_start == False:
                    american.play()
                    player_speed_x = 5
                    enemy_speed_x = 20
                    enemy_speed_y = 20
                    enemy_2_speed_x = 20
                    enemy_2_speed_y = 20
                    enemy_3_speed_x = 20
                    enemy_3_speed_y = 20
                    enemy_4_speed_x = 20
                    enemy_4_speed_y = 20
                    enemy_5_speed_x = 20
                    enemy_5_speed_y = 20
                    enemy_6_speed_x = 20
                    enemy_6_speed_y = 20
                    lvl_3_start = True
                    behemoth_x = 100
                    behemoth_y = 300
                    behemoth_speed_x = 35
                    behemoth_speed_y = 5
                # Restart Level
                elif event.key == pygame.K_e:
                    american.stop()
                    player_hp = 10.0
                    behemoth_hp = 50.0
                    player_speed_x = 0
                    player_speed_y = 0
                    player_x = 0
                    player_y = 0
                    enemy_x = 300
                    enemy_y = 100
                    enemy_speed_x = 0
                    enemy_speed_y = 0
                    enemy_2_x = 200
                    enemy_2_y = 500
                    enemy_2_speed_x = 0
                    enemy_2_speed_y = 0
                    enemy_3_x = 600
                    enemy_3_y = 200
                    enemy_3_speed_x = 0
                    enemy_3_speed_y = 0
                    enemy_4_x = 400
                    enemy_4_y = 200
                    enemy_4_speed_x = 0
                    enemy_4_speed_y = 0
                    enemy_5_x = 100
                    enemy_5_y = 300
                    enemy_5_speed_x = 0
                    enemy_5_speed_y = 0
                    enemy_6_x = 700
                    enemy_6_y = 400
                    enemy_6_speed_x = 0
                    enemy_6_speed_y = 0
                    lvl_3_plane = saber
                    lvl_3_plane_enemy = mig_15
                    lvl_3_plane_enemy_2 = mig_15
                    lvl_3_plane_enemy_3 = mig_15
                    lvl_3_plane_enemy_4 = mig_15
                    lvl_3_plane_enemy_5 = mig_15
                    lvl_3_plane_enemy_6 = mig_15
                    lvl_victories = 0
                    lvl_3_start = False
                    shoot = False
                    fire = False
                    lvl_victories = 0
                    lvl_points = 0
                    secondary_count = 5
                    behemoth_x = 100
                    behemoth_y = 300
                    behemoth_speed_x = 0
                    behemoth_speed_y = 0
                # Player Movement
                elif event.key == pygame.K_w and lvl_3_start == True:
                    player_speed_y = -20
                elif event.key == pygame.K_s and lvl_3_start == True:
                    player_speed_y = 20
                elif event.key == pygame.K_a and lvl_3_start == True:
                    player_speed_x = -20
                    lvl_3_plane = saber_rev
                elif event.key == pygame.K_d and lvl_3_start == True:
                    player_speed_x = 20
                    lvl_3_plane = saber
                # Shooting Primary
                elif event.key == pygame.K_SPACE and fire == False and lvl_3_start == True:
                    if lvl_3_plane == saber:
                        bullet = player_primary
                        fire = True
                        primary_x = primary_x_pos
                        primary_y = primary_y_pos
                        primary_speed_x = 100
                        primary_speed_y = 0
                        bang.play()
                    elif lvl_3_plane == saber_rev:
                        bullet = player_primary_rev
                        fire = True
                        primary_x = primary_x_pos
                        primary_y = primary_y_pos
                        primary_speed_x = -100
                        primary_speed_y = 0
                        bang.play()
                # Shooting Secondary
                elif event.key == pygame.K_b and shoot == False and lvl_3_start == True and secondary_count > 0:
                    secondary_count -= 1
                    if lvl_3_plane == saber:
                        bomb = player_projectile
                        shoot = True
                        bomb_x = bomb_x_pos
                        bomb_y = bomb_y_pos
                        bomb_speed_x = 35
                        bomb_speed_y = 0
                        bang.play()
                    elif lvl_3_plane == saber_rev:
                        bomb = player_projectile_rev
                        shoot = True
                        bomb_x = bomb_x_pos
                        bomb_y = bomb_y_pos
                        bomb_speed_x = -35
                        bomb_speed_y = 0
                        bang.play()
            # Player Movement (Key Up)
            elif event.type == pygame.KEYUP and lvl_3_start == True:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player_speed_y = 0
                elif event.key == pygame.K_d:
                    player_speed_x = 5
                elif event.key == pygame.K_a:
                    player_speed_x = -5
                elif event.key == pygame.K_SPACE:
                    fire = True
                elif event.key == pygame.K_b:
                    shoot = True
        """
        All Events Above Here
        All Game Logic Under Here
        """
        # Player, Enemy, and Entity Movement
        # Player Movement
        player_x += player_speed_x
        player_y += player_speed_y
        # Player Movement Limit
        if player_x >= 920:
            player_x = 920
        if player_x <= 0:
            player_x = 0
        if player_y >= 560:
            player_y = 560
        if player_y <= 0:
            player_y = 0
        # Primary Fire Movement
        primary_x += primary_speed_x
        primary_y += primary_speed_y
        # Primary Fire Movement Limit
        if primary_x >= 1000 or primary_x <= 0:
            fire = False
        # Primary Fire Hitting Enemies
        if (primary_x >= enemy_x and primary_x <= enemy_x + 80) and (primary_y >= enemy_y - 40 and primary_y <= enemy_y + 40):
            enemy_speed_x = 0
            enemy_speed_y = 0
            enemy_x = 2000
            enemy_y = 2000
            fire = False
            lvl_victories += 1
            lvl_points += 100
            explosion.play()
        if (primary_x >= enemy_2_x and primary_x <= enemy_2_x + 80) and (primary_y >= enemy_2_y - 40 and primary_y <= enemy_2_y + 40):
            enemy_2_speed_x = 0
            enemy_2_speed_y = 0
            enemy_2_x = 2000
            enemy_2_y = 2000
            fire = False
            lvl_victories += 1
            lvl_points += 100
            explosion.play()
        if (primary_x >= enemy_3_x and primary_x <= enemy_3_x + 80) and (primary_y >= enemy_3_y - 40 and primary_y <= enemy_3_y + 40):
            enemy_3_speed_x = 0
            enemy_3_speed_y = 0
            enemy_3_x = 2000
            enemy_3_y = 2000
            fire = False
            lvl_victories += 1
            lvl_points += 100
            explosion.play()
        if (primary_x >= enemy_4_x and primary_x <= enemy_4_x + 80) and (primary_y >= enemy_4_y - 40 and primary_y <= enemy_4_y + 40):
            enemy_4_speed_x = 0
            enemy_4_speed_y = 0
            enemy_4_x = 2000
            enemy_4_y = 2000
            fire = False
            lvl_victories += 1
            lvl_points += 100
            explosion.play()
        if (primary_x >= enemy_5_x and primary_x <= enemy_5_x + 80) and (primary_y >= enemy_5_y - 40 and primary_y <= enemy_5_y + 40):
            enemy_5_speed_x = 0
            enemy_5_speed_y = 0
            enemy_5_x = 2000
            enemy_5_y = 2000
            fire = False
            lvl_victories += 1
            lvl_points += 100
            explosion.play()
        if (primary_x >= enemy_6_x and primary_x <= enemy_6_x + 80) and (primary_y >= enemy_6_y - 40 and primary_y <= enemy_6_y + 40):
            enemy_6_speed_x = 0
            enemy_6_speed_y = 0
            enemy_6_x = 2000
            enemy_6_y = 2000
            fire = False
            lvl_victories += 1
            lvl_points += 100
            explosion.play()
        # Secondary Fire Movement
        bomb_x += bomb_speed_x
        bomb_y += bomb_speed_y
        # Secondary Fire Movement Limit
        if bomb_x >= 1000 or bomb_x <= 0 or bomb_y >= 570:
            shoot = False
        # Secondary Hitting Enemies
        if (bomb_x >= enemy_x and bomb_x <= enemy_x + 80) and (bomb_y >= enemy_y - 40 and bomb_y <= enemy_y + 40):
            enemy_speed_x = 0
            enemy_speed_y = 0
            enemy_x = 2000
            enemy_y = 2000
            shoot = False
            lvl_victories += 1
            lvl_points += 150
            explosion.play()
        if (bomb_x >= enemy_2_x and bomb_x <= enemy_2_x + 80) and (bomb_y >= enemy_2_y - 40 and bomb_y <= enemy_2_y + 40):
            enemy_2_speed_x = 0
            enemy_2_speed_y = 0
            enemy_2_x = 2000
            enemy_2_y = 2000
            shoot = False
            lvl_victories += 1
            lvl_points += 150
            explosion.play()
        if (bomb_x >= enemy_3_x and bomb_x <= enemy_3_x + 80) and (bomb_y >= enemy_3_y - 40 and bomb_y <= enemy_3_y + 40):
            enemy_3_speed_x = 0
            enemy_3_speed_y = 0
            enemy_3_x = 2000
            enemy_3_y = 2000
            shoot = False
            lvl_victories += 1
            lvl_points += 150
            explosion.play()
        if (bomb_x >= enemy_4_x and bomb_x <= enemy_4_x + 80) and (bomb_y >= enemy_4_y - 40 and bomb_y <= enemy_4_y + 40):
            enemy_4_speed_x = 0
            enemy_4_speed_y = 0
            enemy_4_x = 2000
            enemy_4_y = 2000
            shoot = False
            lvl_victories += 1
            lvl_points += 150
            explosion.play()
        if (bomb_x >= enemy_5_x and bomb_x <= enemy_5_x + 80) and (bomb_y >= enemy_5_y - 40 and bomb_y <= enemy_5_y + 40):
            enemy_5_speed_x = 0
            enemy_5_speed_y = 0
            enemy_5_x = 2000
            enemy_5_y = 2000
            shoot = False
            lvl_victories += 1
            lvl_points += 150
            explosion.play()
        if (bomb_x >= enemy_6_x and bomb_x <= enemy_6_x + 80) and (bomb_y >= enemy_6_y - 40 and bomb_y <= enemy_6_y + 40):
            enemy_6_speed_x = 0
            enemy_6_speed_y = 0
            enemy_6_x = 2000
            enemy_6_y = 2000
            shoot = False
            lvl_victories += 1
            lvl_points += 150
            explosion.play()
        # Player Health System
        if player_hp <= 0.0:
            american.stop()
            player_hp = 10.0
            behemoth_hp = 50.0
            player_speed_x = 0
            player_speed_y = 0
            player_x = 0
            player_y = 0
            enemy_x = 300
            enemy_y = 100
            enemy_speed_x = 0
            enemy_speed_y = 0
            enemy_2_x = 200
            enemy_2_y = 500
            enemy_2_speed_x = 0
            enemy_2_speed_y = 0
            enemy_3_x = 600
            enemy_3_y = 200
            enemy_3_speed_x = 0
            enemy_3_speed_y = 0
            enemy_4_x = 400
            enemy_4_y = 200
            enemy_4_speed_x = 0
            enemy_4_speed_y = 0
            enemy_5_x = 100
            enemy_5_y = 300
            enemy_5_speed_x = 0
            enemy_5_speed_y = 0
            enemy_6_x = 700
            enemy_6_y = 400
            enemy_6_speed_x = 0
            enemy_6_speed_y = 0
            lvl_3_plane = saber
            lvl_3_plane_enemy = mig_15
            lvl_3_plane_enemy_2 = mig_15
            lvl_3_plane_enemy_3 = mig_15
            lvl_3_plane_enemy_4 = mig_15
            lvl_3_plane_enemy_5 = mig_15
            lvl_3_plane_enemy_6 = mig_15
            lvl_victories = 0
            lvl_3_start = False
            shoot = False
            fire = False
            lvl_victories = 0
            lvl_points = 0
            secondary_count = 5
            behemoth_x = 100
            behemoth_y = 300
            behemoth_speed_x = 0
            behemoth_speed_y = 0
        """
        All Game Logic Above Here
        All Drawing Under Here
        """
        screen.blit(background_3,[0,0])
        # Enemy Plane 1
        drawEnemyPlane(lvl_3_plane_enemy,enemy_x,enemy_y,enemy_speed_x,mig_15,mig_15_rev,player_hp,lvl_points)
        player_hp = drawEnemyPlane(lvl_3_plane_enemy,enemy_x,enemy_y,enemy_speed_x,mig_15,mig_15_rev,player_hp,lvl_points)[6]
        lvl_points = drawEnemyPlane(lvl_3_plane_enemy,enemy_x,enemy_y,enemy_speed_x,mig_15,mig_15_rev,player_hp,lvl_points)[7]
        enemy_x = enemyPlaneLogic(enemy_x,enemy_y,enemy_speed_x,enemy_speed_y)[0]
        enemy_y = enemyPlaneLogic(enemy_x,enemy_y,enemy_speed_x,enemy_speed_y)[1]
        enemy_speed_x = enemyPlaneLogic(enemy_x,enemy_y,enemy_speed_x,enemy_speed_y)[2]
        enemy_speed_y = enemyPlaneLogic(enemy_x,enemy_y,enemy_speed_x,enemy_speed_y)[3]
        # Enemy Plane 2
        drawEnemyPlane(lvl_3_plane_enemy_2,enemy_2_x,enemy_2_y,enemy_2_speed_x,mig_15,mig_15_rev,player_hp,lvl_points)
        player_hp = drawEnemyPlane(lvl_3_plane_enemy_2,enemy_2_x,enemy_2_y,enemy_2_speed_x,mig_15,mig_15_rev,player_hp,lvl_points)[6]
        lvl_points = drawEnemyPlane(lvl_3_plane_enemy_2,enemy_2_x,enemy_2_y,enemy_2_speed_x,mig_15,mig_15_rev,player_hp,lvl_points)[7]
        enemy_2_x = enemyPlaneLogic(enemy_2_x,enemy_2_y,enemy_2_speed_x,enemy_2_speed_y)[0]
        enemy_2_y = enemyPlaneLogic(enemy_2_x,enemy_2_y,enemy_2_speed_x,enemy_2_speed_y)[1]
        enemy_2_speed_x = enemyPlaneLogic(enemy_2_x,enemy_2_y,enemy_2_speed_x,enemy_2_speed_y)[2]
        enemy_2_speed_y = enemyPlaneLogic(enemy_2_x,enemy_2_y,enemy_2_speed_x,enemy_2_speed_y)[3]
        # Enemy Plane 3
        drawEnemyPlane(lvl_3_plane_enemy_3,enemy_3_x,enemy_3_y,enemy_3_speed_x,mig_15,mig_15_rev,player_hp,lvl_points)
        player_hp = drawEnemyPlane(lvl_3_plane_enemy_3,enemy_3_x,enemy_3_y,enemy_3_speed_x,mig_15,mig_15_rev,player_hp,lvl_points)[6]
        lvl_points = drawEnemyPlane(lvl_3_plane_enemy_3,enemy_3_x,enemy_3_y,enemy_3_speed_x,mig_15,mig_15_rev,player_hp,lvl_points)[7]
        enemy_3_x = enemyPlaneLogic(enemy_3_x,enemy_3_y,enemy_3_speed_x,enemy_3_speed_y)[0]
        enemy_3_y = enemyPlaneLogic(enemy_3_x,enemy_3_y,enemy_3_speed_x,enemy_3_speed_y)[1]
        enemy_3_speed_x = enemyPlaneLogic(enemy_3_x,enemy_3_y,enemy_3_speed_x,enemy_3_speed_y)[2]
        enemy_3_speed_y = enemyPlaneLogic(enemy_3_x,enemy_3_y,enemy_3_speed_x,enemy_3_speed_y)[3]
        drawPlayerPlane(lvl_3_plane,player_x,player_y)
        # Enemy Plane 4
        drawEnemyPlane(lvl_3_plane_enemy_4,enemy_4_x,enemy_4_y,enemy_4_speed_x,mig_15,mig_15_rev,player_hp,lvl_points)
        player_hp = drawEnemyPlane(lvl_3_plane_enemy_4,enemy_4_x,enemy_4_y,enemy_4_speed_x,mig_15,mig_15_rev,player_hp,lvl_points)[6]
        lvl_points = drawEnemyPlane(lvl_3_plane_enemy_4,enemy_4_x,enemy_4_y,enemy_4_speed_x,mig_15,mig_15_rev,player_hp,lvl_points)[7]
        enemy_4_x = enemyPlaneLogic(enemy_4_x,enemy_4_y,enemy_4_speed_x,enemy_4_speed_y)[0]
        enemy_4_y = enemyPlaneLogic(enemy_4_x,enemy_4_y,enemy_4_speed_x,enemy_4_speed_y)[1]
        enemy_4_speed_x = enemyPlaneLogic(enemy_4_x,enemy_4_y,enemy_4_speed_x,enemy_4_speed_y)[2]
        enemy_4_speed_y = enemyPlaneLogic(enemy_4_x,enemy_4_y,enemy_4_speed_x,enemy_4_speed_y)[3]
        # Enemy Plane 5
        drawEnemyPlane(lvl_3_plane_enemy_5,enemy_5_x,enemy_5_y,enemy_5_speed_x,mig_15,mig_15_rev,player_hp,lvl_points)
        player_hp = drawEnemyPlane(lvl_3_plane_enemy_5,enemy_5_x,enemy_5_y,enemy_5_speed_x,mig_15,mig_15_rev,player_hp,lvl_points)[6]
        lvl_points = drawEnemyPlane(lvl_3_plane_enemy_5,enemy_5_x,enemy_5_y,enemy_5_speed_x,mig_15,mig_15_rev,player_hp,lvl_points)[7]
        enemy_5_x = enemyPlaneLogic(enemy_5_x,enemy_5_y,enemy_5_speed_x,enemy_5_speed_y)[0]
        enemy_5_y = enemyPlaneLogic(enemy_5_x,enemy_5_y,enemy_5_speed_x,enemy_5_speed_y)[1]
        enemy_5_speed_x = enemyPlaneLogic(enemy_5_x,enemy_5_y,enemy_5_speed_x,enemy_5_speed_y)[2]
        enemy_5_speed_y = enemyPlaneLogic(enemy_5_x,enemy_5_y,enemy_5_speed_x,enemy_5_speed_y)[3]
        # Enemy Plane 6
        drawEnemyPlane(lvl_3_plane_enemy_6,enemy_6_x,enemy_6_y,enemy_6_speed_x,mig_15,mig_15_rev,player_hp,lvl_points)
        player_hp = drawEnemyPlane(lvl_3_plane_enemy_6,enemy_6_x,enemy_6_y,enemy_6_speed_x,mig_15,mig_15_rev,player_hp,lvl_points)[6]
        lvl_points = drawEnemyPlane(lvl_3_plane_enemy_6,enemy_6_x,enemy_6_y,enemy_6_speed_x,mig_15,mig_15_rev,player_hp,lvl_points)[7]
        enemy_6_x = enemyPlaneLogic(enemy_6_x,enemy_6_y,enemy_6_speed_x,enemy_6_speed_y)[0]
        enemy_6_y = enemyPlaneLogic(enemy_6_x,enemy_6_y,enemy_6_speed_x,enemy_6_speed_y)[1]
        enemy_6_speed_x = enemyPlaneLogic(enemy_6_x,enemy_6_y,enemy_6_speed_x,enemy_6_speed_y)[2]
        enemy_6_speed_y = enemyPlaneLogic(enemy_6_x,enemy_6_y,enemy_6_speed_x,enemy_6_speed_y)[3]
        # Player Plane
        drawPlayerPlane(lvl_3_plane,player_x,player_y)
        # Draw Status
        drawStatus()
        # Shoot and Reset Primary and Secondary Shoot
        if shoot == True:
            screen.blit(bomb,[bomb_x,bomb_y])
        if fire == True:
            screen.blit(bullet,[primary_x,primary_y])
        # End of Level 3
        if lvl_victories >= 6:
            american.stop()
            bang.stop()
            explosion.stop()
            lvl_3_end = True
        """
        All Drawing Above Here
        Ending Under Here
        """
        pygame.display.flip()
        clock.tick(10)
    # Level Four Intro
    while not lvl_4_intro_end:
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                lvl_4_intro_end = True
                lvl_4_end = True
                ending_intro_end = True
                ending_end = True
                end = True
            # Set Level Variables and Go to it
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (mouse_x >= 700 and mouse_x <= 900) and (mouse_y >= 650 and mouse_y <= 700):
                    total_points += lvl_points
                    total_victories += lvl_victories
                    player_hp = 10.0
                    behemoth_hp = 50.0
                    player_speed_x = 0
                    player_speed_y = 0
                    player_x = 0
                    player_y = 0
                    enemy_x = 300
                    enemy_y = 100
                    enemy_speed_x = 0
                    enemy_speed_y = 0
                    enemy_2_x = 200
                    enemy_2_y = 500
                    enemy_2_speed_x = 0
                    enemy_2_speed_y = 0
                    enemy_3_x = 600
                    enemy_3_y = 200
                    enemy_3_speed_x = 0
                    enemy_3_speed_y = 0
                    enemy_4_x = 400
                    enemy_4_y = 200
                    enemy_4_speed_x = 0
                    enemy_4_speed_y = 0
                    lvl_4_plane = pak_fa
                    lvl_4_plane_enemy = f_35
                    lvl_4_plane_enemy_2 = f_35
                    lvl_4_plane_enemy_3 = f_35
                    lvl_4_plane_enemy_4 = f_35
                    lvl_victories = 0
                    lvl_4_start = False
                    shoot = False
                    fire = False
                    lvl_victories = 0
                    lvl_points = 0
                    secondary_count = 5
                    lvl_4_intro_end = True
                    behemoth_x = 100
                    behemoth_y = 580
                    behemoth_speed_x = 0
                    behemoth_speed_y = 0
        screen.blit(baltic_brawl_intro_page,[0,0])
        drawButton(700,650)
        pygame.display.flip()
        clock.tick(10)
    # Level Four
    while not lvl_4_end:
        icon = su_57_icon
        bomb_x_pos = player_x
        bomb_y_pos = player_y
        primary_x_pos = player_x
        primary_y_pos = player_y
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                lvl_4_end = True
                ending_intro_end = True
                ending_end = True
                end = True
            if event.type == pygame.KEYDOWN:
                # Skip Level 4
                if event.key == pygame.K_ESCAPE:
                    lvl_4_end = True
                # Start Level
                elif event.key == pygame.K_q and lvl_4_start == False:
                    russian.play()
                    player_speed_x = 5
                    enemy_speed_x = 25
                    enemy_speed_y = 20
                    enemy_2_speed_x = 25
                    enemy_2_speed_y = 20
                    enemy_3_speed_x = 25
                    enemy_3_speed_y = 20
                    enemy_4_speed_x = 25
                    enemy_4_speed_y = 20
                    lvl_4_start = True
                    behemoth_x = 100
                    behemoth_y = 500
                    behemoth_speed_x = 10
                    behemoth_speed_y = 0
                    second_behemoth_logic = True
                # Restart Level
                elif event.key == pygame.K_e:
                    russian.stop()
                    player_hp = 10.0
                    behemoth_hp = 50.0
                    player_speed_x = 0
                    player_speed_y = 0
                    player_x = 0
                    player_y = 0
                    enemy_x = 300
                    enemy_y = 100
                    enemy_speed_x = 0
                    enemy_speed_y = 0
                    enemy_2_x = 200
                    enemy_2_y = 500
                    enemy_2_speed_x = 0
                    enemy_2_speed_y = 0
                    enemy_3_x = 600
                    enemy_3_y = 200
                    enemy_3_speed_x = 0
                    enemy_3_speed_y = 0
                    enemy_4_x = 400
                    enemy_4_y = 200
                    enemy_4_speed_x = 0
                    enemy_4_speed_y = 0
                    lvl_4_plane = pak_fa
                    lvl_4_plane_enemy = f_35
                    lvl_4_plane_enemy_2 = f_35
                    lvl_4_plane_enemy_3 = f_35
                    lvl_4_plane_enemy_4 = f_35
                    lvl_victories = 0
                    lvl_4_start = False
                    shoot = False
                    fire = False
                    lvl_victories = 0
                    lvl_points = 0
                    secondary_count = 5
                    behemoth_x = 100
                    behemoth_y = 700
                    behemoth_speed_x = 0
                    behemoth_speed_y = 0
                # Player Movement
                elif event.key == pygame.K_w and lvl_4_start == True:
                    player_speed_y = -40
                elif event.key == pygame.K_s and lvl_4_start == True:
                    player_speed_y = 40
                elif event.key == pygame.K_a and lvl_4_start == True:
                    player_speed_x = -40
                    lvl_4_plane = pak_fa_rev
                elif event.key == pygame.K_d and lvl_4_start == True:
                    player_speed_x = 40
                    lvl_4_plane = pak_fa
                # Shooting Primary
                elif event.key == pygame.K_SPACE and fire == False and lvl_4_start == True:
                    if lvl_4_plane == pak_fa:
                        bullet = player_primary
                        fire = True
                        primary_x = primary_x_pos
                        primary_y = primary_y_pos
                        primary_speed_x = 100
                        primary_speed_y = 0
                        bang.play()
                    elif lvl_4_plane == pak_fa_rev:
                        bullet = player_primary_rev
                        fire = True
                        primary_x = primary_x_pos
                        primary_y = primary_y_pos
                        primary_speed_x = -100
                        primary_speed_y = 0
                        bang.play()
                # Shooting Secondary
                elif event.key == pygame.K_b and shoot == False and lvl_4_start == True and secondary_count > 0:
                    secondary_count -= 1
                    if lvl_4_plane == pak_fa:
                        bomb = player_projectile
                        shoot = True
                        bomb_x = bomb_x_pos
                        bomb_y = bomb_y_pos
                        bomb_speed_x = 0
                        bomb_speed_y = 60
                        bang.play()
                    elif lvl_4_plane == pak_fa_rev:
                        bomb = player_projectile_rev
                        shoot = True
                        bomb_x = bomb_x_pos
                        bomb_y = bomb_y_pos
                        bomb_speed_x = 0
                        bomb_speed_y = 50
                        bang.play()
            # Player Movement (Key Up)
            elif event.type == pygame.KEYUP and lvl_4_start == True:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player_speed_y = 0
                elif event.key == pygame.K_d:
                    player_speed_x = 5
                elif event.key == pygame.K_a:
                    player_speed_x = -5
                elif event.key == pygame.K_SPACE:
                    fire = True
                elif event.key == pygame.K_b:
                    shoot = True
        """
        All Events Above Here
        All Game Logic Under Here
        """
        # Player, Enemy, and Entity Movement
        # Player Movement
        player_x += player_speed_x
        player_y += player_speed_y
        # Player Movement Limit
        if player_x >= 920:
            player_x = 920
        if player_x <= 0:
            player_x = 0
        if player_y >= 560:
            player_y = 560
        if player_y <= 0:
            player_y = 0
        # Primary Fire Movement
        primary_x += primary_speed_x
        primary_y += primary_speed_y
        # Primary Fire Movement Limit
        if primary_x >= 1000 or primary_x <= 0:
            fire = False
        # Primary Fire Hitting Enemies
        if (primary_x >= enemy_x and primary_x <= enemy_x + 80) and (primary_y >= enemy_y - 40 and primary_y <= enemy_y + 40):
            enemy_speed_x = 0
            enemy_speed_y = 0
            enemy_x = 2000
            enemy_y = 2000
            fire = False
            lvl_victories += 1
            lvl_points += 100
            explosion.play()
        if (primary_x >= enemy_2_x and primary_x <= enemy_2_x + 80) and (primary_y >= enemy_2_y - 40 and primary_y <= enemy_2_y + 40):
            enemy_2_speed_x = 0
            enemy_2_speed_y = 0
            enemy_2_x = 2000
            enemy_2_y = 2000
            fire = False
            lvl_victories += 1
            lvl_points += 100
            explosion.play()
        if (primary_x >= enemy_3_x and primary_x <= enemy_3_x + 80) and (primary_y >= enemy_3_y - 40 and primary_y <= enemy_3_y + 40):
            enemy_3_speed_x = 0
            enemy_3_speed_y = 0
            enemy_3_x = 2000
            enemy_3_y = 2000
            fire = False
            lvl_victories += 1
            lvl_points += 100
            explosion.play()
        if (primary_x >= enemy_4_x and primary_x <= enemy_4_x + 80) and (primary_y >= enemy_4_y - 40 and primary_y <= enemy_4_y + 40):
            enemy_4_speed_x = 0
            enemy_4_speed_y = 0
            enemy_4_x = 2000
            enemy_4_y = 2000
            fire = False
            lvl_victories += 1
            lvl_points += 100
            explosion.play()
        # Secondary Fire Movement
        bomb_x += bomb_speed_x
        bomb_y += bomb_speed_y
        # Secondary Fire Movement Limit
        if bomb_x >= 1000 or bomb_x <= 0 or bomb_y >= 570:
            shoot = False
        # Secondary Hitting Enemies
        if (bomb_x >= enemy_x and bomb_x <= enemy_x + 80) and (bomb_y >= enemy_y - 40 and bomb_y <= enemy_y + 40):
            enemy_speed_x = 0
            enemy_speed_y = 0
            enemy_x = 2000
            enemy_y = 2000
            shoot = False
            lvl_victories += 1
            lvl_points += 150
            explosion.play()
        if (bomb_x >= enemy_2_x and bomb_x <= enemy_2_x + 80) and (bomb_y >= enemy_2_y - 40 and bomb_y <= enemy_2_y + 40):
            enemy_2_speed_x = 0
            enemy_2_speed_y = 0
            enemy_2_x = 2000
            enemy_2_y = 2000
            shoot = False
            lvl_victories += 1
            lvl_points += 150
            explosion.play()
        if (bomb_x >= enemy_3_x and bomb_x <= enemy_3_x + 80) and (bomb_y >= enemy_3_y - 40 and bomb_y <= enemy_3_y + 40):
            enemy_3_speed_x = 0
            enemy_3_speed_y = 0
            enemy_3_x = 2000
            enemy_3_y = 2000
            shoot = False
            lvl_victories += 1
            lvl_points += 150
            explosion.play()
        if (bomb_x >= enemy_4_x and bomb_x <= enemy_4_x + 80) and (bomb_y >= enemy_4_y - 40 and bomb_y <= enemy_4_y + 40):
            enemy_4_speed_x = 0
            enemy_4_speed_y = 0
            enemy_4_x = 2000
            enemy_4_y = 2000
            shoot = False
            lvl_victories += 1
            lvl_points += 150
            explosion.play()
        # Player Health System
        if player_hp <= 0.0:
            russian.stop()
            player_hp = 10.0
            behemoth_hp = 50.0
            player_speed_x = 0
            player_speed_y = 0
            player_x = 0
            player_y = 0
            enemy_x = 300
            enemy_y = 100
            enemy_speed_x = 0
            enemy_speed_y = 0
            enemy_2_x = 200
            enemy_2_y = 500
            enemy_2_speed_x = 0
            enemy_2_speed_y = 0
            enemy_3_x = 600
            enemy_3_y = 200
            enemy_3_speed_x = 0
            enemy_3_speed_y = 0
            enemy_4_x = 400
            enemy_4_y = 200
            enemy_4_speed_x = 0
            enemy_4_speed_y = 0
            lvl_4_plane = pak_fa
            lvl_4_plane_enemy = f_35
            lvl_4_plane_enemy_2 = f_35
            lvl_4_plane_enemy_3 = f_35
            lvl_4_plane_enemy_4 = f_35
            lvl_victories = 0
            lvl_4_start = False
            shoot = False
            fire = False
            lvl_victories = 0
            lvl_points = 0
            secondary_count = 5
            behemoth_x = 100
            behemoth_y = 700
            behemoth_speed_x = 0
            behemoth_speed_y = 0
        """
        All Game Logic Above Here
        All Drawing Under Here
        """
        screen.blit(background_4,[0,0])
        # Behemoth
        drawBehemoth(behemoth_3,behemoth_x,behemoth_y,behemoth_speed_x,warship,warship_rev)
        behemoth = behemothLogic(behemoth_3,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,warship,warship_rev,player_hp,behemoth_hp,lvl_4_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[0]
        behemoth_x = behemothLogic(behemoth_3,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,warship,warship_rev,player_hp,behemoth_hp,lvl_4_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[1]
        behemoth_y = behemothLogic(behemoth_3,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,warship,warship_rev,player_hp,behemoth_hp,lvl_4_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[2]
        behemoth_speed_x = behemothLogic(behemoth_3,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,warship,warship_rev,player_hp,behemoth_hp,lvl_4_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[3]
        behemoth_speed_y = behemothLogic(behemoth_3,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,warship,warship_rev,player_hp,behemoth_hp,lvl_4_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[4]
        warship = behemothLogic(behemoth_3,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,warship,warship_rev,player_hp,behemoth_hp,lvl_4_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[5]
        warship_rev = behemothLogic(behemoth_3,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,warship,warship_rev,player_hp,behemoth_hp,lvl_4_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[6]
        player_hp = behemothLogic(behemoth_3,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,warship,warship_rev,player_hp,behemoth_hp,lvl_4_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[7]
        behemoth_hp = behemothLogic(behemoth_3,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,warship,warship_rev,player_hp,behemoth_hp,lvl_4_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[8]
        lvl_4_end = behemothLogic(behemoth_3,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,warship,warship_rev,player_hp,behemoth_hp,lvl_4_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[9]
        shoot = behemothLogic(behemoth_3,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,warship,warship_rev,player_hp,behemoth_hp,lvl_4_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[10]
        fire = behemothLogic(behemoth_3,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,warship,warship_rev,player_hp,behemoth_hp,lvl_4_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[11]
        primary_x = behemothLogic(behemoth_3,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,warship,warship_rev,player_hp,behemoth_hp,lvl_4_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[12]
        bomb_x = behemothLogic(behemoth_3,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,warship,warship_rev,player_hp,behemoth_hp,lvl_4_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[13]
        primary_y = behemothLogic(behemoth_3,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,warship,warship_rev,player_hp,behemoth_hp,lvl_4_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[14]
        bomb_y = behemothLogic(behemoth_3,behemoth_x,behemoth_y,behemoth_speed_x,behemoth_speed_y,warship,warship_rev,player_hp,behemoth_hp,lvl_4_end,shoot,fire,primary_x,bomb_x,primary_y,bomb_y)[15]
        # Enemy Plane 1
        drawEnemyPlane(lvl_4_plane_enemy,enemy_x,enemy_y,enemy_speed_x,f_35,f_35_rev,player_hp,lvl_points)
        player_hp = drawEnemyPlane(lvl_4_plane_enemy,enemy_x,enemy_y,enemy_speed_x,f_35,f_35_rev,player_hp,lvl_points)[6]
        lvl_points = drawEnemyPlane(lvl_4_plane_enemy,enemy_x,enemy_y,enemy_speed_x,f_35,f_35_rev,player_hp,lvl_points)[7]
        enemy_x = enemyPlaneLogic(enemy_x,enemy_y,enemy_speed_x,enemy_speed_y)[0]
        enemy_y = enemyPlaneLogic(enemy_x,enemy_y,enemy_speed_x,enemy_speed_y)[1]
        enemy_speed_x = enemyPlaneLogic(enemy_x,enemy_y,enemy_speed_x,enemy_speed_y)[2]
        enemy_speed_y = enemyPlaneLogic(enemy_x,enemy_y,enemy_speed_x,enemy_speed_y)[3]
        # Enemy Plane 2
        drawEnemyPlane(lvl_4_plane_enemy_2,enemy_2_x,enemy_2_y,enemy_2_speed_x,f_35,f_35_rev,player_hp,lvl_points)
        player_hp = drawEnemyPlane(lvl_4_plane_enemy_2,enemy_2_x,enemy_2_y,enemy_2_speed_x,f_35,f_35_rev,player_hp,lvl_points)[6]
        lvl_points = drawEnemyPlane(lvl_4_plane_enemy_2,enemy_2_x,enemy_2_y,enemy_2_speed_x,f_35,f_35_rev,player_hp,lvl_points)[7]
        enemy_2_x = enemyPlaneLogic(enemy_2_x,enemy_2_y,enemy_2_speed_x,enemy_2_speed_y)[0]
        enemy_2_y = enemyPlaneLogic(enemy_2_x,enemy_2_y,enemy_2_speed_x,enemy_2_speed_y)[1]
        enemy_2_speed_x = enemyPlaneLogic(enemy_2_x,enemy_2_y,enemy_2_speed_x,enemy_2_speed_y)[2]
        enemy_2_speed_y = enemyPlaneLogic(enemy_2_x,enemy_2_y,enemy_2_speed_x,enemy_2_speed_y)[3]
        # Enemy Plane 3
        drawEnemyPlane(lvl_4_plane_enemy_3,enemy_3_x,enemy_3_y,enemy_3_speed_x,f_35,f_35_rev,player_hp,lvl_points)
        player_hp = drawEnemyPlane(lvl_4_plane_enemy_3,enemy_3_x,enemy_3_y,enemy_3_speed_x,f_35,f_35_rev,player_hp,lvl_points)[6]
        lvl_points = drawEnemyPlane(lvl_4_plane_enemy_3,enemy_3_x,enemy_3_y,enemy_3_speed_x,f_35,f_35_rev,player_hp,lvl_points)[7]
        enemy_3_x = enemyPlaneLogic(enemy_3_x,enemy_3_y,enemy_3_speed_x,enemy_3_speed_y)[0]
        enemy_3_y = enemyPlaneLogic(enemy_3_x,enemy_3_y,enemy_3_speed_x,enemy_3_speed_y)[1]
        enemy_3_speed_x = enemyPlaneLogic(enemy_3_x,enemy_3_y,enemy_3_speed_x,enemy_3_speed_y)[2]
        enemy_3_speed_y = enemyPlaneLogic(enemy_3_x,enemy_3_y,enemy_3_speed_x,enemy_3_speed_y)[3]
        # Enemy Plane 4
        drawEnemyPlane(lvl_4_plane_enemy_4,enemy_4_x,enemy_4_y,enemy_4_speed_x,f_35,f_35_rev,player_hp,lvl_points)
        player_hp = drawEnemyPlane(lvl_4_plane_enemy_4,enemy_4_x,enemy_4_y,enemy_4_speed_x,f_35,f_35_rev,player_hp,lvl_points)[6]
        lvl_points = drawEnemyPlane(lvl_4_plane_enemy_4,enemy_4_x,enemy_4_y,enemy_4_speed_x,f_35,f_35_rev,player_hp,lvl_points)[7]
        enemy_4_x = enemyPlaneLogic(enemy_4_x,enemy_4_y,enemy_4_speed_x,enemy_4_speed_y)[0]
        enemy_4_y = enemyPlaneLogic(enemy_4_x,enemy_4_y,enemy_4_speed_x,enemy_4_speed_y)[1]
        enemy_4_speed_x = enemyPlaneLogic(enemy_4_x,enemy_4_y,enemy_4_speed_x,enemy_4_speed_y)[2]
        enemy_4_speed_y = enemyPlaneLogic(enemy_4_x,enemy_4_y,enemy_4_speed_x,enemy_4_speed_y)[3]
        # Player Plane
        drawPlayerPlane(lvl_4_plane,player_x,player_y)
        # Draw Statues
        drawStatus()
        # Shoot and Reset Primary and Secondary Shoot
        if shoot == True:
            screen.blit(bomb,[bomb_x,bomb_y])
        if fire == True:
            screen.blit(bullet,[primary_x,primary_y])
        # Level 4 Ending
        if lvl_4_end == True:
            russian.stop()
            bang.stop()
            explosion.stop()
        """
        All Drawing Above Here
        Ending Under Here
        """
        pygame.display.flip()
        clock.tick(10)
    # Ending Intro
    while not ending_intro_end:
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        for event in pygame.event.get():
            # End Game
            if event.type == pygame.QUIT:
                ending_intro_end = True
                ending_end = True
                end = True
            # Next Page
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (mouse_x >= 700 and mouse_x <= 900) and (mouse_y >= 650 and mouse_y <= 700):
                    total_points += lvl_points
                    total_victories += lvl_victories
                    ending.play()
                    ending_intro_end = True
        # Title and Songs Used
        ending_title = bertholdr_mainzer_fraktur_titles.render("Game Done, Let Us Go See Your Score", True, white)
        songs_used = helvetica_standard.render("Songs Used:", True, white)
        evangelion = helvetica_standard.render("Cruel Angel's Thesis (From: Neon Genesis Evangelion) By: Yoko Takahashi", True, white)
        german_song = helvetica_standard.render("Luftwaffe March (From: The Battle of Britain) By: Central Band of the Royal Air Force", True, white)
        british_song = helvetica_standard.render("Royal Air Force March Past By: Walford Davies", True, white)
        american_song = helvetica_standard.render("The US Air Force March By: Air Force Band", True, white)
        russian_song = helvetica_standard.render("Katyusha (Instramental Version) By: Unknown", True, white)
        ending_song = helvetica_standard.render("Regimentsgrus By: Heinrich Steinbeck", True, white)
        # Display Texts
        screen.fill(black)
        screen.blit(ending_title,[100,100])
        screen.blit(songs_used,[100,550])
        screen.blit(evangelion,[100,570])
        screen.blit(german_song,[100,590])
        screen.blit(british_song,[100,610])
        screen.blit(american_song,[100,630])
        screen.blit(russian_song,[100,650])
        screen.blit(ending_song,[100,670])
        drawButton(700,650)
        pygame.display.flip()
        clock.tick(10)
    # Ending (score)
    while not ending_end:
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        # Quit Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ending_end = True
                end = True
            # End Game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (mouse_x >= 700 and mouse_x <= 900) and (mouse_y >= 650 and mouse_y <= 700):
                    scores_sheet.write(str(total_points) + "\n")
                    scores_sheet.close()
                    ending_end = True
                    end = True
        # General Display
        screen.fill(white)
        drawButton(700,650)
        # Possible Outcomes
        pts_total = bertholdr_mainzer_fraktur.render("You Got: " + str(total_points) + " Points", True, black)
        vics_total = bertholdr_mainzer_fraktur.render("You Got: " + str(total_victories) + " Victories", True, black)
        gold_medal = bertholdr_mainzer_fraktur.render("Comarde! You Got Gold!", True, black)
        silver_medal = bertholdr_mainzer_fraktur.render("You Got Silver!", True, black)
        bronze_medal = bertholdr_mainzer_fraktur.render("You Got Bronze", True, black)
        loser = bertholdr_mainzer_fraktur.render("You Got Under 1200 Points??? How?????? Are you this bad?????", True, black)
        new_high_score = bertholdr_mainzer_fraktur.render("Kameraden! You Beat The Highscore!", True, black)
        max_points = bertholdr_mainzer_fraktur.render("Tovarishch! You Got the Maximum Possible Score!", True, black)
        # Display Player Victories and Points
        screen.blit(pts_total,[100,100])
        screen.blit(vics_total,[100,130])
        # Determine Player Ranking
        if total_points >= 1600:
            screen.blit(gold_medal,[100,300])
        elif total_points >= 1400:
            screen.blit(silver_medal,[100,300])
        elif total_points >= 1200:
            screen.blit(bronze_medal,[100,300])
        elif total_points < 1200:
            screen.blit(loser,[100,300])
        # Player Hitting Highscore and/or New Record
        if total_points > high_score:
            screen.blit(new_high_score,[100,330])
        if total_points == 2400:
            screen.blit(max_points,[100,360])
        pygame.display.flip()
        clock.tick(10)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()