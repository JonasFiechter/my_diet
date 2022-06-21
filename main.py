from src.features.profile_generator.components.profile_generator import ProfileGenerator


def main():
    while True:
        profile = ProfileGenerator()
        profile.generator()
        print(profile.name)


if __name__ == '__main__':
    main()