<template>
  <q-page class="row items-center justify-evenly" padding>
    <div id="login-page" class="text-center shadow-3 col-8">
      <div id="login-page-title">
        <span>
          <strong>
            Realize o Login para Entrar!
          </strong>
        </span>
      </div>
      <div id="login-page-text">
        <q-input class="q-pt-sm" bg-color="white" outlined v-model="username" label="Login" name="login" />
        <q-input class="q-pt-sm" bg-color="white" outlined v-model="password" type="password" label="Password" name="password" />
      </div>
      <div id="login-page-icon">
        <q-btn @click="submitLogin()" color="white" text-color="primary" label="Entrar" name="entrar" />
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
      async submitLogin () {
        const params = {
            login: this.username,
            password: this.password
        };

        try {
          const response = await this.$axios.post('auth', params);
          const { data } = await response;
          localStorage.setItem('login', data.login);
          localStorage.setItem('email', data.email);
          this.$router.go('/');

        } catch (error) {  
          console.log(error);
        }

      }
    }
  }
</script>

<style lang="scss">
#login-page {
  background-color: $primary;
  color: white;
  padding: 20px 10px;
  border-radius: 5px;
  
  #login-page-title {
    font-size: 20px;
  }

  #login-page-icon {
    padding-top: 1px;
    font-size: 50px;
  }
}
</style>