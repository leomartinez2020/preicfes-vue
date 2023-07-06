import { createRouter, createWebHistory, createWebHashHistory } from 'vue-router'

import Home from '@/views/Home.vue'
//import VocabularioCompo from '@/views/VocabularioCompo.vue'
//import LecturaOracionCompo from '@/views/LecturaOracionCompo.vue'

const routes = [
    { path: '/', name: 'Home', component: Home },
    { path: '/quiz/:id', component: ()=>import('@/views/VocabularioCompo.vue') },
    { path: '/lectura/:id', component: ()=>import('@/views/LecturaOracionCompo.vue') },
    { path: '/lectura2/:id', component: ()=>import('@/views/LecturaVocabularioCompo.vue') },
]

const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHashHistory(),
    routes, // short for `routes: routes`
    linkActiveClass: 'active-link'
})

export default router
