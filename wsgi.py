from web import create_app


instance = create_app()


if __name__ == '__main__':
    instance.run()
