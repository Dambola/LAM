<template>
  <q-page class="row items-center justify-evenly" padding>
    <div id="welcome-home" class="text-center shadow-3 col-8">
      <div id="welcome-home-title">
        <span>
          <strong>
            Em construção!
          </strong>
        </span>
      </div>
      <div id="welcome-home-text">
        <small>Área de Perfil</small>
      </div>
      <div id="welcome-home-icon">
        <q-icon name="fas fa-exclamation-circle"></q-icon>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'Configurações',
  components: {},
  data() {
    return {};
  },
  methods : {}
}
</script>

<style lang="scss">
#welcome-home {
  background-color: $primary;
  color: white;
  padding: 20px 10px;
  border-radius: 5px;
  #welcome-home-title {
    font-size: 20px;
  }
  #welcome-home-text {
  }
  #welcome-home-icon {
    padding-top: 1px;
    font-size: 50px;
  }
}
</style>