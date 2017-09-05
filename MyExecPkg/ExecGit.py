import subprocess
import sys
class ExecGit:
    def __init__(self):
        self.pipe = subprocess.PIPE

    def getUserValue(self, qnstr):
        answer = raw_input(qnstr)
        return answer

    def userConfirmation(self, qnstr, trueOpt, falseOpt):
        """
        Ask user to enter Y or N (case-insensitive).
        :return: True if the answer is Y.
        :rtype: bool
        """
        answer = ""
        trueOpt = trueOpt.lower()
        falseOpt = falseOpt.lower()
	#print(qnstr)
        while answer not in [trueOpt, falseOpt]:
            answer = raw_input(qnstr)
            answer = answer.lower()
            if( answer == trueOpt ):
                return True
            elif( answer == falseOpt ):
                return False

    def execCommand(self, command, handleError=True ):
        stderroutput = ""
        stdoutput = ""
        returncode = 0
        try:
            process = subprocess.Popen(command, stdout=self.pipe, stderr=self.pipe) 
            stdoutput, stderroutput = process.communicate()
            returncode = process.returncode

            if( process.returncode != 0 ):
                if( handleError == True ):
                    print("Error:" + str(returncode) )
                    print(stderroutput)
                    print(stdoutput)
                    print(returncode)
                    sys.exit(-1)
                return (-1, stderroutput, stdoutput)
            else:
                return (0, "", stdoutput)
        except:
            if( handleError == True ):
                print("Error:" + str(returncode) )
                print(stderroutput)
                print(stdoutput)
                sys.exit(-1)
            return (-1, stderroutput, "")
