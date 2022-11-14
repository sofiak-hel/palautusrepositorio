*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  somenew
    Set Password  somepass123
    Set Confirmation  somepass123
    Submit Registeration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  somepass123
    Set Confirmation  somepass123
    Submit Registeration
    Register Should Fail With Message  Username a is too short

Register With Valid Username And Too Short Password
    Set Username  somenew
    Set Password  b
    Set Confirmation  b
    Submit Registeration
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  somenew
    Set Password  somepass1
    Set Confirmation  somepass2
    Submit Registeration
    Register Should Fail With Message  Password and password confirmation must equal


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Registeration
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation
    [Arguments]  ${confirmation}
    Input Password  password_confirmation  ${confirmation}