from typing import Optional

from functions import filter_query


CMD_TO_FUNCTIONS = {
	'filter': filter_query,
}


def read_file(file_name: str):
	with open(file_name) as file:
		for line in file:
			yield line


def build_query(cmd: str, value: str, file_name: str, data: Optional[list]):
	if data is None:
		prepared_data = read_file(file_name)
	else:
		prepared_data = data

	return CMD_TO_FUNCTIONS[cmd](value, prepared_data)
