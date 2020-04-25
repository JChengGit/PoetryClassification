import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Poet from '@/components/Poet'
import Query from '@/components/Query'
import test from '@/components/test'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/poet/',
      name: 'Poet',
      component: Poet
    },
    {
      path: '/query/',
      name: 'Query',
      component: Query
    },
    {
      path: '/test/',
      name: 'test',
      component: test
    },
  ]
})
