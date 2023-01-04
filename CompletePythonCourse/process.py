def run():
    print('Process running...')
    print(__name__)


def shut_down():
    print('Process stopping...')


def pause():
    print('Process pausing...')


if __name__ == '__main__':
    run()
    pause()
    run()
    shut_down()
