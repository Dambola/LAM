<template>
  <q-card>
    <q-card-section class="row">
      <div class="text-h6">Editar música</div>
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
            :options="getTypesOptions()"
            option-value="id"
            option-label="name"
            emit-value
            map-options
            label="Tipo 1" 
            class="col"
          />
        </div>
        <div class="row" v-if="musicToSubmit.type1">
          <q-select 
            v-model="musicToSubmit.type2" 
            :options="getTypesOptions()"
            option-value="id"
            option-label="name"
            emit-value
            map-options
            label="Tipo 2"
            class="col"
            clearable
          />
        </div>
        <div class="row" v-if="musicToSubmit.type2">
          <q-select 
            v-model="musicToSubmit.type3" 
            :options="getTypesOptions()"
            option-value="id"
            option-label="name"
            emit-value
            map-options
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
  import { mapGetters, mapActions } from 'vuex'
  
  export default {
    props : ['music','id'],
    data () {
      return {
        musicToSubmit: {
          name: this.music.name,
          author: this.music.author,
          type1: this.music.type1,
          type2: this.music.type2,
          type3: this.music.type3
        }
      }
    },
    methods: {
      ...mapActions('musics',['updateMusic']),
      submitForm () {
        this.$refs.name.validate();
        if (!this.$refs.name.hasError){
          this.submitMusic();
        }
      },
      submitMusic () {
        const payload = { 
          id: this.id, 
          name: this.musicToSubmit.name,
          author: this.musicToSubmit.author,
          type1: this.musicToSubmit.type1 ? parseInt(this.musicToSubmit.type1) : null,
          type2: this.musicToSubmit.type2 ? parseInt(this.musicToSubmit.type2) : null,
          type3: this.musicToSubmit.type3 ? parseInt(this.musicToSubmit.type3) : null,
        };

        console.log(this.music.type1, this.music.type2, this.music.type3);

        console.log(payload);

        this.updateMusic(payload).then(done => {
          this.$emit('close');
        }).catch(error => {
          console.log(error);
          this.$emit('openError', error.message);
        });
      },
      getTypesOptions () {
        let options = [];
        Object.keys(this.types).forEach((value, index) => {
          options.push({ 'id': value, 'name': this.types[value].name })
        });
        return options;
      }
    }
  }
</script>

<style lang="scss">

</style>