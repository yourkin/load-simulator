# Load Simulator

## Overview

The Load Simulator is designed to simulate a variety of mathematical operations. It offers different levels of complexities and maintains an operation rate limiting feature. 

## Modules

### `constants.py`
Contains constants and enumerations.

### `models.py`
Defines data models for operation details, a list of operations, and simulator configuration.

### `operation_executor.py`
Contains the `OperationExecutor` class to execute mathematical operations.

### `utilities.py`
Utility functions and context managers for logging and other functionalities.

### `load_simulator.py`
Contains the `LoadSimulator` class and `run_simulator` function for simulating the load for mathematical operations.

## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourkin/load-simulator.git
    ```

2. **Navigate to the project directory**
    ```bash
    cd load_simulator
    ```

3. **Install dependencies using Poetry**
    ```bash
    poetry install
    ```

4. **Activate the virtual environment**
    ```bash
    poetry shell
    ```

## Usage

The `run_simulator` function can be imported to run the simulation:

```python
from load_simulator.load_simulator import run_simulator

run_simulator(
    seconds_to_run=10, 
    complexity="medium", 
    max_ops_per_sec=5
)
```

### Parameters for `run_simulator`

- `seconds_to_run`: Number of seconds to run the simulation.
- `complexity`: Complexity level for operations. Options are "easy", "medium", and "complicated".
- `max_ops_per_sec`: Maximum number of operations per second.

## Testing

Run the following command to execute the tests:

```bash
pytest
```

## Contributing

Fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## License

Distributed under the MIT License. See `LICENSE` for more information.