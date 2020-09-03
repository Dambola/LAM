<template>
  <q-page class="row items-center justify-evenly" padding>
    <div id="welcome-home" class="text-center shadow-3 col-8">
      <div id="welcome-home-title">
        <span>
          <strong>
            Realize o Login para Entrar!
          </strong>
        </span>
      </div>
      <div id="welcome-home-text">
        <q-input class="q-pt-sm" bg-color="white" outlined v-model="username" label="Login" />
        <q-input class="q-pt-sm" bg-color="white" outlined v-model="password" type="password" label="Password" />
      </div>
      <div id="welcome-home-icon">
        <q-btn @click="submitLogin()" color="white" text-color="primary" label="Entrar" />
      </div>
    </div>
  </q-page>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'

  export default {
    name: 'Configurações',
    components: {},
    data() {
      return {
        username: '',
        password: ''
      };
    },
    methods : {
      ...mapActions('user', ['doLogin']),
      submitLogin () {
        console.log('submiting the login ' + this.password);
        var loginDone = this.doLogin({ 
          username: this.username, password: this.password 
        }).then((can_redirect) => {
          console.log('pode? '+can_redirect);
          if (can_redirect) {
            this.$router.push(this.$route.query.redirect || '/');
          }
        });
      }
    }
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