from typing import TYPE_CHECKING
from typing import List

from .base_installer import BaseInstaller


if TYPE_CHECKING:
    from poetry.core.packages import Package  # noqa


class NoopInstaller(BaseInstaller):
    def __init__(self):  # type: () -> None
        self._installs = []
        self._updates = []
        self._removals = []

    @property
    def installs(self):  # type: () -> List["Package"]
        return self._installs

    @property
    def updates(self):  # type: () -> List["Package"]
        return self._updates

    @property
    def removals(self):  # type: () -> List["Package"]
        return self._removals

    def install(self, package):  # type: ("Package") -> None
        self._installs.append(package)

    def update(self, source, target):  # type: ("Package", "Package") -> None
        self._updates.append((source, target))

    def remove(self, package):  # type: ("Package") -> None
        self._removals.append(package)
