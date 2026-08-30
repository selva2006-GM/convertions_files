import os
from tree.tree import find_path
from .baseconvertor import CONVERTERS

class FileConverter:

    def __init__(self, input_file, selected, category):
        self.input_file = input_file
        self.output_format = selected
        self.category = category

        self.current_file_type = (
            os.path.splitext(input_file)[1]
            .lower()
            .lstrip(".")
        )

        self.output_file_type = selected

        self.path = find_path(
            self.current_file_type,
            self.output_file_type
        )

    def convert(self):
        if self.path is None:
            raise ValueError(
                f"No path from {self.current_file_type} "
                f"to {self.output_file_type}"
            )

        print("CONVERT STARTED")
        print("PATH:", self.path)

        current_file = self.input_file

        for i in range(len(self.path) - 1):

            source = self.path[i]
            target = self.path[i + 1]

            print(f"STEP: {source} -> {target}")

            converter = CONVERTERS.get((source, target))

            if converter is None:
                raise ValueError(
                    f"Converter not implemented: {source} -> {target}"
                )

            print("FOUND CONVERTER:", converter)

            next_file = f"output.{target}"

            print(f"{current_file} -> {next_file}")

            converter(current_file, next_file)

            print("CONVERSION FINISHED")

            # VERY IMPORTANT
            current_file = next_file

        print("FINAL FILE:", current_file)

        return current_file