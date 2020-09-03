<template>
  <q-page class="items-center justify-evenly" padding>
    <div class="box perfil text-center absolute-full q-ma-sm p">
      <div>
        <q-avatar color="primary" text-color="white" size="120px">DN</q-avatar>
      </div>
      <div>
        <p class="name">Daniel Nogueira Rebouças</p>
      </div>
      <div class="atributtes text-left">
        <div class="attribute">
          <span class="key">Apelido: </span>
          <span class="value">Dambola</span>
        </div>
        <div class="attribute">
          <span class="key">Email: </span>
          <span class="value">danielnreboucas@hotmail.com</span>
        </div>
        <div class="attribute">
          <span class="key">Data de Nascimento: </span>
          <span class="value">12/10/1996</span>
        </div>
        <div class="attribute">
          <span class="key">Data de Entrada: </span>
          <span class="value">03/09/2015</span>
        </div>
        <div class="attribute">
          <span class="key">Sexo: </span>
          <span class="value">Masculino</span>
        </div>
        <div class="attribute">
          <span class="key">Descrição:</span>
        </div>
        <div class="attribute">
          <span class="value">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab pariatur, atque quod iste architecto, itaque dolore earum quos temporibus repellendus quam, cum reiciendis adipisci quasi accusantium voluptas aliquid eos sed!</span>
        </div>
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
.perfil {
  margin: 15px;
  padding: 5px;
  background-color: white;
  
  .atributtes {
    padding-top: 5px;
    .attribute {
      padding: 0px 20px;
      span.key {
        font-size: 14px;
        font-weight: 600;
      }
      span.value {
        font-size: 13px;
      }
    }
  }

  .name {
    font-size: 20px;
    font-weight: 500;
  }
}
</style>
