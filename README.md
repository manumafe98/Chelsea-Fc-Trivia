## Chelsea FC Trivia

This project consists of a GUI application that consumes from a random api endpoint generating a trivia game of 10 questions.

## API

The API is built using FastApi and Docker, offers the following endpoints:

- `GET /players`
- `GET /nationality`
- `GET /position`
- `GET /top_appearances`
- `GET /top_goalscorer`
- `GET /most_goals`
- `GET /most_appearances`

All the endpoints get three random records from the database and return a json with the following structure:
`players` -> list, `correct_answer` -> str/int, `attribute` -> str, `question` -> str.

The API utilizes a Mongodb database to store the scraped data, enabling efficient retrieval of information.


## GUI

The GUI consists on three windows:
- The `home` window, with a botton to check the rules and start playing
- The `trivia` window, that is the core of the game, showing the question to the player with the corresponding options.
- The `score` window, shows the final score of the player giving also the option to play again or stop playing.


## Installation and usage

First clone the repository, then if you don't have docker, install it for your proper os.

Then execute the following command on the path of the cloned repository

```commandline
docker compose up -d
```

After that you can check your `localhost:8000/` and verify the working endpoints.
Then execute the `chelsea_trivia.exe` and you can start playing!
