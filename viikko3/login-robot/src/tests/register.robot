*** Settings ***
Resource  resource.robot
Test Setup  Input  new

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  a  kalle123
    Output Should Contain  Username a is too short

Register With Valid Username And Too Short Password
    Input Credentials  kalle  a
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kalleabc
    Output Should Contain  Password must not be only lowercase alphabetic letters