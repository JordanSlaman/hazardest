import {createRouter, createWebHashHistory} from "vue-router/dist/vue-router";

import DonateHazardest from "@/components/pages/DonateHazardest";
import HomePage from "@/components/pages/HomePage";
import GameList from "@/components/pages/GameList";
import GameFrame from "@/components/pages/GameFrame";
import UserProfile from "@/components/pages/UserProfile";

const routes = [
    {path: '/', component: HomePage},
    {path: '/donate', component: DonateHazardest},
    {path: '/games', component: GameList},
    {path: '/game/:id', component: GameFrame},
    {path: '/profile', component: UserProfile},
    {path: '/profile/:id', component: UserProfile},
]

export const router = createRouter({
    history: createWebHashHistory(),
    routes,
})
