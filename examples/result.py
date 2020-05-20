import sys
from pathlib import Path

sys.path.append('../opres')  # bad practice. forgive me

from opres import Result, Ok, Err


def load_message(message_file_path: Path) -> Result[str, Exception]:
    try:
        if not message_file_path.is_file():
            raise FileNotFoundError(f"{message_file_path} is not a valid file path")
        with message_file_path.open('r') as f:
            line = f.readline()
            return Ok(str(line))
    except Exception as e:
        return Err(e)


def run():
    message = load_message(Path(__file__).parent / 'dummy_file.txt')
    print(f"message.unwrap={message.unwrap()}")

    message = load_message(Path(__file__).parent / 'no_dummy_file.txt')
    if message.is_err():
        print("message is error")

    # sys.exit
    message.unwrap()


if __name__ == '__main__':
    run()
