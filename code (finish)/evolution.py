from settings import * 
from timer import Timer

class Evolution:
	def __init__(self, frames, start_monster, end_monster, font, end_evolution, star_frames):
		self.display_surface = pygame.display.get_surface()
		# Use scale instead of scale2x for compatibility
		start_size = frames[start_monster]['idle'][0].get_size()
		end_size = frames[end_monster]['idle'][0].get_size()
		self.start_monster_surf = pygame.transform.scale(frames[start_monster]['idle'][0], (start_size[0] * 2, start_size[1] * 2))
		self.end_monster_surf = pygame.transform.scale(frames[end_monster]['idle'][0], (end_size[0] * 2, end_size[1] * 2))
		self.timers = {
			'start': Timer(800, autostart = True),
			'end': Timer(1800, func = end_evolution)
		}

		# star animation
		# Use scale instead of scale2x for compatibility
		self.star_frames = []
		for frame in star_frames:
			size = frame.get_size()
			self.star_frames.append(pygame.transform.scale(frame, (size[0] * 2, size[1] * 2)))
		self.frame_index = 0

		# screen tint
		self.tint_surf = pygame.Surface(self.display_surface.get_size())
		self.tint_surf.set_alpha(200)

		# white tint 
		# Create white surface from mask for compatibility
		mask = pygame.mask.from_surface(self.start_monster_surf)
		self.start_monster_surf_white = pygame.Surface(self.start_monster_surf.get_size())
		self.start_monster_surf_white.fill((255, 255, 255))
		self.start_monster_surf_white.set_colorkey((0, 0, 0))
		self.start_monster_surf_white.set_colorkey('black')
		self.tint_amount, self.tint_speed = 0, 80
		self.start_monster_surf_white.set_alpha(self.tint_amount)

		# text 
		self.start_text_surf = font.render(f'{start_monster} is evolving', False, COLORS['black'])
		self.end_text_surf = font.render(f'{start_monster} evolved into {end_monster}', False, COLORS['black'])

	def display_stars(self, dt):
		self.frame_index += 20 * dt
		if self.frame_index < len(self.star_frames):
			frame = self.star_frames[int(self.frame_index)]
			rect = frame.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
			self.display_surface.blit(frame, rect)

	def update(self, dt):
		for timer in self.timers.values():
			timer.update()

		if not self.timers['start'].active:
			self.display_surface.blit(self.tint_surf, (0,0))
			if self.tint_amount < 255:
				rect = self.start_monster_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
				self.display_surface.blit(self.start_monster_surf, rect)

				self.tint_amount += self.tint_speed * dt
				self.start_monster_surf_white.set_alpha(self.tint_amount)
				self.display_surface.blit(self.start_monster_surf_white, rect)

				text_rect = self.start_text_surf.get_rect(midtop = rect.midbottom + vector(0,20))
				pygame.draw.rect(self.display_surface, COLORS['white'], text_rect.inflate(20,20), 0, 5)
				self.display_surface.blit(self.start_text_surf, text_rect)

			else:
				rect = self.end_monster_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
				self.display_surface.blit(self.end_monster_surf, rect)
				
				text_rect = self.end_text_surf.get_rect(midtop = rect.midbottom + vector(0,20))
				pygame.draw.rect(self.display_surface, COLORS['white'], text_rect.inflate(20,20), 0, 5)
				self.display_surface.blit(self.end_text_surf, text_rect)
				self.display_stars(dt)

				if not self.timers['end'].active:
					self.timers['end'].activate()