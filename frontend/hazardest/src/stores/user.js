import axios from 'axios'
import md5 from 'crypto-js/md5';

import {defineStore} from 'pinia'
import {useStorage} from '@vueuse/core'

export const useUserStore = defineStore(
    'user',
    {
        state: () => ({
            token: useStorage('token', null),
            username: useStorage('username', null),
            email: useStorage('email', null),
            gravatarUrl: useStorage('gravatarUrl', null)
        }),
        // getters: {
        //     isAuthenticated() {
        //             return !!this.token
        //     }
        // },
        actions: {
            async getUser() {
                if (this.token) {
                    const response = await axios.get(
                        "http://127.0.0.1:8000/auth/user/",
                        {
                            headers: {'Authorization': 'Token ' + this.token},
                        }
                    );
                    const email = response.data.email

                    const emailHash = md5(email);
                    const gravatarUrl = 'https://www.gravatar.com/avatar/' + emailHash.toString()

                    this.$patch({
                        email,
                        gravatarUrl
                    })
                }
            },

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

                // todo save state to browser?

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