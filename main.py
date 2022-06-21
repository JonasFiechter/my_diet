from src.features.profile_generator.components.profile_generator import profile_generator


def main():
    while True:
        profile = profile_generator()
        print(profile.sex)
        input('press any key')


if __name__ == '__main__':
    main()