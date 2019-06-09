import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Competition from './views/Competition.vue'
import CompetitionResult from './views/CompetitionResults'

Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/competitions',
      name: 'competitions',
      component: Competition,
    },
    {
      path: '/competitions/:id',
      name: 'competitions',
      component: CompetitionResult
    }
  ]
})
