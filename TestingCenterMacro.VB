Private WithEvents mainInboxItems As Outlook.Items

Public Sub Application_Startup()

    Dim olApp As Outlook.Application
    Dim objNS As Outlook.NameSpace
    Set olApp = Outlook.Application
    Set objNS = olApp.GetNamespace("MAPI")
    Set mainInboxItems = objNS.GetDefaultFolder(olFolderInbox).Folders("MacroTest").Items
End Sub

Private Sub mainInboxItems_ItemAdd(ByVal item As Object)
    Dim message As Outlook.MailItem
    Dim reg As RegExp
    Dim MatchList As MatchCollection
    Dim StudentEmail As MatchCollection
    Dim StudentName As String
    Dim nameArray() As String
    Dim InstructorName As String
    Dim InstructorEmail As String
    Dim TestName As String
    Dim testStartTime As Date
    Dim testEndTime As Date
    Dim testStartDate As String
    Dim testEndDate As String
    Dim TestString As Object
    Dim timeStamp As String
    Dim timeAllowed As String
    Dim processedFolder As Folder
    
    timeStamp = "09:00:00"
    'Debug.Print "Found an Item! Subject: " + item.Subject
    Set reg = New RegExp
    Set message = item
    Set processedFolder = Outlook.Application.GetNamespace("MAPI").GetDefaultFolder(olFolderInbox).Folders("Processed")
    'Debug.Print message.Body
    With reg 'test name
        .Pattern = "(Course ID and Test Name \(e\.g\. EGR101 Midterm, Quiz 7, etc\):)+(\s*)([^\r\n]*\w+)+"
        .Global = False
    End With
    If reg.Test(message.Body) Then
        Set MatchList = reg.Execute(message.Body)
        Set M = MatchList(0)
        'Debug.Print M.SubMatches(2)
        TestName = M.SubMatches(2)
    End If
    With reg 'Instructor name
        .Pattern = "(?:Instructor Name and a CONTACT NUMBER \(for urgent questions\): \*\s*)(?:\w*\s*)(\w*)"
        .Global = False
    End With
    If reg.Test(message.Body) Then
        Set MatchList = reg.Execute(message.Body)
        Set M = MatchList(0)
        'Debug.Print M.SubMatches(0)
        InstructorName = M.SubMatches(0)
    End If
      With reg 'Instructor Email
        .Pattern = "(?:Instructor E-mail:\s*)((\w*[\s|\.|@])*)"
        .Global = False
    End With
    If reg.Test(message.Body) Then
        Set MatchList = reg.Execute(message.Body)
        Set M = MatchList(0)
        'Debug.Print M.SubMatches(0)
        InstructorEmail = M.SubMatches(0)
    End If
    With reg 'Start date
        .Pattern = "(?:Please specify the precise date which the test may be administered:\s*)(.+[^\n\r])"
        .Global = False
    End With
    If reg.Test(message.Body) Then
        Set MatchList = reg.Execute(message.Body)
        Set M = MatchList(0)
        'Debug.Print M.SubMatches(0)
        testStartDate = M.SubMatches(0)
    End If
    With reg 'End Date
        .Pattern = "(?:If test may be administered over a span of days, please specify the precise end date the test may be administered:\s*)(.+[^\n\r])"
        .Global = False
    End With
    If reg.Test(message.Body) Then
        Set MatchList = reg.Execute(message.Body)
        Set M = MatchList(0)
        'Debug.Print M.SubMatches(0)
        testEndDate = M.SubMatches(0)
    Else
        testEndDate = testStartDate
    End If
    With reg 'Student Email
        .Pattern = "(?:Student E\-mail:\s*)((\w*[\s|\.|@])*)"
        .Global = True
    End With
    If reg.Test(message.Body) Then
       Set StudentEmail = reg.Execute(message.Body)
    End If
    With reg 'Student Name name
        .Pattern = "(?:Enter EACH student's name\; First and Last, in a list here, and enter emails in the boxes below\:\s*)(.*[^\n\r])"
        .Global = False
    End With
    If reg.Test(message.Body) Then
        Set MatchList = reg.Execute(message.Body)
        Set M = MatchList(0)
        'Debug.Print M.SubMatches(0)
        StudentName = M.SubMatches(0)
        nameArray = Split(StudentName, ",")
    End If
     With reg 'Total time allowed
        .Pattern = "(?:What is the total amount of time the student\(s\) is allowed for this test\?\s*)(\d*)"
        .Global = False
    End With
    If reg.Test(message.Body) Then
        Set MatchList = reg.Execute(message.Body)
        Set M = MatchList(0)
        'Debug.Print M.SubMatches(0)
        totalTime = M.SubMatches(0)
    End If
    If (StrComp(testStartDate, testEndDate, vbTextCompare) = 0) Then
        With reg 'TimeStamp
            .Pattern = "(?:If test must be administered at an exact time please specify in 24 hr format:\s*)(.*[^\n\r])"
            .Global = False
        End With
        If reg.Test(message.Body) Then
            Set MatchList = reg.Execute(message.Body)
            Set M = MatchList(0)
            'Debug.Print M.SubMatches(0)
            timeStamp = CDate(M.SubMatches(0))
            testStartTime = CDate(testStartDate + " " + timeStamp)
            testEndTime = DateAdd("m", (CDbl(totalTime) / 1440), testStartTime)
        End If
    Else
        testStartTime = CDate(testStartDate) + (9 / 24)
        testEndTime = CDate(testEndDate) + (16 / 24)
    End If
    

    Debug.Print "Student Name: " & StudentName
    Debug.Print "Instructor Name: " & InstructorName
    For I = 0 To StudentEmail.Count - 1
        Debug.Print I & ": "; (StudentEmail(I).SubMatches(0))
    Next I
    Debug.Print "Instructor Email: " & InstructorEmail
    Debug.Print "Test Name: " & TestName
    Debug.Print "Test Start Time: " & testStartTime
    Debug.Print "Test End Time: " & testEndTime
    
    Dim appointment As Object
    For I = 0 To StudentEmail.Count - 1
        Set appointment = CreateItem(olAppointmentItem)
        appointment.MeetingStatus = olMeeting
        appointment.Subject = TestName
        appointment.Location = "Hazy Library Rm 232"
        appointment.Start = testStartTime
        appointment.End = testEndTime
        appointment.Recipients.Add (StudentEmail(I))
        appointment.Recipients.Add (InstructorEmail)
        appointment.Body = "Hello " + nameArray(I) + "," + vbNewLine + vbNewLine + "Please accept this calendar invite to scedchule your " + TestName + " from " + testStartDate + " to " + testEndDate + " with a time between 0900 and 1600 as arranged by Professor " + InstructorName + ". You will have " + totalTime + " minutes for you to take your exam." + vbNewLine + "Please ensure your calendar is set to Arizona time and you bring your student ID." + vbNewLine + vbNewLine + "Regards," + vbNewLine + "Testing Center"
        appointment.Display
    Next I
    item.Move processedFolder
End Sub
