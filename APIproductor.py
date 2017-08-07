#!coding=utf-8
import re
import os, sys


class APIproductor(object):
    def __init__(self):
        self.classList = []
        self.apiList = []

    def getClassInfo(self, filePath, ddStr):
        flag = 0
        commentFlag = 0
        tempFunc = ""
        tempS = ""
        tempClass = ""
        count = 0
        commentStrs = ""
        with open(filePath, 'r', encoding='utf-8') as f:
            commentStrs += ddStr + ".py" + '\n'
            commentStrs += "-------------------------------------------------------------------------------------------" + '\n'
            for s in f.readlines():
                reg = r'^class (.*)\(object\):$'
                result = re.findall(reg, s)
                if len(result) != 0:
                    tempClass = result[0]
                    self.classList.append(tempClass)
                regFunc = r'def (.*)\('
                resultFunc = re.findall(regFunc, s)
                if len(resultFunc) != 0:
                    tempFunc = resultFunc[0]
                    tempS = s
                if flag == 1:
                    regAuthor = r'@author:'
                    resultAuthor = re.findall(regAuthor, s)
                    if len(resultAuthor) > 0:
                        commentStrs += '\t' + tempClass + "." + tempFunc + '\n'
                        commentStrs += tempS
                        tempS = ""
                        tempFunc = ""
                        commentFlag = 1
                        flag = 0
                if commentFlag == 1:
                    regReturn = r'@return'
                    resultReturn = re.findall(regReturn, s)
                    commentStrs += s
                    if len(resultReturn) > 0:
                        commentFlag = 0
                        commentStrs += "-------------------------------------------------------------------------------------------" + '\n'
                        continue
                if s.__contains__("\'\'\'"):
                    flag = 1
        with open("API/" + ddStr + '.api', 'w', encoding="utf-8") as f:
            f.write(commentStrs)

    def getFile(self, rootPath):
        dirList = os.listdir(rootPath)
        if len(dirList) == 0:
            print("dir is Empty")
        else:
            for file_name in dirList:
                fileName = rootPath + os.sep + file_name
                if os.path.isfile(fileName):
                    if file_name.endswith(".py"):
                        filePathFull = fileName
                        fileName = fileName.split(".")[0]
                        subFileName = fileName.split("MESSAGE")[1][1:].split(os.sep, )
                        subFile = ".".join(subFileName)
                        self.getClassInfo(filePathFull, subFile)
                        # self.apiList.append(subFile)
                else:
                    customPath = rootPath + os.sep + file_name
                    self.getFile(customPath)
                    # print(self.apiList)


def getInstance():
    return APIproductor()


if __name__ == "__main__":
    rootPath = sys.path[0]
    os.makedirs(rootPath + os.sep + "API",exist_ok=True)
    APIinstance = getInstance()
    APIinstance.getFile(rootPath + os.sep + "bin")

    # getInstance().getClassInfo("API/test.py","")
