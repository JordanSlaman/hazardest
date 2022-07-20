import axios from 'axios'

import {defineStore} from 'pinia'

export const useUserStore = defineStore(
    'user',
    {
        state: () => ({
            token: null,
            username: null
        }),
        actions: {
            // async getUser(authToken) {
            //     const loginData = await Auth.getUser(authToken).then(user => {
            //         this.user = user
            //     })
            //
            //     console.log(loginData)
            //     const token = loginData.key
            //
            //     this.$patch({
            //         username,
            //         token
            //     })
            // },

            async login(username, password) {
                const response = await axios.post(
                    "http://127.0.0.1:8000/auth/login/",
                    {
                        username,
                        password
                    }
                );
                const token = response.data.key

                this.$patch({
                    username,
                    token
                })

                return response
            },
            async logout() {
                const response = await axios.post(
                    "http://127.0.0.1:8000/auth/logout/"
                );
                const x = response.data
                console.log(x)

                this.$patch({
                    username: null,
                    token: null
                })

                return response
            },
            async signup(username, email, password1, password2) {
                const response = await axios.post(
                    "http://127.0.0.1:8000/auth/registration/",
                    {
                        username,
                        email,
                        password1,
                        password2
                    }
                );
                const x = response.data
                console.log(x)
                // todo stuff

                return response
            }

        }
    }
);