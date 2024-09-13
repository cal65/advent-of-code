from day2 import read_file
import numpy as np

class Boat_race():
	def __init__(self, time, record_distance):
		self.time = time
		self.record_distance = record_distance
	
	def race(self, hold_time):
		speed = hold_time
		distance = speed * (self.time - hold_time)
		return distance
	
	def iterate_races(self):
		distances = []
		for i in range(1, self.time):
			distances.append(self.race(i))
		winning_distances = [d for d in distances if d > self.record_distance]
		return len(winning_distances)



if __name__ == '__main__':
	d6 = read_file('day6.txt')
	times_raw = d6[0].split(' ')
	distances_raw = d6[1].split(' ')
	distances = [int(d) for d in distances_raw[1:] if d != '']
	times = [int(t) for t in times_raw[1:] if t != '']
	boats = []
	winnings_list = []
	for t, d in zip(times, distances):
		boat = Boat_race(t, d)
		boats.append(boat)
		winnings_list.append(boat.iterate_races())
	print(winnings_list)
	print(np.prod(winnings_list))
    
	test_boats = [Boat_race(7, 9), Boat_race(15, 40), Boat_race(30, 200)]
	test_wins = [b.iterate_races() for b in test_boats]
	print('test wins')
	print(test_wins)