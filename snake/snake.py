import pygame

class Snake:
	def __init__(self):

		self.head = [45,45]
		self.body = [[45, 45], [34, 45], [23, 45]]

	def move(self, control):
		#Движение змеи в зависимости от направления
		if control.flag_direction == "RIGHT":
			self.head[0] += 11
		elif control.flag_direction == "LEFT":
			self.head[0] -= 11
		elif control.flag_direction == "UP":
			self.head[1] -= 11
		elif control.flag_direction == "DOWN":
			self.head[1] += 11

	def animation(self):
		#Прибавляем в начало списка тела голову, а хвост удаляем
		self.body.insert(0, list(self.head))
		self.body.pop()

	def draw_snake(self, window):
		#Отрисовка змеи на экране
		for segment in self.body:
			pygame.draw.rect(window, pygame.Color("Green"), pygame.Rect(segment[0],
						 segment[1], 10, 10))
	def check_end_window(self):
		#Отслеживает достижение змеёй края экрана
		if self.head[0] == 419:
			self.head[0] == 23
		elif self.head[0] == 12:
			self.head[0] == 419
		elif self.head[1] == 23:
			self.head[1] == 419
		elif self.head[1] == 419:
			self.head[1] == 34

	def eat(self, food, gui):
		#Змея ест еду
		if self.head == food.food_position:
			self.body.append(food.food_position)
			food.get_food_position(gui)
			gui.get_new_indicator()

	def check_barrier(self, gui):
		#Проверяет не врезалась ли змея куда-то
		if self.head in gui.barrier:
			self.body.pop()
			gui.indicator.pop()
		if self.head in self.body[1:]:
			self.body.pop()
			gui.indicator.pop()
			

		