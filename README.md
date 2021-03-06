[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!--
  <a href="https://github.com/seppedelanghe/E-Builder">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
  -->

  <h3 align="center">E-Builder</h3>

  <p align="center">
    Python based physics environment builder. Mainly build to create custom environments to train reinforcement learning models.
    <br />
    <br />
    <a href="#usage">View Example</a>
    ·
    <a href="https://github.com/seppedelanghe/E-Builder/issues">Report Bug</a>
    ·
    <a href="https://github.com/seppedelanghe/E-Builder/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#examples">Examples</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Python based physics environment builder to be used to train AI Models.
You could for example recreate a game you want to train an AI model for so you can easily make actions via code and read out a score/reward.

### Built With

* Python 3.8
* PyGame


### Features

Currently the project allows you to modify the following things:

- Environment
  - screen size
  - fixed FPS
  - Enable FPS Counter
  - Background color

- Supported objects
  - Circle
  - Rectangle
  - Triangle
  
- Non physics objects:
  - Line

- Objects options
  - position
  - size
  - color
  - gravity
  - bounce
  - velocity (speed and direction)
  - friction (fixed rate)
  - gravitate to other object (based on mass)

- Other
  - spring functionality
  - bounce of edges (with loss of momentum/velocity)


### Examples

This is a list of the current examples that showcase what e-builder can do.

- __Bounce:__ 
  - Bounce some balls (circles) around of the walls.
  - Apply gravity to objects
- __Edge:__ 
  - Respawning an object on other side for continues loop of moving objects
- __Flappy:__
  - Bad clone of flappy bird
  - Shows how the `events` and `updates` callbacks can be used
- __Planest:__
  - A planet gravitating to the sun
  - Shows gravitateTo and velocity
- __Removal:__
  - Example on how you can remove entities from the environment after the have left the screen
- __Reuse:__
  - Similar to Removal, instead objects are reused and respawned at original location
- __Simple:__
  - Bare bone starting template with 1 object moving up
  - This is the template for the Usage part in the README
- __Spaceship:__
  - Spaceship that can apply thrust and move forward
  - Show how friction slowly slows down the object
  - Shows how arrow keys can be used to control an objects movement
- __Springs:__
  - 3 circles being held under tension to create a shape
  - Example of how to use the springs funciontion


<br>

<!-- GETTING STARTED -->
## Getting Started

__To use follow these steps.__

### Installation


1. Clone the repo to folder ebuilder
   ```sh
   git clone https://github.com/seppedelanghe/E-Builder.git ebuilder
   ```

2. (Optional) Create and activate a new conda env
    ```sh
    conda create -n ebuilder python=3.8
    conda activate ebuilder
    ```

3. Install pip packages
   ```sh
   pip install -r requirements.txt
   ```



<!-- USAGE EXAMPLES -->
## Usage

### Creating an environment

<br>

_Simple environment with 1 circle_

```python
from ebuilder.models.environment import Env
from ebuilder.models.objects import Circle

import pygame, math

WIDTH = 640
HEIGHT = 480

# Handle PyGame events here
'''
For example:
- Clicks
- Mouse events
- Quit action
- etc.

Events get triggered every frame, before updates.
'''
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            env.running = False 

# Handle entity updates here
'''
For example:
- Position
- Velocity
- Color
- etc.

Updates get triggered every frame, before drawing.
'''
def updates(entities: dict):
    pass # no action needed for this example

# Create an env that will create a window of 640px by 480px that runs at 30 FPS
env = Env(
    updates,
    events,
    size=(WIDTH, HEIGHT),
    fps=30)

# Create a ball (2D Circle) with fixed properties
ball = Circle(
        WIDTH / 2, # Middle of the screen
        HEIGHT, # Bottom of the screen
        radius=4, # Radius of 4 px
        speed=10,
        direction=-math.pi / 2, # Move up
        mass=0, # Mass of 0
        gravity=0, # no gravity
        bounce=-0, # no elasticity
        friction=0, # no friction => slowing down in air
        color=(0, 0, 0) # RBG Color black
    )

env.addEntity(ball, 'ball') # Adding the ball to the env

env.start() # Starting the env
```

<br>

__More examples can be found in the `examples` folder or you can run them using the `main.py` file__

<br>


<!-- ROADMAP -->
## Roadmap

Take a look at the project board [Version 1](https://github.com/seppedelanghe/E-Builder/projects/1) to see what features the project will have in the near future. \
Or see the [open issues](https://github.com/seppedelanghe/E-Builder/issues) for a list of all things in progress (bug fixes, features and more).



<br>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the GNU AFFERO GENERAL PUBLIC LICENSE License. See `LICENSE` for more information.

<br>

<!-- CONTACT -->
## Contact

Seppe De Langhe - Twitter: [@notSeppe](https://twitter.com/@notSeppe)

Project Link: [https://github.com/seppedelanghe/E-Builder](https://github.com/seppedelanghe/E-Builder)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/seppedelanghe/e-builder?style=for-the-badge
[contributors-url]: https://github.com/seppedelanghe/E-Builder/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/seppedelanghe/e-builder?style=for-the-badge
[forks-url]: https://github.com/seppedelanghe/E-Builder/network/members
[stars-shield]: https://img.shields.io/github/stars/seppedelanghe/e-builder?style=for-the-badge
[stars-url]: https://github.com/seppedelanghe/E-Builder/stargazers
[issues-shield]: https://img.shields.io/github/issues/seppedelanghe/e-builder?style=for-the-badge
[issues-url]: https://github.com/seppedelanghe/E-Builder/issues
[license-shield]: https://img.shields.io/github/license/seppedelanghe/e-builder?style=for-the-badge
[license-url]: https://github.com/seppedelanghe/E-Builder/blob/master/LICENSE
