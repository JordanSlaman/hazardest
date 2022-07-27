import {defineStore} from 'pinia'
import {useStorage} from '@vueuse/core'

import auth from '@/modules/api/auth'
import profile from '@/modules/api/profile'
import session from '@/modules/api/session'

export const useUserStore = defineStore(
    'user',
    {
        state: () => ({
            token: useStorage('token', null),
            username: useStorage('username', null),
            email: useStorage('email', null),
            gravatarUrl: useStorage('gravatarUrl', null)
        }),
        getters: {
            isAuthenticated: (state) => !!state.token,
        },
        actions: {
            async getUser() {
                if (this.token) {
                    const user_response = await auth.getAccountDetails();

                    console.log(user_response)

                    const profile_response = await profile.getProfile();

                    console.log(profile_response)


                    // this.$patch({
                    //     email,
                    //     gravatarUrl
                    // })
                }
            },

            async login(username, password) {
                const response = await auth.login(username, password);

                if (response.status === 200) {
                    const token = response.data.key
                    session.defaults.headers.Authorization = `Token ${token}`
                    this.$patch({
                        username,
                        token
                    })
                    console.log('one')
                    await this.getUser()
                    console.log('two')
                }

                return response
            },
            async logout() {
                const response = await auth.logout();

                this.$patch({
                    token: null,
                    username: null,
                    email: null,
                    gravatarUrl: null
                })

                return response
            },
            async signup(username, email, password1, password2) {
                const response = await auth.createAccount(username, password1, password2, email);

                // Token
                // getUser

                return response
            }

        }
    }
);