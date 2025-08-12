# OR_tools_exploration
Repository for playing with Google's OR Tools packages

[Package install guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

## Activating the environment  
Install packages after the environment is activated.  
```
source .venv/bin/activate  
which python  
.venv/bin/python
```
## Install OR Tools
`python -m pip install ortools`

[Get started with OR-Tools for Python](https://developers.google.com/optimization/introduction/python)


## Deactivating the environment  
`deactivate`  


## Learnings from examples
`traveling_salesman_example.py`: The general structure for a routing problem is laid out:
* create a data model - Here it is locations but in future examples it's the distance matrix.  Number of vehicles and the depot location are included. (Can there be more than 1 depot location?)
* create a routing index manager - This keeps track of the indices of the locations, the vehicles, and the depot.
* create a routing model - Simple, it creates a routing object, and the index manager is passed to it.
* create and register a transit callback - Create a function that recalls the distance between two nodes given the node indices, and then add it to the routing object.
* Define the cost of each arc using the transit callback. (Method of the routing object).
* Set the first solution heuristic - Set default search parameters and look for the cheapest arc.
* Solve the problem.
* Print the solution.

`vrp_example.py`
Similar to `traveling_salesman_example.py` but more than one vehicle defined in create_data_model and adds a Dimension associated with the max route length of one vehicle.  For 3 or more vehicles this seems non-optimal:  what is controlling the length of the cars that don't have the max length?

