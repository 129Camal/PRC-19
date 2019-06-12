import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Competition from './views/Competition.vue'
import CompetitionResult from './views/CompetitionResults'
import Athletes from './views/Athletes'
import Teams from './views/Teams'
import Team from './components/teams/Team'
import Athlete from './components/athletes/Athlete'
import StageResult from './components/competitions/Stage'

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
    ,
    {
      path: '/competitions/:id/:stage',
      name: 'competitions',
      component: StageResult
    }
    ,
    {
      path: '/athletes',
      name: 'athletes',
      component: Athletes
    }
    ,
    {
      path: '/athletes/:id',
      name: 'athletes',
      component: Athlete
    }
    ,
    {
      path: '/teams',
      name: 'teams',
      component: Teams
    },
    {
      path: '/teams/:id',
      name: 'team',
      component: Team
    }
  ]
})
