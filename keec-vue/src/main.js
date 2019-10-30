// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import router from './router';

import MuseUI from 'muse-ui';
import 'muse-ui/dist/muse-ui.css';
import theme from 'muse-ui/lib/theme';

Vue.use(MuseUI.Grid);
Vue.use(MuseUI.Pagination);

theme.add('keec_theme', {
  primary: '#3914AF',
  
  text: {
    primary: '#FFD300',
    secondary: '#A68900',
    alternate: '#3914AF',
  },
  background: {
    paper: '#200772',
    chip: '#FFDE40',
    default: '#FFE773',
  },
}, 'light');

theme.use('keec_theme');

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
