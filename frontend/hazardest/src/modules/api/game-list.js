// import axios from "axios"
import session from './session';

export async function gameList() {
        const response = await session.get(
            "http://127.0.0.1:8000/api/games/",

            // {
            //     headers: {'Authorization': 'Token ' + token},
            // }

        );
        return response.data

}
