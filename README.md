# SQLAlchemy Repository

This project is a library that simplifies the use of SQLAlchemy in Python applications. It also provides a implementation of the repository pattern for SQLAlchemy.

It has a FastAPI integration through a middleware that manages the session and transaction for each request.

![PyPI](https://img.shields.io/pypi/v/sqlalchemy-repository.svg)
![Supported Python versions](https://img.shields.io/pypi/pyversions/sqlalchemy-repository.svg)

## Features

Here's what sqlalchemy-repository can do for you. 🚀

- **DatabaseManager**: It provides a class that manages the session and transaction for each request.
- **Repository pattern**: It provides a implementation of the repository pattern for SQLAlchemy.
- **FastAPI integration**: It provides a middleware that manages the session and transaction for each request in FastAPI.
- **Async support**: It provides a async version of the DatabaseManager, the Repository pattern and the FastAPI middleware.

## Installation

```console
$ pip install sqlalchemy-repository
---> 100%
Successfully installed sqlalchemy-repository
```

## License

This project is licensed under the terms of the [MIT license](https://github.com/javalce/sqlalchemy-repository/blob/main/LICENSE).
