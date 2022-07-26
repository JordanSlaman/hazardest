import {createRouter, createWebHashHistory} from "vue-router/dist/vue-router";

import HomePage from "@/components/pages/HomePage";
import GameList from "@/components/pages/GameList";
import GameFrame from "@/components/pages/GameFrame";

const routes = [
  { path: '/', component: HomePage },
  { path: '/games', component: GameList },
  { path: '/game/:id', component: GameFrame },
]

export const router = createRouter({
  history: createWebHashHistory(),
  routes,
})
