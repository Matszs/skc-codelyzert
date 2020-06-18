import os
import glob
from shutil import copyfile
import fileinput
import re
import subprocess

TMP_FILE = "check.py"

def validate_file(run_output, file_name):
	points = 0
	if re.search('Beste mats', run_output):
		points += 5
	if re.search('je leeftijd is', run_output):
		points += 5
	if re.search('3217', run_output):
		points += 5

	print(file_name + " heeft " + str(points) + " punten gehaald.")


def create_tmp_file(name):
	copyfile(name, "check.py")

	file_data = 'import sys\n'

	with open(TMP_FILE, 'r') as file:
		for line in file:
			if 'naam =' in line or 'naam=' in line:
				line = 'naam = sys.argv[1]\n'
			elif 'geboortejaar =' in line or 'geboortejaar=' in line:
				line = 'geboortejaar = int(sys.argv[2])\n'

			file_data = file_data + line

	with open(TMP_FILE, 'w') as file:
		file.write(file_data)



def run_file(args):
	proc = subprocess.Popen(["check.py"] + args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
	return proc.communicate()[0].decode("utf-8")


def check_file(name):
		create_tmp_file(name)
		run_output = run_file(["mats", "25"])
		validate_file(run_output, name)


def main():
	for file in glob.glob("code_files/*.py"):
		check_file(file)



if __name__ == '__main__':
	main()

