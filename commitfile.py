from datetime import date
import subprocess
subprocess.run(['git', 'add','.'])
subprocess.run(['git', 'commit', '-m', 'create file for !'+str(  date.today())])
subprocess.run(['git', 'push', 'origin/master'])