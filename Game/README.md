# Game

### Running
```
pip install pygame
python Main.py
```
**IMPORTANT: Make sure you run it from within the `Game/` directory, importing `Core` modules will fail otherwise.**

### Game State
STATE (`dict`) in Main.py maintains the game state, and consists of:
- cell_width (`int`): Width of each cell in the maze.
- screen (`pygame.Surface`): Main game surface.
- maze (`Maze`): Currently loaded maze.
- walls (`list`): List of maze walls (for collision detection and stuff).
- enemies (`dict`): Collection of enemies with their name (`string`) as key and agent (`Agent`) as value.
- player (`Agent`): Current player agent.

### Assets:  
```
- Agent
- Wall
- Utils
```

## Agent
### Instantiation
```
Agent(screen, start_position, width, color, speed, player, state)
```
Parameters:
- screen (`pygame.Surface`): Surface on which this agent exists.
- start_position (`tuple`): Cartesian coordinates of the starting cell.
- width (`int`): Dimensions of the agent in pixels.
- color (`tuple`): Optional. Base color of each cell. Defaults to (255, 255, 0) [yellow].
- speed (`float`): Optional. Speed of the agent in cells per movement. Defaults to 1.
- player (`bool`): Optional. Whether or not the current agent is a player. Defaults to False.
- state (`string`): Optional. Initial state of the agent. Defaults to "ACTIVE".

### States
- ACTIVE: The agent is available and can perform actions when called.
- MOVING: The agent is in the process of moving to a position.
- INACTIVE: The agent is static at some position and can not perform any action.

### Other Attributes
- rect (`pygame.Rect`): Is used internally to modify the position of the agent and to detect collisions. `agent.rect.center` can be used to get the current cartesian coordinates of `agent` as a 2-tuple.

### Methods
```
activate()
```
Change state of the agent to "ACTIVE".

```
deactivate()
```
Change state of the agent to "INACTIVE".

```
walk(algorithm, STATE)
```
Make the agent 'walk' around the maze, determining its next step using the algorithm passed argument. Internally makes use of `move_up`, `move_down`, `move_right`, `move_left` and `move_to_coordinate` methods. The agent will change state to "MOVING" while in motion and back to "ACTIVE" when done moving.

Parameters:
- algorithm(agent, STATE) (`function`): A function that takes in an agent (`Agent`) and the current game state (`dict`) as input and outputs a single string (`"N" / "S" / "W" / "E"`) indicating the direction in which the agent should move next. 
- STATE (`dict`): The current game state.

```
draw()
```
Render agent on the screen.

## Utils
### Methods
```
position(coordinates, cell_width): 
```
Returns the indices of the grid in which the given coordinates fall.

Parameters:
- coordinates (`tuple`): x, y coordinates of the target.
- cell_width (`int`): Width of each cell in the maze.

```
coordinates(position, cell_width): 
```
Returns the coordinates of the center of the cell identified by the given position.

Parameters:
- position (`tuple`): i, j indices of the target cell.
- cell_width (`int`): Width of each cell in the maze.

## Wall
TODO
