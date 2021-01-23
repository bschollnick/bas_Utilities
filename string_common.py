

def extractString(textData, startText=None, endText=None, startPos=0, forceCase=False):
#    stringStart = -1
#    stringEnd = -1
    output = None
    if forceCase:
        startText = startText.upper()
        endText = endText.upper()
        textData = textData.upper()
    stringStart = textData.find(startText, startPos)
#    print(stringStart)
    if stringStart != -1:
        stringEnd = textData.find(endText, stringStart+len(startText))
 #       print(stringEnd)
        if stringEnd != -1:
            output = textData[stringStart+len(startText):stringEnd]
    return output

def insertString(original, insertFrag, searchText):
    stringStart = original.upper().find(searchText.upper())
    return (original[:stringStart] + insertFrag + original[stringStart:])

