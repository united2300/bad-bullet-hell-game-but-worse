# ruh...??!??!?!?
try:
  import pygame
  import random
  import sys
  import os
  import math  # Import the math module
except Exception as e:
  print(e)
  input("")

# Initialize Pygame
try:
  pygame.init()
except Exception as e:
  print(e)
  input("")

try:
  # Constants
  WIDTH, HEIGHT = 0, 0
  aaa = False

  # Constants for enemy bullets
  enemy_bullet_color = (255, 0, 0)  # Red color for enemy bullets
  BULLET_WIDTH = 5
  BULLET_HEIGHT = 10
  bullet_speed = 5
  enemy_bullet_damage = 3
  enemy_bullet_speed = 0.01

  # Create a class for enemy bullets
  class EnemyBullet:
      def __init__(self, x, y):
          self.x = x
          self.y = y
          self.speed = 7.5
          self.chase_duration = pygame.time.get_ticks()
          self.timestamp = pygame.time.get_ticks()  # Add a timestamp when the bullet is created


      def move_towards_player(self, player_x, player_y):
          # Check if the chase duration has exceeded 1 second
          if pygame.time.get_ticks() - self.chase_duration > 800:
              return

          angle = math.atan2(player_y + 10 - self.y, player_x + 10 - self.x)
          self.x += self.speed * math.cos(angle)
          self.y += self.speed * math.sin(angle)

  enemy_bullets = []  # List to store enemy bullets


  PLAYER_MAX_HP = 100  # Max player HP
  PLAYER_HP = PLAYER_MAX_HP  # Set player HP to max initially
  PLAYER_ATK = 5
  PLAYER_SPEED = 5
  PLAYER_EXP = 0
  PLAYER_EXP_CAP = 100  # Experience needed to level up
  PLAYER_LEVEL = 1
  PLAYER_HEALTH_REGEN = 0.01  # Health regeneration rate (1 per tick.... i think?????)

  # Allied attributes
  allieds = []
  allied_speed = PLAYER_SPEED * 2
  allied_size = 12
  allied_attack = PLAYER_ATK

  # Constants for handling allied spawning
  allied_spawn_timer = 0
  allied_spawn_interval = 666  # Spawn interval in milliseconds


  ENEMY_1_HP = 5
  ENEMY_1_ATK = 5
  ENEMY_1_SPEED = 2
  ENEMY_1_EXP_REWARD = 10

  ENEMY_2_HP = 10
  ENEMY_2_ATK = 5
  ENEMY_2_SPEED = 3
  ENEMY_2_EXP_REWARD = 20

  ENEMY_3_HP = 15
  ENEMY_3_ATK = 5
  ENEMY_3_SPEED = 3.5
  ENEMY_3_EXP_REWARD = 30

  ENEMY_4_HP = 20
  ENEMY_4_ATK = 5
  ENEMY_4_SPEED = 3
  ENEMY_4_EXP_REWARD = 40

  ENEMY_5_HP = 20
  ENEMY_5_ATK = 5
  ENEMY_5_SPEED = 4
  ENEMY_5_EXP_REWARD = 50

  ENEMY_6_HP = 900
  ENEMY_6_ATK = 1
  ENEMY_6_SPEED = 3.25
  ENEMY_6_EXP_REWARD = 305

  ENEMY_7_HP = 10
  ENEMY_7_ATK = 5
  ENEMY_7_SPEED = 2
  ENEMY_7_EXP_REWARD = 10

  ENEMY_8_HP = 150
  ENEMY_8_ATK = 1.2
  ENEMY_8_SPEED = 3.35
  ENEMY_8_EXP_REWARD = 505

  ENEMY_9_HP = 200
  ENEMY_9_ATK = 1.3
  ENEMY_9_SPEED = 3.45
  ENEMY_9_EXP_REWARD = 605

  TEST_ENEMY_HP = 50
  TEST_ENEMY_ATK = 5
  TEST_ENEMY_SPEED = 2
  TEST_ENEMY_EXP_REWARD = 0

  # Colors
  WHITE = (255, 255, 255)
  BLUE = (0, 0, 255)
  RED = (255, 0, 0)
  DARK_RED = (139, 0, 0)  # Dark red color
  GREEN = (0, 255, 0)  # Green color for the experience bar
  YELLOW = (255, 255, 0)  # Yellow color
  ORANGE = (255, 165, 0)  # Orange color
  PINK = (255, 192, 203)  # Pink color
  PURPLE = (128, 0, 128) # Purple color

  # Get the screen size
  infoObject = pygame.display.Info()
  WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h

  # Create the screen
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("Mildly interesting survival game.")
  # The games background image
  background_image = pygame.image.load("background.png").convert_alpha()

  # time
  clock = pygame.time.Clock()
  FPS = 0

  # Before the main game loop

  class_selection = True
  player_class = None

  while class_selection:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if warrior_button_rect.collidepoint(mouse_pos):
          player_class = "warrior"
          class_selection = False
        elif mage_button_rect.collidepoint(mouse_pos):
          player_class = "mage"
          class_selection = False
        elif ranger_button_rect.collidepoint(mouse_pos):
          player_class = "ranger"
          class_selection = False

    screen.blit(background_image, (0, 0))

    # Draw class selection buttons
    warrior_button_rect = pygame.draw.rect(screen, (255, 0, 0), (100, 200, 200, 50))
    mage_button_rect = pygame.draw.rect(screen, (0, 0, 255), (100, 300, 200, 50))
    ranger_button_rect = pygame.draw.rect(screen, (0, 255, 0), (100, 400, 200, 50))

    # Text on buttons
    font = pygame.font.Font(None, 36)
    warrior_text = font.render("Warrior", True, (255, 255, 255))
    mage_text = font.render("Mage", True, (255, 255, 255))
    ranger_text = font.render("Ranger", True, (255, 255, 255))
    screen.blit(warrior_text, (140, 210))
    screen.blit(mage_text, (150, 310))
    screen.blit(ranger_text, (145, 410))
    clock.tick(FPS)

    pygame.display.update()

  # After class selection


  # Player attributes
  player_x = WIDTH // 2
  player_y = HEIGHT // 2
  player_max_hp = PLAYER_MAX_HP
  player_hp = PLAYER_HP
  player_atk = PLAYER_ATK
  player_speed = PLAYER_SPEED
  original_player_speed = PLAYER_SPEED  # Store the original player speed
  original_player_attack = PLAYER_ATK  # Store the original player speed
  player_exp = PLAYER_EXP
  player_exp_cap = PLAYER_EXP_CAP
  player_level = PLAYER_LEVEL
  player_health_regen = PLAYER_HEALTH_REGEN
  player_inventory = {}  # the inventory is a dictionary for stacking items


  # Enemy attributes
  enemies = []
  spawn_time = 0
  enemy1_spawn_prob = 0.8
  enemy2_spawn_prob = 0
  enemy3_spawn_prob = 0
  enemy4_spawn_prob = 0
  enemy5_spawn_prob = 0
  enemy6_spawn_prob = 0
  enemy7_spawn_prob = 0
  enemy8_spawn_prob = 0
  enemy9_spawn_prob = 0

  enemy1_name = "Red"
  enemy2_name = "Dark red"
  enemy3_name = "Yellow"
  enemy4_name = "Orange"
  enemy5_name = "Pink"
  enemy6_name = "Black"
  enemy7_name = "Purple"
  enemy8_name = "Green"
  enemy9_name = "White"
  test_enemy_name = "Test Enemy"

  max_enemies = 40
  if WIDTH + HEIGHT > 200:
    max_enemies += round((WIDTH + HEIGHT) / 100)
  print (max_enemies)
  print (WIDTH, HEIGHT)

  Spawned_boss_1 = False
  Spawned_boss_2 = False
  Spawned_boss_3 = False
  Spawned_boss_4 = False
  Boss_in_map = False
  renderinv = False

  EnemyCountUp1 = False
  EnemyCountUp2 = False
  EnemyCountUp3 = False
  EnemyCountUp4 = False



  def forced_spawn(enemy):

      edge = random.randint(0, 3)

      if edge == 0:
          x = 0
          y = random.randint(0, HEIGHT)
      elif edge == 1:
          x = random.randint(0, WIDTH)
          y = 0
      elif edge == 2:
          x = WIDTH
          y = random.randint(0, HEIGHT)
      else:
          x = random.randint(0, WIDTH)
          y = HEIGHT

      if enemy == "Red":
          enemy = {
              'x': x,
              'y': y,
              'hp': ENEMY_1_HP,
              'max_hp': ENEMY_1_HP,
              'atk': ENEMY_1_ATK,
              'speed': ENEMY_1_SPEED,
              'exp_reward': ENEMY_1_EXP_REWARD,
              'name': enemy1_name,
          }
          enemies.append(enemy)
      elif enemy == "Dark red":
          enemy = {
              'x': x,
              'y': y,
              'hp': ENEMY_2_HP,
              'max_hp': ENEMY_2_HP,
              'atk': ENEMY_2_ATK,
              'speed': ENEMY_2_SPEED,
              'exp_reward': ENEMY_2_EXP_REWARD,
              'name': enemy2_name,
          }
          enemies.append(enemy)
      elif enemy == "Yellow":
          enemy = {
              'x': x,
              'y': y,
              'hp': ENEMY_3_HP,
              'max_hp': ENEMY_3_HP,
              'atk': ENEMY_3_ATK,
              'speed': ENEMY_3_SPEED,
              'exp_reward': ENEMY_3_EXP_REWARD,
              'name': enemy3_name,
          }
          enemies.append(enemy)
      elif enemy == "Orange":
          enemy = {
              'x': x,
              'y': y,
              'hp': ENEMY_4_HP,
              'max_hp': ENEMY_4_HP,
              'atk': ENEMY_4_ATK,
              'speed': ENEMY_4_SPEED,
              'exp_reward': ENEMY_4_EXP_REWARD,
              'name': enemy4_name,
          }
          enemies.append(enemy)
      elif enemy == "Pink":
          enemy = {
              'x': x,
              'y': y,
              'hp': ENEMY_5_HP,
              'max_hp': ENEMY_5_HP,
              'atk': ENEMY_5_ATK,
              'speed': ENEMY_5_SPEED,
              'exp_reward': ENEMY_5_EXP_REWARD,
              'name': enemy5_name,
          }
          enemies.append(enemy)
      elif enemy == "Black":
          enemy = {
              'x': x,
              'y': y,
              'hp': ENEMY_6_HP,
              'max_hp': ENEMY_6_HP,
              'atk': ENEMY_6_ATK,
              'speed': ENEMY_6_SPEED,
              'exp_reward': ENEMY_6_EXP_REWARD,
              'name': enemy6_name,
          }
          enemies.append(enemy)

      elif enemy == "Purple":
          enemy = {
              'x': x,
              'y': y,
              'hp': ENEMY_7_HP,
              'max_hp': ENEMY_7_HP,
              'atk': ENEMY_7_ATK,
              'speed': ENEMY_7_SPEED,
              'exp_reward': ENEMY_7_EXP_REWARD,
              'name': enemy7_name,
          }
          enemies.append(enemy)

      elif enemy == "Green":
          enemy = {
              'x': x,
              'y': y,
              'hp': ENEMY_8_HP,
              'max_hp': ENEMY_8_HP,
              'atk': ENEMY_8_ATK,
              'speed': ENEMY_8_SPEED,
              'exp_reward': ENEMY_8_EXP_REWARD,
              'name': enemy8_name,
          }
          enemies.append(enemy)

      elif enemy == "White":
          enemy = {
              'x': x,
              'y': y,
              'hp': ENEMY_9_HP,
              'max_hp': ENEMY_9_HP,
              'atk': ENEMY_9_ATK,
              'speed': ENEMY_9_SPEED,
              'exp_reward': ENEMY_9_EXP_REWARD,
              'name': enemy8_name,
          }
          enemies.append(enemy)

      elif enemy == "Test Enemy":
          enemy = {
              'x': x,
              'y': y,
              'hp': TEST_ENEMY_HP,
              'max_hp': TEST_ENEMY_HP,
              'atk': TEST_ENEMY_ATK,
              'speed': TEST_ENEMY_HP,
              'exp_reward': TEST_ENEMY_EXP_REWARD,
              'name': test_enemy_name,
          }
          enemies.append(enemy)


  # Modify the spawn_enemy function to spawn enemies only on the edges
  def spawn_enemy():
      global spawn_time, enemy1_spawn_prob, enemy2_spawn_prob, enemy3_spawn_prob, enemy4_spawn_prob, enemy5_spawn_prob, enemy6_spawn_prob, enemy7_spawn_prob, enemy8_spawn_prob, enemy9_spawn_prob, max_enemies, Boss_in_map, EnemyCountUp1, EnemyCountUp2, EnemyCountUp3, EnemyCountUp4

      if len(enemies) < max_enemies and Boss_in_map == False:
          # Adjusting the enemy spawnrates as time goes on
          if current_time < 7500:
            enemy1_spawn_prob = 0.8
            enemy2_spawn_prob = 0
            enemy3_spawn_prob = 0
            enemy4_spawn_prob = 0
            enemy5_spawn_prob = 0
            enemy6_spawn_prob = 0
            enemy7_spawn_prob = 0
            enemy8_spawn_prob = 0
            enemy9_spawn_prob = 0
          if current_time > 7500 and current_time < 15000:
            enemy1_spawn_prob = 0.8
            enemy2_spawn_prob = 0.2
            enemy3_spawn_prob = 0
            enemy4_spawn_prob = 0
            enemy5_spawn_prob = 0
            enemy6_spawn_prob = 0
            enemy7_spawn_prob = 0.25
            enemy8_spawn_prob = 0
            enemy9_spawn_prob = 0
          if current_time > 15000 and current_time < 30000:
            enemy1_spawn_prob = 0.8
            enemy2_spawn_prob = 0.3
            enemy3_spawn_prob = 0.1
            enemy4_spawn_prob = 0
            enemy5_spawn_prob = 0
            enemy6_spawn_prob = 0
            enemy7_spawn_prob = 0.25
            enemy8_spawn_prob = 0
            enemy9_spawn_prob = 0
          if current_time > 30000 and current_time < 45000:
            enemy1_spawn_prob = 0.8
            enemy2_spawn_prob = 0.5
            enemy3_spawn_prob = 0.3
            enemy4_spawn_prob = 0.15
            enemy5_spawn_prob = 0
            enemy6_spawn_prob = 0
            enemy7_spawn_prob = 0.25
            enemy8_spawn_prob = 0
            enemy9_spawn_prob = 0
          if current_time > 45000 and current_time < 65000:
            enemy1_spawn_prob = 0.8
            enemy2_spawn_prob = 0.6
            enemy3_spawn_prob = 0.35
            enemy4_spawn_prob = 0.2
            enemy5_spawn_prob = 0.1
            enemy6_spawn_prob = 0
            enemy7_spawn_prob = 0.25
            enemy8_spawn_prob = 0
            enemy9_spawn_prob = 0
          if current_time > 65000 and current_time < 90000:
            enemy1_spawn_prob = 0.8
            enemy2_spawn_prob = 0.7
            enemy3_spawn_prob = 0.4
            enemy4_spawn_prob = 0.3
            enemy5_spawn_prob = 0.175
            enemy6_spawn_prob = 0
            enemy7_spawn_prob = 0.25
            enemy8_spawn_prob = 0
            enemy9_spawn_prob = 0
          if current_time > 90000:
            enemy1_spawn_prob = 0.65
            enemy2_spawn_prob = 0.8
            enemy3_spawn_prob = 0.7
            enemy4_spawn_prob = 0.6
            enemy5_spawn_prob = 0.2
            enemy6_spawn_prob = 0
            enemy7_spawn_prob = 0.25
            enemy8_spawn_prob = 0
            enemy9_spawn_prob = 0

          # Beefing up the max enemy count for M O R E    D I F F I C U L T Y in the mid to late-game
          if current_time > 3000 and EnemyCountUp1 == False:
            EnemyCountUp1 = True
            max_enemies += 5

          if current_time > 60000 and EnemyCountUp2 == False:
            EnemyCountUp2 = True
            max_enemies += 5

          if current_time > 90000 and EnemyCountUp3 == False:
            EnemyCountUp3 = True
            max_enemies += 5
          if current_time > 110000 and EnemyCountUp4 == False:
            EnemyCountUp3 = True
            max_enemies += 5


          edge = random.randint(0, 3)

          if edge == 0:
              x = 0
              y = random.randint(0, HEIGHT)
          elif edge == 1:
              x = random.randint(0, WIDTH)
              y = 0
          elif edge == 2:
              x = WIDTH
              y = random.randint(0, HEIGHT)
          else:
              x = random.randint(0, WIDTH)
              y = HEIGHT

          if random.random() < enemy1_spawn_prob:
              enemy = {
                  'x': x,
                  'y': y,
                  'hp': ENEMY_1_HP,
                  'max_hp': ENEMY_1_HP,
                  'atk': ENEMY_1_ATK,
                  'speed': ENEMY_1_SPEED,
                  'exp_reward': ENEMY_1_EXP_REWARD,
                  'name': enemy1_name,
              }
              enemies.append(enemy)

          if random.random() < enemy2_spawn_prob:
              enemy = {
                  'x': x,
                  'y': y,
                  'hp': ENEMY_2_HP,
                  'max_hp': ENEMY_2_HP,
                  'atk': ENEMY_2_ATK,
                  'speed': ENEMY_2_SPEED,
                  'exp_reward': ENEMY_2_EXP_REWARD,
                  'name': enemy2_name,
              }
              enemies.append(enemy)

          if random.random() < enemy3_spawn_prob:
              enemy = {
                  'x': x,
                  'y': y,
                  'hp': ENEMY_3_HP,
                  'max_hp': ENEMY_3_HP,
                  'atk': ENEMY_3_ATK,
                  'speed': ENEMY_3_SPEED,
                  'exp_reward': ENEMY_3_EXP_REWARD,
                  'name': enemy3_name,
              }
              enemies.append(enemy)

          if random.random() < enemy4_spawn_prob:
              enemy = {
                  'x': x,
                  'y': y,
                  'hp': ENEMY_4_HP,
                  'max_hp': ENEMY_4_HP,
                  'atk': ENEMY_4_ATK,
                  'speed': ENEMY_4_SPEED,
                  'exp_reward': ENEMY_4_EXP_REWARD,
                  'name': enemy4_name,
              }
              enemies.append(enemy)

          if random.random() < enemy5_spawn_prob:
              enemy = {
                  'x': x,
                  'y': y,
                  'hp': ENEMY_5_HP,
                  'max_hp': ENEMY_5_HP,
                  'atk': ENEMY_5_ATK,
                  'speed': ENEMY_5_SPEED,
                  'exp_reward': ENEMY_5_EXP_REWARD,
                  'name': enemy5_name,
              }
              enemies.append(enemy)


          if random.random() < enemy7_spawn_prob:
              enemy = {
                  'x': x,
                  'y': y,
                  'hp': ENEMY_7_HP,
                  'max_hp': ENEMY_7_HP,
                  'atk': ENEMY_7_ATK,
                  'speed': ENEMY_7_SPEED,
                  'exp_reward': ENEMY_7_EXP_REWARD,
                  'name': enemy7_name,
              }
              enemies.append(enemy)

          spawn_time = pygame.time.get_ticks()


  # Function to calculate the distance between two points
  def distance(x1, y1, x2, y2):
      return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

  # Function to handle enemy repulsion
  def handle_enemy_repulsion():
      for i in range(len(enemies)):
          for j in range(i + 1, len(enemies)):
              enemy1 = enemies[i]
              enemy2 = enemies[j]
            # If the enemies are touching and NEITHER of the enemies are purple OR if the enemies are touching and BOTH of the enemies are purple push them away from eachother
              if distance(enemy1['x'], enemy1['y'], enemy2['x'], enemy2['y']) < 30 and enemy1['name'] != "Purple" and enemy2['name'] != "Purple" or distance(enemy1['x'], enemy1['y'], enemy2['x'], enemy2['y']) < 30 and enemy1['name'] and enemy2['name'] == "Purple":
                  # Calculate angle between the two enemies
                  angle = math.atan2(enemy2['y'] - enemy1['y'], enemy2['x'] - enemy1['x'])
                  # Calculate the repulsion force
                  repulsion_force = 2.0
                  enemy1['x'] -= math.cos(angle) * repulsion_force
                  enemy1['y'] -= math.sin(angle) * repulsion_force
                  enemy2['x'] += math.cos(angle) * repulsion_force
                  enemy2['y'] += math.sin(angle) * repulsion_force

  # Function to draw a health bar
  def draw_health_bar(x, y, current_hp, max_hp, color):
      bar_length = 50
      bar_height = 5
      fill = (current_hp / max_hp) * bar_length
      outline_rect = pygame.Rect(x, y, bar_length, bar_height)
      fill_rect = pygame.Rect(x, y, fill, bar_height)
      pygame.draw.rect(screen, color, fill_rect)
      pygame.draw.rect(screen, WHITE, outline_rect, 1)

  # Function to draw an experience bar
  def draw_exp_bar(x, y, current_exp, exp_cap):
      bar_length = 100
      bar_height = 5
      fill = (current_exp / exp_cap) * bar_length
      outline_rect = pygame.Rect(x, y, bar_length, bar_height)
      fill_rect = pygame.Rect(x, y, fill, bar_height)
      pygame.draw.rect(screen, GREEN, fill_rect)
      pygame.draw.rect(screen, WHITE, outline_rect, 1)

  # Function to level up the player
  def level_up():
      global player_level, player_max_hp, player_atk, player_speed, player_health_regen, player_exp, player_exp_cap, allied_spawn_interval, allied_speed, allied_size, allied_attack
      player_level += 1
      player_max_hp += 0.2
      player_atk += 0.1
      player_speed += 0.075
      player_exp_cap += 1

      allied_speed += 0.075
      allied_size = 12
      allied_attack += 0.1

      original_player_speed = player_speed
      original_player_attack = player_atk
      allied_spawn_interval *= 0.99

  def use_health_potion():
    global player_hp, player_inventory
    if "Health Potion" in player_inventory and player_inventory["Health Potion"] > 0:
        player_inventory["Health Potion"] -= 1
        player_hp = min(player_max_hp, player_hp + 20)

  def use_speed_potion():
    global player_speed, player_inventory, original_player_speed
    if "Speed Potion" in player_inventory and player_inventory["Speed Potion"] > 0:
        #original_player_speed = player_speed  # Store the original player speed
        player_speed += 0.025
        #pygame.time.set_timer(pygame.USEREVENT, 3000)  # Set a timer for 3 seconds
        player_inventory["Speed Potion"] -= 1

  def use_dps_potion():
    global player_atk, player_inventory, original_player_attack
    if "DPS Potion" in player_inventory and player_inventory["DPS Potion"] > 0:
        #original_player_attack = player_atk  # Store the original player speed
        player_atk += 0.25
        #pygame.time.set_timer(pygame.USEREVENT, 3000)  # Set a timer for 3 seconds
        player_inventory["DPS Potion"] -= 1

  def drop_item():
    # 66% chance to drop a potion
    rng = random.random()
    if rng < 0.66:
        rng = random.random()
        # 50% chance for the dropped item to be a health potion
        if rng < 0.50:
            if "Health Potion" not in player_inventory:
                player_inventory["Health Potion"] = 1
            else:
                player_inventory["Health Potion"] += 1

        # 10% chance for the dropped item to be a speed potion
        elif rng > 0.5 and rng < 0.75: 
            if "Speed Potion" not in player_inventory:
                player_inventory["Speed Potion"] = 1
            else:
                player_inventory["Speed Potion"] += 1

        # 15%% chance for the dropped item to be a DPS potion
        elif rng > 0.75: 
            if "DPS Potion" not in player_inventory:
                player_inventory["DPS Potion"] = 1
            else:
                player_inventory["DPS Potion"] += 1

  # Function to display the inventory (and general UI)
  def render_inventory():
    font = pygame.font.Font(None, 36)
    inventory_text = font.render("Inventory:", True, (0, 0, 0))
    lvl_text = font.render(f"LVL: {player_level}", True, (0, 0, 0))
    timer_text = font.render(f"Timer: {current_time / 1000}", True, (0, 0, 0))
    screen.blit(inventory_text, (10, 10))
    screen.blit(lvl_text, ((WIDTH - 100), 10))
    screen.blit(timer_text, ((WIDTH / 2 - 50), 10))
    for i, item in enumerate(player_inventory.keys()):
        item_text = font.render(f"{i + 1}: {item} x{player_inventory[item]}", True, (0, 0, 0))
        screen.blit(item_text, (10, 10 + (i + 1) * 30))


  # Function to spwan cute little blue boys
  def spawn_allied(type):
    global allied_spawn_timer, last_key_pressed, allied_speed
    current_time = pygame.time.get_ticks()
    if current_time - allied_spawn_timer > allied_spawn_interval:
        # Warrior
        for _ in range(5):
          if type == "slash":
              allied = {
                      'id': _,
                      'x': player_x,
                      'y': player_y,
                      'speed': (allied_speed),
                      'type': type,
                      'movement': "directional",
                      'direction': last_key_pressed,
                      'spawn_time': current_time  # Store the spawn time'
              }
              allieds.append(allied)
          
        # Mage
        if type == "homing_bullet":
            allied = {
                'x': player_x,
                'y': player_y,
                'speed': (allied_speed),
                'type': type,
                'movement': "homing_strong",
            }
            allieds.append(allied)
        if len(allieds) > 5:
          allieds.remove(allied)
        allied_spawn_timer = current_time

  # Function to handle allied movement towards the nearest enemy
  def move_allied_towards_enemy(allied, enemy):
      if allied['movement'] == "directional":
        
          if allied['id'] == 0: # center
              if allied['direction'] == "left":
                  allied['x'] -= allied['speed']
              if allied['direction'] == "right":
                  allied['x'] += allied['speed']
              if allied['direction'] == "up":
                  allied['y'] -= allied['speed']
              if allied['direction'] == "down":
                  allied['y'] += allied['speed']
                
          if allied['id'] == 1: # 90* leftmost to the center
            if allied['direction'] == "left":
                allied['y'] += allied['speed']
            if allied['direction'] == "right":
                allied['y'] -= allied['speed']
            if allied['direction'] == "up":
                allied['x'] -= allied['speed']
            if allied['direction'] == "down":
                allied['x'] += allied['speed']
              
          if allied['id'] == 2: # 90* rightmost to the center
            if allied['direction'] == "left":
                allied['y'] -= allied['speed']
            if allied['direction'] == "right":
                allied['y'] += allied['speed']
            if allied['direction'] == "up":
                allied['x'] += allied['speed']
            if allied['direction'] == "down":
                allied['x'] -= allied['speed']
        
          if allied['id'] == 3:  # 45* rightmost to the center
            diagonal_speed = allied['speed'] / math.sqrt(2)  # Calculate the diagonal speed
            if allied['direction'] == "left":
                allied['x'] -= diagonal_speed
                allied['y'] += diagonal_speed  # Adjust y-axis for 45-degree movement
            elif allied['direction'] == "right":
                allied['x'] += diagonal_speed
                allied['y'] -= diagonal_speed  # Adjust y-axis for 45-degree movement
            elif allied['direction'] == "up":
                allied['y'] -= diagonal_speed
                allied['x'] -= diagonal_speed  # Adjust x-axis for 45-degree movement
            elif allied['direction'] == "down":
                allied['y'] += diagonal_speed
                allied['x'] += diagonal_speed  # Adjust x-axis for 45-degree movement
          if allied['id'] == 4:  # 45* leftmost to the center
            diagonal_speed = allied['speed'] / math.sqrt(2)  # Calculate the diagonal speed
            if allied['direction'] == "left":
                allied['x'] -= diagonal_speed
                allied['y'] -= diagonal_speed  # Adjust y-axis for 45-degree movement
            elif allied['direction'] == "right":
                allied['x'] += diagonal_speed
                allied['y'] += diagonal_speed  # Adjust y-axis for 45-degree movement
            elif allied['direction'] == "up":
                allied['y'] -= diagonal_speed
                allied['x'] += diagonal_speed  # Adjust x-axis for 45-degree movement
            elif allied['direction'] == "down":
                allied['y'] += diagonal_speed
                allied['x'] -= diagonal_speed  # Adjust x-axis for 45-degree movement

    
      if allied['movement'] == "homing_strong":
          if enemy['name'] == "Purple":
              allied['speed'] *= 0.75

          if allied['x'] < enemy['x']:
              allied['x'] += allied['speed']
              if allied['x'] > enemy['x']:
                  allied['x'] = enemy['x']
          elif allied['x'] > enemy['x']:
              allied['x'] -= allied['speed']
              if allied['x'] < enemy['x']:
                  allied['x'] = enemy['x']
          if allied['y'] < enemy['y']:
              allied['y'] += allied['speed']
              if allied['y'] > enemy['y']:
                  allied['y'] = enemy['y']
          elif allied['y'] > enemy['y']:
              allied['y'] -= allied['speed']
              if allied['y'] < enemy['y']:
                  allied['y'] = enemy['y']

          if enemy['name'] == "Purple":
              allied['speed'] = round(allied['speed'] * 1.33333333)
            

  # Game loop
  clock = pygame.time.Clock()

  heal_timer = 0
  heal_interval = 400  # 400 milliseconds (0.4 seconds)

  while True:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          elif event.type == pygame.KEYDOWN:
              if event.key == pygame.K_SPACE:  # Use health potion when space is pressed
                  use_health_potion()
              elif event.key == pygame.K_z:
                  use_speed_potion()
              elif event.key == pygame.K_x:
                  use_dps_potion()
              #elif event.key == pygame.K_i:  # Display the inventory when 'i' is pressed
                  #render_inventory()
              elif event.key == pygame.K_c:  # Spawn allied blue square when 'c' is pressed
                  if player_class == "mage":
                      spawn_allied("homing_bullet")
                  elif player_class == "warrior":
                      spawn_allied("slash")
                  elif player_class == "ranger":
                      spawn_allied("")

              """elif event.type == pygame.USEREVENT:  # Event for speed potion timer
              player_speed = original_player_speed  # Reset the player's speed back to normal
              player_atk = original_player_attack"""



      # Handle player movement
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT] or keys[pygame.K_a]:
          player_x = max(0, player_x - player_speed)  # Bound movement on the left side
          last_key_pressed = "left"
      if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
          player_x = min(WIDTH - 20, player_x + player_speed)  # Bound movement on the right side
          last_key_pressed = "right"
      if keys[pygame.K_UP] or keys[pygame.K_w]:
          player_y = max(0, player_y - player_speed)  # Bound movement on the top side
          last_key_pressed = "up"
      if keys[pygame.K_DOWN] or keys[pygame.K_s]:
          player_y = min(HEIGHT - 20, player_y + player_speed)  # Bound movement on the bottom side
          last_key_pressed = "down"


      # Keep the player within the game window
      player_x = max(0, min(WIDTH, player_x))
      player_y = max(0, min(HEIGHT, player_y))

      # Heal the player by the specified rate
      current_time = pygame.time.get_ticks()
      if current_time - heal_timer >= heal_interval:
          player_hp += (player_max_hp * player_health_regen)
          if player_hp > player_max_hp:
              player_hp = player_max_hp
          heal_timer = current_time

      # Check if we want to spawn enemies
      current_time = pygame.time.get_ticks()

      if current_time - spawn_time > 1000:
          spawn_enemy()

      # Bosses!


      if current_time > 45000 and Spawned_boss_1 == False:
          Spawned_boss_1 = True
          #enemies = [] # Kills all enemies.
          forced_spawn("Black") # Spawn a black
          Boss_in_map = True

      if current_time > 100000 and Spawned_boss_2 == False:
          Spawned_boss_2 = True
          #enemies = [] # Kills all enemies.
          forced_spawn("Black") # Spawn one black
          e = 10
          while e != 0:
              e -= 1
              forced_spawn("Pink") # Spawn 10 pinks
          Boss_in_map = True

      if current_time > 150000 and Spawned_boss_3 == False:
          Spawned_boss_3 = True
          #enemies = [] # Kills all enemies.
          forced_spawn("Black") # Spawn one black
          e = 15
          while e != 0:
              e -= 1
              forced_spawn("Pink") # Spawn 15 pinks
          Boss_in_map = True

      if current_time > 200000 and Spawned_boss_4 == False:
          Spawned_boss_4 = True
          #enemies = [] # Kills all enemies.
          e = 1
          while e != 0:
              e -= 1
              forced_spawn("Black") # Spawn 2 blacks
          e = 15
          while e != 0:
              e -= 1
              forced_spawn("Pink") # Spawn 15 pinks
          Boss_in_map = True

      """if Boss_in_map == True:
          for enemy in enemies:
            if enemy['name'] == "Red" or enemy['name'] == "Dark red" or enemy['name'] == "Yellow" or enemy['name'] == "Pink" or enemy['name'] == "Orange":
              enemy['hp'] = 0""" # unused as of now. used to kill all enemies immediately if there's a boss on the map. i forgor why this was bad, prob was buggy as hell all i think. either way i found a better way to do it. i'll keep this here just in case its needed for some reason though.

      # Handle enemy repulsion
      handle_enemy_repulsion()

      # Update allied positions and check for collisions with enemies
      for allied in allieds:
          nearest_enemy = None
          min_distance = float('inf')
          if allied['type'] == 'slash':
              move_allied_towards_enemy(allied, nearest_enemy)
          if allied['type'] == 'slash' and current_time - allied['spawn_time'] >= 500:  # Check lifespan for 'slash' type allies
              allieds.remove(allied)

          for enemy in enemies:
              dist = distance(allied['x'], allied['y'], enemy['x'], enemy['y'])
              if dist < min_distance:
                  min_distance = dist
                  nearest_enemy = enemy
          if nearest_enemy is not None and allied['type'] != "slash":
              move_allied_towards_enemy(allied, nearest_enemy)
          if nearest_enemy is not None:
              if distance(allied['x'], allied['y'], nearest_enemy['x'], nearest_enemy['y']) < 15:
                  if nearest_enemy['name'] == "Purple":
                      nearest_enemy['hp'] -= allied_attack / 2
                  else:
                      nearest_enemy['hp'] -= allied_attack
                  try:
                      allieds.remove(allied)
                  except Exception as e:
                    print (e)
                    continue





      # Level up if the player has enough experience
      while player_exp >= player_exp_cap:
          player_exp -= player_exp_cap
          level_up()

      # Check if the player's HP is less than 1
      if player_hp < 1:
          pygame.quit()
          sys.exit()

      # Clear the screen
      #screen.fill(WHITE)

      # Blit the background image onto the screen
      screen.blit(background_image, (0, 0))

      # Update the display
      #pygame.display.flip()

      # Draw player
      pygame.draw.rect(screen, BLUE, (player_x, player_y, 20, 20))

      # Draw player's health bar and experience bar
      draw_health_bar(player_x, player_y - 10, player_hp, player_max_hp, BLUE)
      draw_exp_bar(player_x, player_y - 20, player_exp, player_exp_cap)

      # Draw enemies and their health bars
      # Update enemy positions and check for collisions
      for enemy in enemies:
          enemy['speed'] += 0.0005 # gradually increase enemy speed
        # If the enemy isn't a purple OR the enemy isn't close to the the player move normally.
          if enemy['name'] != "Purple" or abs(enemy['x'] - player_x) > 150 or abs(enemy['y'] - player_y) > 150:
            if enemy['x'] < player_x:
                enemy['x'] += enemy['speed']
                if enemy['x'] > player_x:
                  enemy['x'] = player_x

            elif enemy['x'] > player_x:
                enemy['x'] -= enemy['speed']
                if enemy['x'] < player_x:
                    enemy['x'] = player_x

            if enemy['y'] < player_y:
                enemy['y'] += enemy['speed']
                if enemy['y'] > player_y:
                    enemy['y'] = player_y

            elif enemy['y'] > player_y:
                enemy['y'] -= enemy['speed'] 
                if enemy['y'] < player_y:
                    enemy['y'] = player_y


          elif enemy['name'] == "Purple": # Move away from player
            # This code is used for the purple enemy
            if enemy['x'] < player_x:
              enemy['x'] -= enemy['speed'] * 0.333
              if enemy['x'] > player_x:
                enemy['x'] = player_x

            elif enemy['x'] > player_x:
              enemy['x'] += enemy['speed'] * 0.333
              if enemy['x'] < player_x:
                  enemy['x'] = player_x

            if enemy['y'] < player_y:
              enemy['y'] -= enemy['speed'] * 0.333
              if enemy['y'] > player_y:
                  enemy['y'] = player_y

            elif enemy['y'] > player_y:
              enemy['y'] += enemy['speed'] * 0.333
              if enemy['y'] < player_y:
                  enemy['y'] = player_y

          if enemy['x'] < 0:
            enemy['x'] = 0
          elif enemy['x'] > (WIDTH - 21):
            enemy['x'] = (WIDTH - 21)

          if enemy['y'] < 0:
            enemy['y'] = 0
          elif enemy['y'] > (HEIGHT - 41):
            enemy['y'] = (HEIGHT - 41)



          if abs(enemy['x'] - player_x) < 15 and abs(enemy['y'] - player_y) < 15:
              player_hp -= enemy['atk']
              enemy['hp'] -= player_atk

          if enemy['hp'] <= 0:
              drop_item()  # Call the function to check for a potion drop
              if enemy['name'] == "Black":
                  Boss_in_map = False
              player_exp += enemy['exp_reward']
              enemies.remove(enemy)

          # enemy segment 1 (2)
          if enemy['name'] == enemy1_name:
              color = RED
              size = 20  # Modify size as needed
          elif enemy['name'] == enemy2_name:
              color = DARK_RED
              size = 20  # Modify size as needed
          elif enemy['name'] == enemy3_name:
              color = YELLOW
              size = 15  # Modify size as needed
          elif enemy['name'] == enemy4_name:
              color = ORANGE
              size = 20  # Modify size as needed
          elif enemy['name'] == enemy5_name:
              color = PINK
              size = 20  # Modify size as needed
          elif enemy['name'] == enemy6_name:
              color = (0, 0, 0)  # Black color
              size = 30  # Adjust the size as needed
          elif enemy['name'] == enemy7_name:
              color = (128, 0, 128)  # Purple color
              size = 17.5  # Modify size as needed
          elif enemy['name'] == enemy8_name:
              color = (34, 139, 34)  # Green color
              size = 35  # Modify size as needed
          elif enemy['name'] == enemy9_name:
              color = WHITE
              size = 40  # Modify size as needed
          pygame.draw.rect(screen, color, (enemy['x'], enemy['y'], size, size))
          draw_health_bar(enemy['x'], enemy['y'] - 10, enemy['hp'], enemy['max_hp'], color)

        # enemy segment 2

          if enemy['name'] == enemy7_name:
            enemy_bullet_color = PURPLE
            # Spawn bullets periodically
            if random.random() < 0.018:  # Adjust probability based on game balance
                enemy_bullet = EnemyBullet(enemy['x'], enemy['y'])
                enemy_bullets.append(enemy_bullet)
                if len(enemy_bullets) > 50:
                  enemy_bullets.pop(0)

          elif enemy['name'] == enemy9_name:
            pass # Spawns enemy bullets


      # Update enemy bullets
      for enemy_bullet in enemy_bullets:
          # Move enemy bullets towards the player
          enemy_bullet.move_towards_player(player_x, player_y)
          pygame.draw.rect(screen, enemy_bullet_color, (enemy_bullet.x, enemy_bullet.y, BULLET_WIDTH, BULLET_HEIGHT))


        # Remove bullets that are off-screen or exceed the 7-second threshold
          if (
              enemy_bullet.y > HEIGHT or
              pygame.time.get_ticks() - enemy_bullet.timestamp > 7000
          ):
              enemy_bullets.remove(enemy_bullet)

          # Check for collisions with the player
          if (
              player_x < enemy_bullet.x < player_x + 20 and
              player_y < enemy_bullet.y < player_y + 20
          ):
              player_hp -= enemy_bullet_damage
              try:
                enemy_bullets.remove(enemy_bullet)
              except:
                print ("!!! WARNING: WIERD GOOFY AHHH ERROR. PANIC. !!! (Line 914 as of writing.)")


      for allied in allieds:
        pygame.draw.circle(screen, BLUE, ((allied['x'] + 10), (allied['y'] + 10)), (allied_size * 0.66))


      render_inventory()  # Call the function to display the inventory on the Pygame window

      # Update the display
      pygame.display.update()

      # Cap the frame rate
      clock.tick(35)

except Exception as e:
  print(f"An unexpected error has occured: {e}")
  input("")


time.sleep(5)
input("")

