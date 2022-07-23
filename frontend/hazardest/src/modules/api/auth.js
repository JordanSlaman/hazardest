import session from './session';

const baseUrl = 'http://localhost:8000/auth'

export default {
    login(username, password) {
        return session.post(`${baseUrl}/login/`, {username, password});
    },
    logout() {
        return session.post(`${baseUrl}/logout/`, {});
    },
    createAccount(username, password1, password2, email) {
        return session.post(`${baseUrl}/registration/`, {username, password1, password2, email});
    },
    changeAccountPassword(password1, password2) {
        return session.post(`${baseUrl}/password/change/`, {password1, password2});
    },
    sendAccountPasswordResetEmail(email) {
        return session.post(`${baseUrl}/password/reset/`, {email});
    },
    resetAccountPassword(uid, token, new_password1, new_password2) { // eslint-disable-line camelcase
        return session.post(`${baseUrl}/password/reset/confirm/`, {uid, token, new_password1, new_password2});
    },
    getAccountDetails() {
        return session.get(`${baseUrl}/user/`);
    },
    updateAccountDetails(data) {
        return session.patch(`${baseUrl}/user/`, data);
    },
    verifyAccountEmail(key) {
        return session.post(`${baseUrl}/registration/verify-email/`, {key});
    }
};
