import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/Home';
import AllNews from '@/components/AllNews';
import Legals from "../components/Legals";
import Contacts from "../components/Contacts";
import Clubs from "../components/Clubs";
import AllEvents from "../components/AllEvents";
import About from "../components/About";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },

    {
      path: '/news',
      name: 'all-news',
      component: AllNews,
    },

    {
      path: '/legal',
      name: 'legals',
      component: Legals,
    },

    {
      path: '/contact',
      name: 'contacts',
      component: Contacts,
    },

    {
      path: '/clubs',
      name: 'clubs',
      component: Clubs,
    },

    {
      path: '/events',
      name: 'all-events',
      component: AllEvents,
    },

    {
      path: '/about',
      name: 'about',
      component: About,
    },

  ],
});
