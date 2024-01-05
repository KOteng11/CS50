from gradebook import GradeBook


def main():
    course_name = GradeBook.get()

    print(course_name.welcome_message())


if __name__ == "__main__":
    main()
