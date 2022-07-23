import session from './session';

const baseUrl = 'http://localhost:8000/api'

export default {
    gameList() {
        return session.get(`${baseUrl}/games/`);
    }
}


