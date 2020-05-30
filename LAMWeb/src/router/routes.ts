import { RouteConfig } from 'vue-router';

const routes: RouteConfig[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { 
        path: '/', component: () => import('pages/Index.vue')
      },
      { 
        path: '/indicacao', component: () => import('pages/Indication.vue')
      },
      { 
        path: '/musica', component: () => import('pages/Music.vue')
      },
      { 
        path: '/relatorio', component: () => import('pages/Report.vue')
      },
      { 
        path: '/perfil', component: () => import('pages/Perfil.vue')
      },
      { 
        path: '/admin', component: () => import('pages/Settings.vue')
      }
    ]
  }
];

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue')
  });
}

export default routes;
