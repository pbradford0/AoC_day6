#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/6

import sys

def lights_toggle(low_left, top_right, *light_grid):
  #no output, just change a grid (dict) and set a range to flip in each cell
  #split the coordinate instructions into ints
  snip_bottom = low_left.split(",")
  snip_top = top_right.split(",")
  grid_x = int(snip_bottom[0])
  grid_y = int(snip_bottom[1])
  while grid_x <= int(snip_top[0]):
    while grid_y <= int(snip_top[1]):
      if light_grid[grid_x][grid_y] == 1:
        light_grid[grid_x][grid_y] = 0
      else:
       light_grid[grid_x][grid_y] = 1
      grid_y = grid_y + 1
    grid_y = int(snip_bottom[1])
    grid_x = grid_x + 1
  return light_grid

def lights_off(low_left, top_right, *light_grid):
  #no output, just change a grid (dict) and set a range = 0 in each cell
  #split the coordinate instructions into ints
  snip_bottom = low_left.split(",")
  snip_top = top_right.split(",")
  grid_x = int(snip_bottom[0])
  grid_y = int(snip_bottom[1])
  while grid_x <= int(snip_top[0]):
    while grid_y <= int(snip_top[1]):
      light_grid[grid_x][grid_y] = 0
      grid_y = grid_y + 1
    grid_y = int(snip_bottom[1])
    grid_x = grid_x + 1
  return light_grid

def lights_on(low_left, top_right, *light_grid):
  #no output, just change a grid (dict) and set a range = 1 in each cell
  #split the coordinate instructions into ints
  snip_bottom = low_left.split(",")
  snip_top = top_right.split(",")
  grid_x = int(snip_bottom[0])
  grid_y = int(snip_bottom[1])
  while grid_x <= int(snip_top[0]):
    while grid_y <= int(snip_top[1]):
      light_grid[grid_x][grid_y] = 1
      grid_y = grid_y + 1
    grid_y = int(snip_bottom[1])
    grid_x = grid_x + 1
  return light_grid

def count_lights(grid):
  #output: number of lights currently lit
  lit = 0
  #loop through the grid
  grid_x = 0
  grid_y = 0
  while grid_x <= 999:
    while grid_y <= 999:
      if grid[grid_x][grid_y] == 1:
        lit = lit + 1
      grid_y = grid_y + 1
    grid_y = 0
    grid_x = grid_x + 1
  return lit

def defeat_neighbor(filename):
  input = open(filename, 'rU')
  #output: number of lights currently lit
  lit = 0
  #fill the grid with one million lights
  light_grid = []
  grid_x = 0
  grid_y = 0
  while grid_x <= 999:
    light_grid.append([])
    while grid_y <= 999:
      light_grid[grid_x].append(0)
      grid_y = grid_y + 1
    grid_y = 0
    grid_x = grid_x + 1
  #loop thru input, run each command
  for command in input:
     #separate the command into words, then use the first 2 to determine action
    snip = command.split()
    if snip[0] == "toggle":
      light_grid = lights_toggle(snip[1], snip[3], *light_grid)
    elif snip[0] == "turn":
      if snip[1] == "on":
        light_grid = lights_on(snip[2], snip[4], *light_grid)
      elif snip[1] == "off":
        light_grid = lights_off(snip[2], snip[4], *light_grid)
      else:
        print "Error: Invalid instructions!"
    else:
      print "Error: Invalid instructions!"
  #now check how many lights are lit
  lit = count_lights(light_grid)
  return lit

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  lit = defeat_neighbor(sys.argv[1])
  print str(lit) + " lights are actively ensuring the domination of thine neighbors."

if __name__ == '__main__':
  main()