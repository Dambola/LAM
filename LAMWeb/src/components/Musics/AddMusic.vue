<template>
  <q-card>
    <q-card-section class="row">
      <div class="text-h6">Nova música</div>
      <q-space />
      <q-btn 
        flat
        round
        dense
        v-close-popup
        icon="close"
      />
    </q-card-section>
    <form @submit.prevent="submitForm">
      <q-card-section class="q-pt-none">
        <div class="row">
          <q-input
            v-model="musicToSubmit.name"
            label="Nome da Música"
            class="col"
            ref="name"
            :rules="[val => !!val || 'Nome da música é necessário']"
          />
        </div>
        <div class="row">
          <q-input
            v-model="musicToSubmit.author"
            label="Autor da Música"
            class="col"
          />
        </div>
        <div class="row">
          <q-select 
            v-model="musicToSubmit.type1" 
            :options="types" 
            label="Tipo 1" 
            class="col"
          />
        </div>
        <div class="row" v-if="musicToSubmit.type1">
          <q-select 
            v-model="musicToSubmit.type2" 
            :options="types" 
            label="Tipo 2"
            class="col"
            clearable
          />
        </div>
        <div class="row" v-if="musicToSubmit.type2">
          <q-select 
            v-model="musicToSubmit.type3" 
            :options="types" 
            label="Tipo 3" 
            class="col"
            clearable 
          />
        </div>

      </q-card-section>

      <q-card-actions align="right">
        <q-btn 
          label="Save" 
          color="primary"
          type="submit"
        />
      </q-card-actions>
    </form>
  </q-card>
</template>

<script>
  import { mapActions } from 'vuex'
  
  export default {
    data () {
      return {
        musicToSubmit: {
          name: '',
          author: '',
          type1: '',
          type2: '',
          type3: ''
        },
        types: [
          'Adoração',
          'Oração',
          'Júbilo'
        ]
      }
    },
    methods: {
      ...mapActions('musics',['createMusic']),
      submitForm () {
        this.$refs.name.validate()
        if (!this.$refs.name.hasError){
          this.submitMusic()
        }
      },
      submitMusic () {
        this.createMusic(this.musicToSubmit)
        this.$emit('close')
      }
    }
  }
</script>

<style lang="scss">

</style>