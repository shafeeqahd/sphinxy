from __future__ import annotations

from sphinxy.riddle import Riddle


class IncorrectAnswer(Exception):
    ...


class Sphinx:
    def __init__(self, name: str) -> None:
        self._name = name
        self._riddle = Riddle(
            question=(
                "What goes on four legs in the morning, two legs at noon, "
                "and three legs in the evening?"
            ),
            answer="man",
        )

    def introduce(self) -> str:
        """
        This is a test script.

        Returns:None

        """
        return (
            f"Greetings, mortals. I am {self._name}. I have guarded the city of Thebes"
            "for centuries and posed riddles to those who dared to approach me."
        )

    def update_riddle(self, riddle: Riddle) -> str:
        """
        Testing if the updates are pulled.
        Args:
            riddle:

        Returns:

        """
        self._riddle = riddle
        return "I have updated my riddle. Are you ready to solve it?"

    def pose_riddle(self, include_hint: bool = False) -> tuple[str, str | None]:
        hint = (
            f"Hint: The answer starts with the letter '{self._riddle.get_hint()}'."
            if include_hint
            else None
        )
        return (self._riddle.question, hint)

    def check_riddle_answer(self, answer: str, return_hint: bool = False) -> str:
        if self._riddle.check_answer(answer):
            return "Your answer was correct. You may pass."
        elif return_hint:
            return (
                "Your answer was wrong. Hint: The answer starts with the letter "
                f"'{self._riddle.get_hint()}'."
            )
        else:
            raise IncorrectAnswer("Your answer was wrong. You shall not pass.")

class QaCheck(ABC):
    """
    Base class for checks to be run on guidance and survey data
    """

    def __init__(self, check_name: str):
        self.check_name = check_name

    @abstractmethod
    def run_check(self, data: Any, **kwargs) -> bool:
        """
        Perform the check on the data object and return True if the check passes, False otherwise.
        """
        raise NotImplementedError
