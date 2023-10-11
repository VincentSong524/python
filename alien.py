import my_tools

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x_postition'] = 0
alien_0['y_postition'] = 25

my_tools.line()

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = '5'

print(alien_0)

my_tools.line()

print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

my_tools.line()

alien_0 = {'x_position': 0, 'y_position': '25', 'speed': 'medium'}
print(f"Original x_position: {alien_0['x_position']}.")

#向右移动外星人
#根据当前速度确定将外星人向右移动多远。
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#新位置为旧位置加上移动距离
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New x_position: {alien_0['x_position']}.")

my_tools.line()

del alien_0['speed']
print(alien_0)