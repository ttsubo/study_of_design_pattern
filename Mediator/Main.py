import sys
from mediator.mediator import ConcreteMediator 
from mediator.colleague import ConcreteColleagueTextArea, ConcreteColleagueButton


def startMain(userid, password):
    m = ConcreteMediator()
    inputIdObj = ConcreteColleagueTextArea(m, "ID")
    inputPwObj = ConcreteColleagueTextArea(m, "PW")
    pushButtonObj = ConcreteColleagueButton(m, "Login")
    m.setColleagues(inputIdObj, inputPwObj, pushButtonObj)

    inputIdObj.inputText(userid)
    inputPwObj.inputText(password)
    if pushButtonObj.clickButton():
        print("Login Succeed!!")
    else:
        print("Login Failed!!")


def check_input_data(params):
    if len(params)==3:
        userid = params[1]
        password = params[2]
    elif len(params)==2:
        userid = params[1] 
        password = None
    elif len(params)==1:
        userid = None
        password = None
    return userid, password


if __name__ == "__main__":
    userid, password = check_input_data(sys.argv)
    startMain(userid, password)
