import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Competition from './views/Competition.vue'
import CompetitionResult from './views/CompetitionResults'
import Athletes from './views/Athletes'
import NotFound from './views/404'
import Teams from './views/Teams'
import Team from './components/teams/Team'
import Athlete from './components/athletes/Athlete'
import StageResult from './components/competitions/Stage'
import Login from './components/users/Login'
import store from './store/modules/token';
import Register from './components/users/Register'

Vue.use(Router)

const ifAuthenticated = (to, from, next) => {
  if (store.state.token != null) {
    next()
    return
  }
  next('/login')
}

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
      beforeEnter: ifAuthenticated
    },
    {
      path: '/competitions/:id',
      name: 'competitions',
      component: CompetitionResult,
      beforeEnter: ifAuthenticated
    }
    ,
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    }
    ,
    {
      path: '/competitions/:id/:stage',
      name: 'competitions',
      component: StageResult,
      beforeEnter: ifAuthenticated
    }
    ,
    {
      path: '/athletes',
      name: 'athletes',
      component: Athletes,
      beforeEnter: ifAuthenticated
    }
    ,
    {
      path: '/athletes/:id',
      name: 'athletes',
      component: Athlete,
      beforeEnter: ifAuthenticated
    }
    ,
    {
      path: '/teams',
      name: 'teams',
      component: Teams,
      beforeEnter: ifAuthenticated
    },
    {
      path: '/teams/:id',
      name: 'team',
      component: Team,
      beforeEnter: ifAuthenticated
    }
    ,
    {
      path: '*',
      name: 'all',
      component: NotFound
    }
  ]
})
