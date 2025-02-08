class Elment_Login():
    login_button_element = ("xpath", "//button[@id='login']")
    """登录按钮"""

    login_user_input = ("xpath", "//input[@name='account']")
    """账号输入框"""

    login_password_input = ("xpath", "//input[@name='password']")
    """密码输入框"""

    login_captcha_input = ("xpath", "//input[@name='code']")
    """验证码输入框"""

    login_succeed_assertion = ("xpath", "//div[(text()='登录成功')]")
    """登录成功"""

    account_password_error_assertion = ("xpath", "//div[(text()='账号密码错误')]")
    """账号密码错误"""

    login_captcha_error_assertion = ("xpath", "//div[(text()='验证码错误')]")
    """验证码错误"""