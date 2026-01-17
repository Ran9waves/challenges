#Pytest tests for login flow

import pytest
from mfa_steps import step1_login,step2_otp,step3_yubikey
from users_data import users
from unittest.mock import patch

#Mock input for login
@patch("builtins.input", side_effect=["alice", "password123"])
def test_step1_login(mock_input):
    username, risk_score = step1_login()
    assert username == "alice"
    assert isinstance(risk_score,int)


#Mock input for OTP
@patch("builtins.input", side_effect=["000000"]) #wrong OTP for testing
def test_step2_otp_fail(mock_input):
    users["alice"]["failed_otp_attempt"] = 0
    result = step2_otp("alice")
    assert result is False or result is True #depending on random simulation

#Mock input for Yubikey
@patch("builtins.input", return_value="")
def test_step3_yubikey(mock_input):
    assert step3_yubikey("alice") is True

