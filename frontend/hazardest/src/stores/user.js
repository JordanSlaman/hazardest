import {defineStore} from 'pinia'

import * as Auth from '@/modules/api/Auth.js'

export const useUserStore = defineStore(
    'user',
    {
        state: () => ({
            token: '',
            username: ''
        }),

        actions: {
            // logout() {
            //     this.$patch({
            //         name: '',
            //         isAdmin: false,
            //     })

            // },

            async login(username, password) {
                const loginData = await Auth.login(username, password)

                console.log(loginData)
                const token = loginData.key

                this.$patch({
                    username,
                    token
                })
            },
        }
    }
);