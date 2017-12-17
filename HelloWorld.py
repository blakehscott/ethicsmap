"""
The purpose of this document is to

Atom Pair Key:
d41a439c438a100756f5-4bf35003e819bb138249-epeOaSomx2a



"""



class AnswerClass:
    "A question's answer."



class QuestionClass:
    "A question, and will also have linked answers to choose from."

    type = "multiple-choice" # class variable shared by all instances

    def __init__(self, question=False):
        self.q = question # instance variable unique to each instance
        self.a = [] # instance variable unique to each instance

    def is_valid(self):
        if not self.q or self.q in ("no", "No", "N", "", "0", 0): # obviously, do something else as needed
            # empty string should return False
            # zero integer should return false
            return False
        return True #note: do not default to True on validation checks!!!





class RunTakeQuestions:
    "Runtime loop, take questions (and answers)."

    def __init__(self):
        print "log: set self.keep_asking = True"
        self.keep_asking = True # instance variable unique to each instanc

    # take an answer

    def take_a_question(self):
        q = raw_input("Please input a question:")
        questionObj = QuestionClass(q)
        if questionObj.is_valid():
            print "Success, we received your question!"
            print "-----------"
            print questionObj.q
            print "-----------"
            print "Now, let's have some answers!"
            # take an answer

        else:
            print "Sorry, that question was not valid. Terminating process."
            self.keep_asking = False



    def run_fox_run(self):
        while self.keep_asking:
            # start control flow tree with "would you like to enter another question"
            # user_response = raw_input("Would you like to enter another question? (y/n)")
            # if user_response in ("y","yes","Y","Yes"):
            self.take_a_question()
        else:
            print "Alright, we're done. OK?"
            user_response = raw_input("y/n")




if __name__ == "__main__":
    lazyFox = RunTakeQuestions()
    lazyFox.run_fox_run()
