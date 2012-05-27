"""
In the classic problem of the Towers of Hanoi, you have 3 rods and N disks of different sizes which can slide on to any tower.
The puzzle starts with disks sorted in ascending order of size from top to bottom (e g , each disk sits on top of an even larger one) You have the following constraints:
* (A) Only one disk can be moved at a time
* (B) A disk is slid off the top of one rod onto the next rod
* (C) A disk can only be placed on top of a larger disk
Write a program to move the disks from the first rod to the last using Stacks.
"""


class Tower(object):
	def __init__(self, tower_index):
		self.disks = [] 
		self.tower_index = tower_index

	def add(self, disk):
		if self.disks and self.disks[-1] <= disk:
			raise ValueError('Disk {} cannot be placed on top of disk {}'.format(disk, self.disks[-1]))
		self.disks.append(disk)
		#print 'Disk: {}  ===> Tower: {}'.format(disk, self.tower_index)

	def move_top(self, to_tower):
		if not self.disks:
			raise Exception('No disks in this tower: {}'.format(self.tower_index))
		top_disk = self.disks.pop()
		to_tower.add(top_disk)
		print 'Disk: {}  Tower: {}  ===> Tower: {}'.format(top_disk, self.tower_index, to_tower.tower_index)

	def move_all(self, to_tower, buffer_tower, remaining):
		if remaining <= 0:
			return
		self.move_all(buffer_tower, to_tower, remaining - 1)
		self.move_top(to_tower)
		buffer_tower.move_all(to_tower, self, remaining - 1)

def stage(num_towers=3, num_disks=4):
	towers = []
	for x in xrange(num_towers):
		towers.append(Tower(x))
	for x in xrange(num_disks-1, -1, -1):
		towers[0].add(x)
	return towers

def print_towers(towers):
	for t in towers:
		print 'Tower: {}  :  {}'.format(t.tower_index, ','.join([str(x) for x in t.disks]))
	print '________________'

def _test_all():
	towers = stage()
	print_towers(towers)
	total_disks = len(towers[0].disks)
	towers[0].move_all(towers[-1], towers[1], total_disks)
	print_towers(towers)
	assert len(towers[-1].disks) == total_disks
	for t in towers[0:-1]:
		assert not t.disks

if __name__ == '__main__':
	_test_all()
	

