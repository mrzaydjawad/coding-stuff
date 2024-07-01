import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
INITIAL_RADIUS = 200
RADIUS_DECREMENT = 5
MIN_RADIUS = 20  # Minimum radius before the circle disappears
CIRCLE_CENTER = (WIDTH // 2, HEIGHT // 2)
CIRCLE_RADIUS = INITIAL_RADIUS
GRAVITY = 0.06  # Increased gravity
FRICTION = 0.99  # Reduced friction coefficient
SHRINK_COOLDOWN = 10  # Frames between each shrink
SOUND_COOLDOWN = 10  # Frames between sound plays

# Colors
BLACK = (0, 0, 0)
START_COLOR = (255, 0, 0)
END_COLOR = (0, 0, 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls with Reduced Gravity")

# Load sound
try:
    collision_sound = pygame.mixer.Sound("sound effects/boom.mp3")
except pygame.error as e:
    print(f"Error loading sound: {e}")
    collision_sound = None

def interpolate_color(start_color, end_color, factor):
    return tuple(int(start_color[i] + (end_color[i] - start_color[i]) * factor) for i in range(3))

class Ball:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = 20
        self.shrink_cooldown = 0
        self.sound_cooldown = 0
        self.color_factor = 0
        self.color_direction = 1

    def update(self):
        global CIRCLE_RADIUS  # Ensure the global declaration is before usage

        self.vx *= FRICTION  # Apply reduced friction
        self.vy += GRAVITY  # Apply increased gravity
        self.x += self.vx
        self.y += self.vy

        # Collision detection with circular boundary
        distance_to_center = math.sqrt((self.x - CIRCLE_CENTER[0])**2 + (self.y - CIRCLE_CENTER[1])**2)
        if distance_to_center >= CIRCLE_RADIUS - self.radius:
            # Play sound if loaded and cooldown is 0
            if collision_sound and self.sound_cooldown == 0:
                collision_sound.play()
                self.sound_cooldown = SOUND_COOLDOWN

            # Calculate normal vector of the collision point on the circle
            nx = (self.x - CIRCLE_CENTER[0]) / distance_to_center
            ny = (self.y - CIRCLE_CENTER[1]) / distance_to_center

            # Reflect velocity vector about the normal vector
            dot_product = self.vx * nx + self.vy * ny
            self.vx -= 2 * dot_product * nx
            self.vy -= 2 * dot_product * ny

            # Adjust position to sit exactly on the boundary
            self.x = CIRCLE_CENTER[0] + (CIRCLE_RADIUS - self.radius) * nx
            self.y = CIRCLE_CENTER[1] + (CIRCLE_RADIUS - self.radius) * ny

            # Shrink circle radius if cooldown has passed
            if self.shrink_cooldown == 0:
                CIRCLE_RADIUS -= RADIUS_DECREMENT
                self.shrink_cooldown = SHRINK_COOLDOWN

        # Decrease cooldown counters if they're above 0
        if self.shrink_cooldown > 0:
            self.shrink_cooldown -= 1

        if self.sound_cooldown > 0:
            self.sound_cooldown -= 1

        # Update color factor
        self.color_factor += self.color_direction * 0.01
        if self.color_factor >= 1:
            self.color_factor = 1
            self.color_direction = -1
        elif self.color_factor <= 0:
            self.color_factor = 0
            self.color_direction = 1

    def draw(self):
        color = interpolate_color(START_COLOR, END_COLOR, self.color_factor)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius, 0)  # Filled circle with anti-aliasing

# Function to generate a random position for the ball
def generate_random_position():
    while True:
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        # Ensure the ball is not initialized too close to the circle boundary
        distance_to_center = math.sqrt((x - CIRCLE_CENTER[0])**2 + (y - CIRCLE_CENTER[1])**2)
        if distance_to_center <= CIRCLE_RADIUS - 40:  # Ensure the ball is not placed too close to the boundary
            return x, y

# Main loop
x, y = generate_random_position()
balls = [Ball(x, y, 5, 5)]  # Create a list of initial balls
circle_color_factor = 0
circle_color_direction = 1
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)  # Set background color to black

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw balls
    for ball in balls:
        ball.update()
        ball.draw()

    # Update circle color factor
    circle_color_factor += circle_color_direction * 0.01
    if circle_color_factor >= 1:
        circle_color_factor = 1
        circle_color_direction = -1
    elif circle_color_factor <= 0:
        circle_color_factor = 0
        circle_color_direction = 1

    circle_color = interpolate_color(START_COLOR, END_COLOR, circle_color_factor)
    pygame.draw.circle(screen, circle_color, CIRCLE_CENTER, CIRCLE_RADIUS, 2)  # Circle with anti-aliasing

    # If the circle radius is smaller than the minimum radius, exit the loop
    if CIRCLE_RADIUS <= MIN_RADIUS:
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
