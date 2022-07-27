import session from './session';

const baseUrl = 'http://localhost:8000/api'

export default {
    getProfile(userId) {
        return session.get(`${baseUrl}/user/${userId}/profile`);
    }
}
