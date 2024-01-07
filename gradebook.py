class GradeBook:
    @classmethod
    def get(cls):
        course_name: str = input("Please enter the course name: ").strip()
        return cls(course_name)

    def __init__(self, course_name: str):
        self.course_name: str = course_name

    # method to get course name
    @property
    def course_name(self) -> str:
        return self._course_name

    # method to set course name
    @course_name.setter
    def course_name(self, course_name: str) -> None:
        self._course_name = course_name

    def welcome_message(self) -> str:
        return f"\nWelcome to the Grade Book for\n{self.course_name}"


