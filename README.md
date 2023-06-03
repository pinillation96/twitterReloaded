# Twitter Reloaded

A simple Python application to simulate a Twitter-like platform, demonstrating SOLID principles and design patterns.

## Requirements

- Python 3.8 or higher
- Docker (optional)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/twitter-reloaded.git
cd twitter-reloaded
```
2. Install the dependencies:

```bash
pip install -r requirements.txt
```
## Running the application

1. To run the application locally, use:

```bash
python main.py
```

2. To run the application using Docker:

- Build the Docker image:

```bash
docker build -t twitter-reloaded .
```

- Run the Docker container:

```bash
docker run -p 4000:80 twitter-reloaded
```

## SOLID Principles

1. **Single Responsibility Principle (SRP)**: Each class in the `model` and `service` directories has a single responsibility. For instance, the `Tweet` class is only responsible for storing the details of a tweet. The `TweetFactory` class is responsible for creating tweets and replies. The `EventLogger` is only responsible for logging events.

2. **Open-Closed Principle (OCP)**: The application is open for extension but closed for modification. This is exemplified in the `Tweet` class hierarchy, where adding a new type of tweet does not require modifying the existing `Tweet` or `Reply` classes. New types of tweets can be added as new subclasses of `Tweet`.

3. **Liskov Substitution Principle (LSP)**: The `Tweet` class hierarchy also demonstrates this principle. Any instance of the `Tweet` class can be replaced with an instance of a `Reply` (a subclass of `Tweet`) without affecting the correctness of the program.

4. **Interface Segregation Principle (ISP)**: The interfaces (Python classes in this case) are client-specific, meaning they only contain the functionality required by the client classes. For example, the `Event` class contains only the functionality required by the `EventLogger`.

5. **Dependency Inversion Principle (DIP)**: The high-level `TwitterReloaded` class does not depend directly on the low-level `TweetFactory` or `EventLogger` classes. Instead, it depends on abstractions. This is achieved by passing the `TweetFactory` and `EventLogger` objects as arguments to the `TwitterReloaded` constructor, allowing you to change the implementations of these objects without having to change the `TwitterReloaded` class.

## Design Patterns

1. **Factory Method**: The `TweetFactory` class is used as a factory to create instances of `Tweet` or `Reply`, depending on the provided parameters. This allows the client code to remain decoupled from the actual classes (`Tweet` and `Reply`). This pattern is used in the `create_tweet` and `reply_to_tweet` methods of the `TwitterReloaded` class, which call the `create_tweet` and `create_reply` methods of the `TweetFactory`.

2. **Observer Pattern**: The `EventLogger` class acts as an observer, logging events whenever certain actions occur in the `TwitterReloaded` class. In particular, it logs events when a tweet is created, a reply is posted, or the application is opened. This allows the logging functionality to be added without modifying the code that triggers these actions. This pattern is implemented in the `log_event` method of the `EventLogger`, which is called from the `create_tweet`, `reply_to_tweet`, and `__init__` methods of the `TwitterReloaded` class.

3. **Decorator Pattern**: The `Reply` class acts as a decorator for the `Tweet` class. A `Reply` object wraps a `Tweet` object, and adds new behavior (the ability to reply to the tweet). This allows you to add replies to a tweet without modifying the `Tweet` class or affecting other parts of your program that use the `Tweet` class. This pattern is used in the `reply_to_tweet` method of the `TwitterReloaded` class, which creates a `Reply` object that wraps the original `Tweet`.

