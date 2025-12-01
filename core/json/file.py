""" Module that will simplify working with json files
"""

from typing import TypeVar, Type, Any, Union, Optional, overload
from dataclasses import is_dataclass, asdict
import json
import os

from dacite import from_dict
from .locals import Constants

T = TypeVar("T")


class SimpleJsonFile:
    """ Module designed for simplified work with json files.
    This is a base class and it does not contain functions for working with dataclasses
    """

    def __init__(self, path: str, json_format: int,
                 *, encoding: int = Constants.encoding.UTF8) -> None:
        self.path = path
        self.name = os.path.basename(self.path)
        self.file_format = json_format
        self.encoding = encoding

        self.is_exists = os.path.exists(self.path)
        self.is_empty = len(self.read()) if self.is_exists else True

        self.content = self.read() if self.is_exists else None

    def __call__(self) -> Union[dict, list]:
        return self.read()

    def __str__(self) -> str:
        return str(self.content)

    def get_content(self) -> Union[dict, list]:
        """ Gets the value loaded at creation
        Returns:
            Union[dict, list]: Data received from the file
        """

        return self.content

    def new(self, replace_file: bool = False,
            default_content: Optional[Any] = None) -> None:
        """ Creates a new json file
        Args:
            replace_file (bool, optional): Replaces the file with a new one by default. Defaults to False.
            default_content (Any | None, optional): Adds data to a new file. Defaults to None.
        """

        if not self.is_exists or replace_file:
            with open(self.path, "w+", encoding=self.encoding) as new_file:
                new_file.write("{}" if self.file_format == Constants.file_format.DICTIONARY else "[]")

            if default_content:
                if self.file_format == Constants.file_format.LIST:
                    self.write([default_content])

                elif self.file_format == Constants.file_format.DICTIONARY:
                    self.write(default_content)

            self.is_exists = os.path.exists(self.path)
            self.is_empty = len(self.read()) if self.is_exists else True

    def delete(self) -> None:
        """ Deletes the json file
        """

        os.remove(self.path)

    def read(self) -> Union[dict, list]:
        """ Reads json data from a file
        Returns:
            Union[dict, list]: Data received from the file
        """

        with open(self.path, "r", encoding=self.encoding) as read_file:
            read_data = json.load(read_file)
            self.content = read_data
            return read_data

    def write(self, data: Optional[Any] = None,
              indent: int = 4, ensure_ascii: bool = False) -> None:
        """ Writes json data to a file
        Args:
            data (Optional[Any], optional): File data. Defaults to None.
            indent (int, optional): Level indentation. Defaults to 4.
            ensure_ascii (bool, optional): Escaping non-ASCII characters. Defaults to False.
        """

        data = self.get_content() if data is None else data

        with open(self.path, "w+", encoding=self.encoding) as write_file:
            json.dump(data, write_file, indent=indent, ensure_ascii=ensure_ascii)

        self.content = self.read()

    def get_element_number(self, element: Any) -> int:
        """ Returns the number of elements in the JSON file with the specified element
        Args:
            element (Any): the value in the file
        Returns:
            int: the element to search for elements by
        """

        find_count = 0

        if self.file_format == Constants.file_format.LIST\
                and isinstance(self.content, list):

            for item in self.content:
                find_count += 1 if item == element else 0

            return -1 if find_count == 0 else find_count

        elif self.file_format == Constants.file_format.DICTIONARY\
                and isinstance(self.content, dict):

            for key in self.content:
                find_count += 1 if self.content.get(key) == element else 0

            return -1 if find_count == 0 else find_count

    @overload
    def add_element(self, element: Any, key_or_index: int) -> None: ...

    @overload
    def add_element(self, element: Any, key_or_index: str) -> None: ...

    def add_element(self, element: Any, key_or_index: Union[int, str]) -> None:
        """ Adds an element to json
        Args:
            element (Any): The value to be added
            key_or_index (Union[int, str]): The value to which the element will be assigned
        """

        if self.file_format == Constants.file_format.DICTIONARY\
                and isinstance(self.content, dict):
            self.get_content()[key_or_index] = element

        elif self.file_format == Constants.file_format.LIST\
                and isinstance(self.content, list):
            if key_or_index < 0:
                self.get_content().append(element)

            else:
                self.get_content()[key_or_index] = element


class JsonFile(SimpleJsonFile):
    """ A module designed for simplified work with json files
    """

    def __init__(self, path: str, json_format: int,
                 *, encoding: int = Constants.encoding.UTF8) -> None:
        super().__init__(path, json_format, encoding=encoding)

    def read_as_dataclass(self, dataclass: Type[T]) -> T | list[T]:
        """ Reads json data from a file as a dataclass

        Args:
            dataclass (Type[T]): The date class model that will be presented

        Returns:
            T | list[T]: Dataclass with json file data
        """

        data = self.read()

        if isinstance(data, list):
            return [from_dict(dataclass, item) for item in data]

        return from_dict(dataclass, data)

    def write(self, data: Optional[Any] = None, indent: int = 4,
              ensure_ascii: bool = False) -> None:
        """ Writes json data to a file Extended. Support dataclasses
        Args:
            data (Optional[Any], optional): File data. Defaults to None.
            indent (int, optional): Level indentation. Defaults to 4.
            ensure_ascii (bool, optional): Escaping non-ASCII characters. Defaults to False.
        """

        data = self.get_content() if data is None else data

        if isinstance(data, list):
            items = []
            for item in data:
                if is_dataclass(item):
                    item = asdict(item)

            data = items

        elif is_dataclass(data):
            data = asdict(data)

            with open(self.path, "w+", encoding=self.encoding) as file:
                json.dump(data, file, indent=indent, ensure_ascii=ensure_ascii)

            self.content = data
