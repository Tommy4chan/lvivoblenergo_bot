import logging

from bot import start_bot
from bot import start_local_bot


def main():
    logging.basicConfig(level=logging.INFO)
    start_bot()
    #start_local_bot()


if __name__ == '__main__':
    main()