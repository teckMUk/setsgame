# Set Card Game

A Python implementation of the classic Set card game with MongoDB backend for card storage and management.

## About the Game

Set is a card game where players identify "sets" of three cards from a collection. Each card has four attributes:
- **Color**: Purple, Green, or Red
- **Shape**: Diamond, Squiggle, or Oval
- **Fill**: Outline, Filled, or Stripes
- **Number**: 1, 2, or 3 shapes

A valid "set" consists of three cards where each attribute is either all the same or all different across the three cards.

## Features

- MongoDB-backed card storage system
- Random card drawing (12 cards)
- Set validation logic
- Command-line interface
- 81 unique card images (SVG format)

## Prerequisites

- Python 3.x
- MongoDB (running locally on port 27017)
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd setgame
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. For development dependencies:
```bash
pip install -r requirements_dev.txt
```

4. Install the package:
```bash
pip install -e .
```

## Setup

### Option 1: Local Setup

1. Ensure MongoDB is running on `localhost:27017`

2. Initialize the card database by running the card split script:
```bash
python setscardsplit.py
```

This will populate the MongoDB database with all 81 cards and their attributes.

### Option 2: Docker Setup

1. Build and start the containers:
```bash
docker-compose up -d
```

2. Initialize the database:
```bash
docker-compose exec app python setscardsplit.py
```

3. Run the game:
```bash
docker-compose exec app python setsgame.py
```

To stop the containers:
```bash
docker-compose down
```

To stop and remove all data:
```bash
docker-compose down -v
```

## Usage

### Running the Game

Run the main game script:
```bash
python setsgame.py
```

The game will:
1. Draw 12 random cards from the deck
2. Display the cards with their IDs
3. Prompt you to enter three card IDs separated by spaces
4. Validate if the selected cards form a valid set

### Using the CLI

```bash
setgame -s setsgame -c <id1> <id2> <id3>
```

## Project Structure

```
.
├── setgame/              # Main package directory
│   ├── __init__.py
│   └── main.py          # CLI entry point
├── setsgame_cards_image/ # SVG card images (81 cards)
├── scripts/
│   └── formating.sh     # Code formatting script
├── setsgame.py          # Main game script
├── setscardsplit.py     # Database initialization script
├── requirements.txt     # Production dependencies
├── requirements_dev.txt # Development dependencies
└── setup.py            # Package setup configuration
```

## Database Schema

Cards are stored in MongoDB with the following structure:
```json
{
  "_id": 1,
  "color": "purple",
  "shape": "diamond",
  "fill_type": "filled",
  "Number of shapes": "1",
  "file_name": "diamond_purple_filled_1.svg",
  "bitlist": "0100"
}
```

## Development

### Code Formatting

Format code using Black:
```bash
black .
```

Or use the provided script:
```bash
bash scripts/formating.sh
```

## Dependencies

- **pymongo** (4.6.3): MongoDB driver for Python
- **black** (24.3.0): Code formatter (dev)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

[Add contribution guidelines here]
