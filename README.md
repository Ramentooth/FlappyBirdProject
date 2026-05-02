# FlappyBirdProject
## Flappy Bird UML
![FlappyUML](https://github.com/Ramentooth/FlappyBirdProject/blob/main/images/FlappyBirdUML_1.drawio.png?raw=true)
## Flappy Bird interface
![FlappyGameplay](https://github.com/Ramentooth/FlappyBirdProject/blob/main/images/Flappybird.png?raw=true)
## Details
### Description

The game functions like regular Flappy Bird with the user having to jump through gaps in pipes. As the user progresses through each pair of pipes the score increases by one and the game continues infinitely until the user loses, where they are prompted with a game over screen where the high score is saved and the user can play again.

---

### Target User

For recreational gamers with extra time on their hands, since the controls are pretty self-explanatory.

**Controls:**
| Input | Action |
|-------|--------|
| `SPACE` | Flap / Jump |
| Mouse Click | Button interaction |

---

### Planned Features

- Different types of birds with different speeds and flap length
- Pipes with two entry points, with one scoring the player more points if they can make it in
- Changing backgrounds as the user progresses

---

### Program Structure

| File | Role |
|------|------|
| `FlappyBird.py` | Main file — game loop, event handling, collision detection, scoring |
| `Bird.py` | Bird class — position, gravity, boost mechanics |
| `Pipe.py` | Pipe class — procedural generation, movement, scoring zones |
| `Background.py` | Background class — scrolling parallax background |
| `Button.py` | Button class — interactive UI buttons (Start, Play Again, Quit) |
| `Settings.py` | Global constants — screen size, speed, colors, fonts |

---

### Assets

| File | Usage |
|------|-------|
| `fieldBG.jpeg` | Scrolling gameplay background |
| `FlappyGameOver.jpeg` | Game over screen overlay |

---

### Challenges

The most challenging part of this project has definitely been getting the game to loop properly after the end screen is done.

---

### How to Run

```bash
pip install pygame
python FlappyBird.py
```

> Requires Python 3.x and Pygame.
### Credits

* SFX: https://pixabay.com/sound-effects/search/flap/
* Bird picture: my mom
* background: https://mungfali.com/post/D95842A662F978B00FC85138C37F7EC0C914D06E/A10FE8976CEDA675DC0F6BAC06A4B9990E9C8DC8?utm_source=Pinterest&utm_medium=organic
