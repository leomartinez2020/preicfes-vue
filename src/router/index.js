import { createRouter, createWebHistory, createWebHashHistory } from 'vue-router'

import Home from '@/views/Home.vue'
import VocabularioCompo from '@/views/VocabularioCompo.vue'

const routes = [
    { path: '/', name: 'Home', component: Home },
    // { path: '/quiz1', name: 'quiz1', component: VocabularioCompo },
    { path: '/quiz/:id', component: ()=>import('@/views/VocabularioCompo.vue') },
]

const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHashHistory(),
    routes, // short for `routes: routes`
    linkActiveClass: 'active-link'
})

export default router
