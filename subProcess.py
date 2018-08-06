import os
from subprocess import Popen, PIPE, call

def runSQL(sql, tag):
	print("start calling"+tag)
	proc = subprocess.Popen(["sql-shell","-q"],stdout=PIPE, stderr=PIPE)
	call_stdout, call_stderr = proc.communicate()

	if proc.returncode != 0:
		print(call_stdout)
		print(call_stderr)
		print(tag+" failure")
	else:
		print(call_stdout)
		print(tag+" success")

