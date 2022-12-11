import logging

from bot import start_bot


def main():
    logging.basicConfig(level=logging.INFO)
    start_bot()


if __name__ == '__main__':
    main()