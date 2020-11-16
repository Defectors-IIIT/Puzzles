# Core
### Modules:  
```
- Node
- Maze
```

## Node
### Instantiation
```
Node(neighbors, color)
```
Parameters: 
- neighbors (`dict`): Optional. Edge weights for each of the node's neighbors in 4 directions. Keys: N, S, E, W. Defaults to INF.
- color (`list`): Optional. Background color of the node as a 3-tuple list containing three integers between 0-255 mapped to RGB values. Defaults to black.

## Maze
### Instantiation
``` 
Maze(num_rows, num_columns) 
```
Parameters: 
- num_rows (`int`): Optional. Number of rows, defaults to 1.
- num_columns (`int`): Optional. Number of columns, defaults to 1.


### Methods:
```
reset()
```
Reinitializes all the edge weights to infinity. 
   
**Parameters:**  
None.
```
benchmark()
```
Benchmarks the maze on basis of Deadends, Straightways, Turns, Junctions and Crossroads. 
   
**Parameters:**  
None.

```
add_path(start_position, direction, edge_value)
```
Adds a (weighted) path between two adjacent nodes.

**Parameters:**
- start_position (`tuple`): x, y coordinates of the starting node.
- direction (`string`): N / S / E / W.
- edge_value (`float`): Weight of the path to be added.

```
add_colors(start, color)
```
Colors the entire maze using BFS.

**Parameters:**
- start (`tuple`): Optional. x, y coordinates of the starting node. Defaults to (0, 0).
- color (`tuple`): Optional. Base color of each cell. Defaults to (255, 0, 0) [red]. 

```
draw(cell_width, padding)
```
Renders the maze and returns it as an image.

**Parameters:**
- cell_width (`int`): Optional. Dimensions of each cell (in pixels) of the maze to be drawn. Defaults to 50.
- padding (`int`): Optional. Outer padding (in pixels) of the maze boundary. Defaults to 10.

```
diff(maze, cell_width, padding)
```
Compares current maze with the input and renders the maze along with differences.

**Parameters:**
- maze (`Maze`): Object to compare the current maze with.
- cell_width (`int`): Optional. Dimensions of each cell (in pixels) of the maze to be drawn. Defaults to 50.
- padding (`int`): Optional. Outer padding (in pixels) of the maze boundary. Defaults to 10.

```
dump(filename)
```
Dumps the maze into a file as json.

**Parameters:**
- filename (`str`): File to write the maze into. Name it something like `<algorithm_name>_<dimensions>.maze` for consistency.

```
load(filename)
```
Loads a maze from a file.

**Parameters:**
- filename (`str`): File to read the maze from.

```
load_from_image(imgpath, resolution)
```
Generates a maze from an image. For best results, use a monochrome 1:1 image and pick a resolution that perfectly divides the image dimensions.

**Parameters:**
- imgpath (`str`): Relative path to the image.
- resolution (`int`): Dimensions of the generated maze. Higher implies more detail.
