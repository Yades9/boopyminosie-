from . generate import *

class Account:
    """
    Account class for handling account related requests.
    """
    def __init__(self, session: Session, debug: Optional[bool] = False):
        self.session = session
        self.debug = debug

    def register(self, email: str, password: str, username: str, verificationCode: str):
        """
        `**register**` - Registers a new account.
        
        `**Example**`
        ```py
        from pymino import *

        bot = Bot()
        bot.request_security_validation(email=email)
        code = input("Enter the code you received: ")
        response = bot.register(email=email, password=password, username=username, verificationCode=code)
        print(response.json)
        ```
        """
        return Authenticate(self.session.handler(
            method = "POST", url="/g/s/auth/register",
            data={
                "secret": f"0 {password}",
                "deviceID": device_id(),
                "email": email,
                "clientType": 100,
                "nickname": username,
                "validationContext": {
                    "data": {
                        "code": verificationCode
                    },
                    "type": 1,
                    "identity": email
                },
                "type": 1,
                "identity": email,
                "timestamp": int(time() * 1000)
            }))

    def delete_request(self, email: str, password: str):
        """
        `**delete_request**` - Sends a delete request to the account.
        
        `**Example**`
        ```py
        from pymino import *
        
        bot = Bot()
        bot.run(email=email, password=password)
        response = bot.delete_request(email=email, password=password)
        print(response)
        ```"""
        return SResponse(self.session.handler(
            method = "POST", url="/g/s/account/delete-request",
        data={
            "secret": f"0 {password}",
            "deviceID": device_id(),
            "email": email,
            "timestamp": int(time() * 1000)
        })).json

    def delete_request_cancel(self, email: str, password: str):
        """
        `**delete_request_cancel**` - Cancels the delete request.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        bot.run(email=email, password=password)
        response = bot.delete_request_cancel(email=email, password=password)
        print(response)
        ```
        """
        return SResponse(self.session.handler(
            method = "POST", url="/g/s/account/delete-request/cancel",
        data={
            "secret": f"0 {password}",
            "deviceID": device_id(),
            "email": email,
            "timestamp": int(time() * 1000)
        })).json

    def check_device(self, deviceId: str):
        """
        `**check_device**` - Checks if the device is valid.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        response = bot.check_device(deviceId=device_id())
        print(response)
        ```
        """
        return SResponse(self.session.handler(
            method = "POST", url="/g/s/device/check",
        data={
            "deviceID": deviceId,
            "clientType": 100,
            "timezone": -310,
            "systemPushEnabled": True,
            "timestamp": int(time() * 1000)
        })).json

    def fetch_account(self):
        """
        `**fetch_account**` - Fetches the account information.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        bot.run(email=email, password=password)
        response = bot.fetch_account()
        print(response)
        ```
        """
        return SResponse(self.session.handler(method = "GET", url="/g/s/account")).json

    def upload_image(self, image: str) -> SResponse:
        """
        `**upload_image**` - Uploads an image to the server.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        bot.run(email=email, password=password)
        response = bot.upload_image(image="image.jpg")
        print(response)
        ```
        """
        return SResponse(self.session.handler(method="POST", url=f"/g/s/media/upload",
            data=open(image, "rb").read(), content_type="image/jpg")).mediaValue

    def fetch_profile(self):
        """
        `**fetch_profile**` - Fetches the profile information.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        bot.run(email=email, password=password)
        response = bot.fetch_profile()
        print(response)
        ```
        """
        return SResponse(self.session.handler(
            method = "GET", url = f"/g/s/user-profile/{self.userId}")).json

    def set_amino_id(self, aminoId: str):
        """
        `**set_amino_id**` - Sets the amino id.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        bot.run(email=email, password=password)
        response = bot.set_amino_id(aminoId="aminoId")
        print(response)
        ```
        """
        return SResponse(self.session.handler(
            method = "POST", url="/g/s/account/change-amino-id",
            data={
                "aminoId": aminoId,
                "timestamp": int(time() * 1000)
            })).json

    def fetch_wallet(self):
        """
        `**fetch_wallet**` - Fetches the wallet information.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        bot.run(email=email, password=password)
        response = bot.fetch_wallet()
        print(response)
        """
        return Wallet(self.session.handler(
            method = "GET", url="/g/s/wallet")).json

    def request_security_validation(self, email: str, resetPassword: bool = False):
        """
        `**request_security_validation**` - Requests a security validation.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        response = bot.request_security_validation(email=email)
        print(response)
        ```
        """
        return SResponse(self.session.handler(
            method = "POST", url="/g/s/auth/request-security-validation",
            data={
                "identity": email,
                "type": 1,
                "deviceID": device_id(),
                "level": 2 if resetPassword else None,
                "purpose": "reset-password" if resetPassword else None,
                "timestamp": int(time() * 1000)
            })).json

    def activate_email(self, email: str, code: str):
        """
        `**activate_email**` - Activates an email.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        response = bot.activate_email(email=email, code=code)
        print(response)
        ```
        """
        return SResponse(self.session.handler(
            method = "POST", url="/g/s/auth/activate-email",
            data={
                "type": 1,
                "identity": email,
                "data": {
                    "code":code
                    },
                "deviceID": device_id(),
                "timestamp": int(time() * 1000)
            })).json

    def reset_password(self, email: str, new_password: str, code: str):
        """
        `**reset_password**` - Resets the password.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        bot.run(email=email, password=password)
        response = bot.reset_password(email=email, new_password=new_password, code=code)
        print(response)
        ```
        """
        return ResetPassword(self.session.handler(
            method = "POST", url="/g/s/auth/reset-password",
            data={
                "updateSecret": f"0 {new_password}",
                "emailValidationContext": {
                    "data": {
                        "code": code
                    },
                    "type": 1,
                    "identity": email,
                    "level": 2,
                    "deviceID": device_id()
                },
                "phoneNumberValidationContext": None,
                "deviceID": device_id()
            }))