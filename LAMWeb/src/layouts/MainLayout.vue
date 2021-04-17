<template>
  <q-layout view="hHh LpR lFf">
    <q-header id="menu-header" elevated>
      <q-toolbar id="menu-toolbar">
        <!-- <q-btn flat @click="leftDrawerOpen = !leftDrawerOpen" round dense icon="menu" class="computer"/> -->
        <q-toolbar-title class="text-center">
          <img id="menu-logo" src="../assets/logobordered.png" class="vertical-middle">
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <!-------- Mobile Navegation Bar -------->
    <q-footer elevated>
      <q-tabs>
        <q-route-tab
          v-for="(item,index) in menuItems"
          :key="index"
          :icon="item.icon" 
          :label="item.title"
          :to="item.link"
          exact
        />
      </q-tabs>
    </q-footer>

    <!-------- Computer Navegation Bar -------->
    <!-- <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-1"
      class="computer"
    >
      <q-list>
        <q-item-label
          header
          class="text-grey-8"
        >
          Essential Links
        </q-item-label>
        <q-item
          clickable
          tag="a"
          v-for="(item,index) in menuItems"
          :key="index"
          :to="item.link"
          exact
        >
          <q-item-section
            v-if="item.icon"
            avatar
          >
            <q-icon :name="item.icon" />
          </q-item-section>

          <q-item-section>
            <q-item-label>{{ item.title }}</q-item-label>
            <q-item-label caption>
              {{ item.caption }}
            </q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer> -->

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: 'MainLayout',

  data () {
    return {
      leftDrawerOpen: false,
      menuItems: [
        {
          title: 'Home',
          caption: 'Início',
          icon: 'fas fa-home',
          link: '/'
        },
        // {
        //   title: 'Indicação',
        //   caption: 'Início',
        //   icon: 'fas fa-plus-square',
        //   link: '/indicacao'
        // },
        {
          title: 'Música',
          caption: 'Lista de Músicas',
          icon: 'fas fa-music',
          link: '/musica'
        },
        // {
        //   title: 'Relatório',
        //   caption: 'Lista de Músicas',
        //   icon: 'fas fa-clipboard',
        //   link: '/relatorio'
        // },
        // {
        //   title: 'Admin',
        //   caption: 'Página de Administração',
        //   icon: 'fas fa-tools',
        //   link: '/admin'
        // },
        // {
        //   title: 'Perfil',
        //   caption: 'Página de Administração',
        //   icon: 'fas fa-user',
        //   link: '/perfil'
        // },
      ]
    }
  }
}
</script>

<style lang="scss">
  #menu-header {
    #menu-toolbar {
      height: 60px;
      #menu-logo {
        width: 90px; 
        padding-right: 15px;
        text-shadow: 1px 1px white;
      }
      #menu-text {
        font-size: 25px;
      }
    }
  }

</style>