import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Poet from '@/components/Poet'
import Query from '@/components/Query'
import Retrieve from '@/components/Retrieve'
import Classifier from '@/components/Classifier'

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
      path: '/retrieve/',
      name: 'Retrieve',
      component: Retrieve
    },
    {
      path: '/classifier/',
      name: 'Classifier',
      component: Classifier
    },
  ]
})
